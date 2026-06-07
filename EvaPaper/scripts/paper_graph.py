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
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


OPENALEX_BASE = "https://api.openalex.org"
S2_BASE = "https://api.semanticscholar.org/graph/v1"
DEFAULT_MAILTO = os.environ.get("OPENALEX_MAILTO", "evapaper@example.com")


def _http_json(url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 30) -> dict:
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


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

    seed_works = openalex.search_works(query, per_page=seed_limit, from_year=from_year)
    if not seed_works:
        return {"query": query, "seeds": [], "candidates": []}

    seeds = [openalex_to_node(work, "openalex", 0, "query_seed") for work in seed_works]
    candidates: Dict[str, PaperNode] = {}

    for seed_work, seed_node in zip(seed_works, seeds):
        candidates[seed_node.paper_id] = seed_node

        referenced_ids = seed_work.get("referenced_works", [])[:neighbors_per_seed]
        related_ids = seed_work.get("related_works", [])[:neighbors_per_seed]

        for work in openalex.get_works_by_ids(referenced_ids):
            node = openalex_to_node(work, "openalex", 1, f"references:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        for work in openalex.get_works_by_ids(related_ids):
            node = openalex_to_node(work, "openalex", 1, f"related:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        for work in openalex.get_citing_works(seed_work["id"].rsplit("/", 1)[-1], per_page=neighbors_per_seed):
            node = openalex_to_node(work, "openalex", 1, f"cites_seed:{seed_node.paper_id}")
            node.score = compute_score(node)
            candidates.setdefault(node.paper_id, node)
            if candidates[node.paper_id] is not node:
                merge_node(candidates[node.paper_id], node)

        if include_semantic_scholar:
            identifier = seed_work.get("doi") or seed_work["id"].rsplit("/", 1)[-1]
            for work in s2.recommendations(identifier, limit=neighbors_per_seed):
                node = s2_to_node(work, f"s2_recommendation:{seed_node.paper_id}")
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
