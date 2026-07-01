#!/usr/bin/env python3
"""
Graph-backed paper discovery for EvaPaper.

This script uses public scholarly graph APIs to expand from a query or seed paper
into a citation neighborhood that is better than plain keyword search alone.

Primary provider: OpenAlex
Optional provider: Semantic Scholar recommendations API
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.error import HTTPError, URLError


OPENALEX_BASE = "https://api.openalex.org"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
ARXIV_BASE = "https://export.arxiv.org/api/query"
DEFAULT_MAILTO = os.environ.get("OPENALEX_MAILTO", "evapaper@example.com")
DEFAULT_USER_AGENT = os.environ.get(
    "EVAPAPER_USER_AGENT",
    f"EvaPaper/1.0 (mailto:{DEFAULT_MAILTO})",
)


def _http_json(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 30,
    retries: int = 2,
    backoff: float = 1.0,
    max_delay: float = 5.0,
) -> dict:
    request_headers = {"User-Agent": DEFAULT_USER_AGENT}
    request_headers.update(headers or {})
    last_error: Exception | None = None

    for attempt in range(retries):
        request = urllib.request.Request(url, headers=request_headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            last_error = exc
            if exc.code not in {408, 429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
            retry_after = exc.headers.get("Retry-After")
            delay = float(retry_after) if retry_after and retry_after.isdigit() else backoff * (2**attempt)
            delay = min(delay, max_delay)
            time.sleep(delay)
        except URLError as exc:
            last_error = exc
            if attempt == retries - 1:
                raise
            time.sleep(backoff * (2**attempt))

    if last_error:
        raise last_error
    raise RuntimeError(f"Request failed without an exception: {url}")


def _http_text(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 30,
    retries: int = 2,
    backoff: float = 1.0,
    max_delay: float = 5.0,
) -> str:
    request_headers = {"User-Agent": DEFAULT_USER_AGENT}
    request_headers.update(headers or {})
    last_error: Exception | None = None

    for attempt in range(retries):
        request = urllib.request.Request(url, headers=request_headers)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8")
        except HTTPError as exc:
            last_error = exc
            if exc.code not in {408, 429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
            retry_after = exc.headers.get("Retry-After")
            delay = float(retry_after) if retry_after and retry_after.isdigit() else backoff * (2**attempt)
            delay = min(delay, max_delay)
            time.sleep(delay)
        except URLError as exc:
            last_error = exc
            if attempt == retries - 1:
                raise
            time.sleep(backoff * (2**attempt))

    if last_error:
        raise last_error
    raise RuntimeError(f"Request failed without an exception: {url}")


def _safe_get(dct: dict, path: Sequence[str], default=None):
    current = dct
    for part in path:
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return current


def _chunked(values: Sequence[str], size: int) -> Iterable[Sequence[str]]:
    for i in range(0, len(values), size):
        yield values[i : i + size]


@dataclass
class PaperNode:
    paper_id: str
    title: str
    year: Optional[int]
    url: Optional[str]
    abstract: Optional[str]
    citation_count: int
    source: str
    seed_distance: int = 999
    matched_edges: List[str] = field(default_factory=list)
    topics: List[str] = field(default_factory=list)
    score: float = 0.0


class OpenAlexClient:
    def __init__(self, api_key: Optional[str] = None, mailto: str = DEFAULT_MAILTO):
        self.api_key = api_key or os.environ.get("OPENALEX_API_KEY")
        self.mailto = mailto

    def _build_url(self, path: str, params: Dict[str, str]) -> str:
        query = dict(params)
        if self.api_key:
            query["api_key"] = self.api_key
        if self.mailto:
            query["mailto"] = self.mailto
        return f"{OPENALEX_BASE}{path}?{urllib.parse.urlencode(query, doseq=True)}"

    def search_works(self, query: str, per_page: int = 10, from_year: Optional[int] = None) -> List[dict]:
        filters = []
        if from_year is not None:
            filters.append(f"from_publication_date:{from_year}-01-01")
        params = {
            "search": query,
            "per-page": str(per_page),
            "sort": "relevance_score:desc",
            "select": "id,display_name,publication_year,cited_by_count,doi,primary_location,abstract_inverted_index,topics,referenced_works,related_works",
        }
        if filters:
            params["filter"] = ",".join(filters)
        payload = _http_json(self._build_url("/works", params))
        return payload.get("results", [])

    def get_work(self, work_id: str) -> dict:
        params = {
            "select": "id,display_name,publication_year,cited_by_count,doi,primary_location,abstract_inverted_index,topics,referenced_works,related_works",
        }
        return _http_json(self._build_url(f"/works/{urllib.parse.quote(work_id, safe=':/')}", params))

    def get_works_by_ids(self, work_ids: Sequence[str]) -> List[dict]:
        if not work_ids:
            return []
        results: List[dict] = []
        for batch in _chunked(list(dict.fromkeys(work_ids)), 25):
            payload = _http_json(
                self._build_url(
                    "/works",
                    {
                        "filter": f"openalex:{'|'.join(batch)}",
                        "per-page": str(len(batch)),
                        "select": "id,display_name,publication_year,cited_by_count,doi,primary_location,abstract_inverted_index,topics,referenced_works,related_works",
                    },
                )
            )
            results.extend(payload.get("results", []))
            time.sleep(0.1)
        return results

    def get_citing_works(self, work_id: str, per_page: int = 20) -> List[dict]:
        payload = _http_json(
            self._build_url(
                "/works",
                {
                    "filter": f"cites:{work_id}",
                    "per-page": str(per_page),
                    "sort": "cited_by_count:desc",
                    "select": "id,display_name,publication_year,cited_by_count,doi,primary_location,abstract_inverted_index,topics",
                },
            )
        )
        return payload.get("results", [])


class SemanticScholarClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

    def recommendations(self, paper_id: str, limit: int = 10) -> List[dict]:
        if not self.api_key:
            return []
        url = (
            f"{S2_BASE}/paper/{urllib.parse.quote(paper_id, safe='')}/recommendations"
            f"?fields=paperId,title,year,abstract,citationCount,url&limit={limit}"
        )
        payload = _http_json(url, headers={"x-api-key": self.api_key})
        return payload.get("recommendedPapers", [])

    def search_papers(self, query: str, limit: int = 10, from_year: Optional[int] = None) -> List[dict]:
        fields = "paperId,title,year,abstract,citationCount,url,externalIds"
        params = {"query": query, "limit": str(limit), "fields": fields}
        if from_year is not None:
            params["year"] = f"{from_year}-"
        headers = {"x-api-key": self.api_key} if self.api_key else {}
        payload = _http_json(
            f"{S2_BASE}/paper/search?{urllib.parse.urlencode(params)}",
            headers=headers,
            retries=2 if self.api_key else 1,
            backoff=2.0,
        )
        return payload.get("data", [])


class ArxivClient:
    def search_papers(self, query: str, limit: int = 10, from_year: Optional[int] = None) -> List[dict]:
        params = {
            "search_query": self._query_syntax(query),
            "start": "0",
            "max_results": str(limit),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        xml_text = _http_text(f"{ARXIV_BASE}?{urllib.parse.urlencode(params)}", retries=3, backoff=1.0)
        root = ET.fromstring(xml_text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        papers: List[dict] = []
        for entry in root.findall("atom:entry", ns):
            paper = self._entry_to_paper(entry, ns)
            if from_year is not None and paper.get("year") and paper["year"] < from_year:
                continue
            papers.append(paper)
        return papers

    @staticmethod
    def _query_syntax(query: str) -> str:
        tokens = [token.lower() for token in re.findall(r"[A-Za-z0-9][A-Za-z0-9-]{2,}", query)]
        clauses: List[str] = []
        if query.strip():
            clauses.append(f'all:"{query.strip()}"')
        for left, right in zip(tokens, tokens[1:]):
            clauses.append(f'all:"{left} {right}"')
        if tokens:
            clauses.append(" AND ".join(f"all:{token}" for token in tokens[: min(3, len(tokens))]))
        return " OR ".join(dict.fromkeys(clauses[:8])) or "all:agent"

    @staticmethod
    def _entry_to_paper(entry: ET.Element, ns: dict) -> dict:
        def text(path: str) -> str:
            node = entry.find(path, ns)
            return "" if node is None or node.text is None else " ".join(node.text.split())

        url = text("atom:id")
        arxiv_id = url.rsplit("/", 1)[-1] if url else ""
        published = text("atom:published")
        year = int(published[:4]) if published[:4].isdigit() else None
        topics = [category.attrib.get("term", "") for category in entry.findall("atom:category", ns)]
        return {
            "paperId": f"arXiv:{arxiv_id}",
            "title": text("atom:title"),
            "year": year,
            "abstract": text("atom:summary"),
            "citationCount": 0,
            "url": url,
            "externalIds": {"ArXiv": arxiv_id},
            "topics": topics,
        }


def openalex_to_node(work: dict, source: str, seed_distance: int, edge_label: str) -> PaperNode:
    doi = _safe_get(work, ["doi"])
    location_url = _safe_get(work, ["primary_location", "landing_page_url"])
    topics = [topic.get("display_name", "") for topic in work.get("topics", [])[:5] if topic.get("display_name")]
    return PaperNode(
        paper_id=work["id"].rsplit("/", 1)[-1],
        title=work.get("display_name", "").strip(),
        year=work.get("publication_year"),
        url=doi or location_url or work.get("id"),
        abstract=reconstruct_abstract(work.get("abstract_inverted_index")),
        citation_count=work.get("cited_by_count", 0),
        source=source,
        seed_distance=seed_distance,
        matched_edges=[edge_label],
        topics=topics,
    )


def s2_to_node(work: dict, edge_label: str) -> PaperNode:
    return PaperNode(
        paper_id=work.get("paperId", ""),
        title=work.get("title", "").strip(),
        year=work.get("year"),
        url=work.get("url"),
        abstract=work.get("abstract"),
        citation_count=work.get("citationCount", 0),
        source="semantic_scholar",
        seed_distance=1,
        matched_edges=[edge_label],
        topics=[],
    )


def arxiv_to_node(work: dict, seed_distance: int, edge_label: str) -> PaperNode:
    return PaperNode(
        paper_id=work.get("paperId", ""),
        title=work.get("title", "").strip(),
        year=work.get("year"),
        url=work.get("url"),
        abstract=work.get("abstract"),
        citation_count=work.get("citationCount", 0),
        source="arxiv",
        seed_distance=seed_distance,
        matched_edges=[edge_label],
        topics=work.get("topics", []),
    )


def reconstruct_abstract(inverted_index: Optional[dict]) -> Optional[str]:
    if not inverted_index:
        return None
    words: List[Tuple[int, str]] = []
    for token, positions in inverted_index.items():
        for position in positions:
            words.append((position, token))
    if not words:
        return None
    return " ".join(token for _, token in sorted(words))


def merge_node(existing: PaperNode, new_node: PaperNode) -> None:
    existing.seed_distance = min(existing.seed_distance, new_node.seed_distance)
    existing.citation_count = max(existing.citation_count, new_node.citation_count)
    existing.score = max(existing.score, new_node.score)
    for edge in new_node.matched_edges:
        if edge not in existing.matched_edges:
            existing.matched_edges.append(edge)
    for topic in new_node.topics:
        if topic not in existing.topics:
            existing.topics.append(topic)
    if not existing.abstract and new_node.abstract:
        existing.abstract = new_node.abstract
    if not existing.url and new_node.url:
        existing.url = new_node.url


def compute_score(node: PaperNode) -> float:
    citation_score = math.log10(node.citation_count + 1)
    edge_bonus = len(node.matched_edges) * 1.2
    distance_penalty = 0.8 * max(node.seed_distance - 1, 0)
    recency_bonus = 0.0
    if node.year:
        recency_bonus = max(0, node.year - 2022) * 0.15
    return round(citation_score + edge_bonus + recency_bonus - distance_penalty, 3)


def discover_from_query(
    query: str,
    seed_limit: int = 5,
    neighbors_per_seed: int = 10,
    from_year: Optional[int] = None,
    include_semantic_scholar: bool = False,
) -> Dict[str, object]:
    openalex = OpenAlexClient()
    s2 = SemanticScholarClient()
    arxiv = ArxivClient()
    provider_errors: List[str] = []

    try:
        seed_works = openalex.search_works(query, per_page=seed_limit, from_year=from_year)
    except Exception as exc:
        seed_works = []
        provider_errors.append(f"openalex search failed: {type(exc).__name__}: {exc}")

    seeds = [openalex_to_node(work, "openalex", 0, "query_seed") for work in seed_works]
    candidates: Dict[str, PaperNode] = {}

    for seed_work, seed_node in zip(seed_works, seeds):
        candidates[seed_node.paper_id] = seed_node

        referenced_ids = seed_work.get("referenced_works", [])[:neighbors_per_seed]
        related_ids = seed_work.get("related_works", [])[:neighbors_per_seed]

        try:
            referenced_works = openalex.get_works_by_ids(referenced_ids)
        except Exception as exc:
            referenced_works = []
            provider_errors.append(f"openalex references failed for {seed_node.paper_id}: {type(exc).__name__}: {exc}")
        for work in referenced_works:
            node = openalex_to_node(work, "openalex", 1, f"references:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        try:
            related_works = openalex.get_works_by_ids(related_ids)
        except Exception as exc:
            related_works = []
            provider_errors.append(f"openalex related failed for {seed_node.paper_id}: {type(exc).__name__}: {exc}")
        for work in related_works:
            node = openalex_to_node(work, "openalex", 1, f"related:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        try:
            citing_works = openalex.get_citing_works(seed_work["id"].rsplit("/", 1)[-1], per_page=neighbors_per_seed)
        except Exception as exc:
            citing_works = []
            provider_errors.append(f"openalex citations failed for {seed_node.paper_id}: {type(exc).__name__}: {exc}")
        for work in citing_works:
            node = openalex_to_node(work, "openalex", 1, f"cites_seed:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        if include_semantic_scholar:
            identifier = seed_work.get("doi") or seed_work["id"].rsplit("/", 1)[-1]
            try:
                recommended_works = s2.recommendations(identifier, limit=neighbors_per_seed)
            except Exception as exc:
                recommended_works = []
                provider_errors.append(f"semantic scholar recommendations failed for {seed_node.paper_id}: {type(exc).__name__}: {exc}")
            for work in recommended_works:
                node = s2_to_node(work, f"s2_recommendation:{seed_node.paper_id}")
                node.score = compute_score(node)
                candidates.setdefault(node.paper_id, node)
                if candidates[node.paper_id] is not node:
                    merge_node(candidates[node.paper_id], node)

    if not seed_works:
        try:
            arxiv_works = arxiv.search_papers(query, limit=max(seed_limit, neighbors_per_seed), from_year=from_year)
        except Exception as exc:
            arxiv_works = []
            provider_errors.append(f"arxiv search failed: {type(exc).__name__}: {exc}")

        seeds = [arxiv_to_node(work, 0, "arxiv_query_seed") for work in arxiv_works[:seed_limit]]
        for work in arxiv_works:
            node = arxiv_to_node(work, 1, "arxiv_live_search")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        try:
            s2_works = s2.search_papers(query, limit=neighbors_per_seed, from_year=from_year)
        except Exception as exc:
            s2_works = []
            provider_errors.append(f"semantic scholar search failed: {type(exc).__name__}: {exc}")
        for work in s2_works:
            node = s2_to_node(work, "s2_live_search")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

    for node in candidates.values():
        node.score = compute_score(node)

    ranked = sorted(
        (node for node in candidates.values() if node.seed_distance > 0),
        key=lambda node: (-node.score, -(node.citation_count or 0), -(node.year or 0)),
    )

    return {
        "query": query,
        "seeds": [node.__dict__ for node in seeds],
        "candidates": [node.__dict__ for node in ranked],
        "provider_errors": provider_errors,
    }


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover papers via scholarly citation graphs.")
    parser.add_argument("query", help="Seed query for initial paper lookup")
    parser.add_argument("--seed-limit", type=int, default=5, help="How many initial query matches to expand")
    parser.add_argument(
        "--neighbors-per-seed",
        type=int,
        default=10,
        help="How many references / related works / citing papers to pull per seed",
    )
    parser.add_argument("--from-year", type=int, default=None, help="Only seed from works published on or after this year")
    parser.add_argument(
        "--include-semantic-scholar",
        action="store_true",
        help="Add Semantic Scholar recommendations when SEMANTIC_SCHOLAR_API_KEY is set",
    )
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of a text summary")
    return parser.parse_args(argv)


def print_text_report(result: dict) -> None:
    print(f"Query: {result['query']}")
    print("")
    print("Seed papers:")
    for idx, seed in enumerate(result["seeds"], start=1):
        print(f"{idx}. {seed['title']} ({seed.get('year') or 'n/a'}) [{seed['paper_id']}]")
    print("")
    print("Graph-ranked candidates:")
    for idx, candidate in enumerate(result["candidates"][:20], start=1):
        edges = ", ".join(candidate["matched_edges"][:3])
        topics = ", ".join(candidate.get("topics", [])[:3])
        print(
            f"{idx}. {candidate['title']} ({candidate.get('year') or 'n/a'})"
            f" | score={candidate['score']}"
            f" | citations={candidate['citation_count']}"
            f" | via={edges}"
        )
        if candidate.get("url"):
            print(f"   {candidate['url']}")
        if topics:
            print(f"   topics: {topics}")


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    result = discover_from_query(
        query=args.query,
        seed_limit=args.seed_limit,
        neighbors_per_seed=args.neighbors_per_seed,
        from_year=args.from_year,
        include_semantic_scholar=args.include_semantic_scholar,
    )
    if args.json:
        json.dump(result, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print_text_report(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
