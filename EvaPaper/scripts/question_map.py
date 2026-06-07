#!/usr/bin/env python3
"""
Map a user question to the papers in the local corpus that best answer it.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from typing import Dict, List, Sequence, Tuple

from paper_corpus import DEFAULT_INDEX, DEFAULT_REPORT, build_index


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "do", "does", "for", "from", "how",
    "i", "if", "in", "into", "is", "it", "me", "my", "of", "on", "or", "our", "that", "the",
    "their", "them", "there", "these", "this", "to", "use", "using", "want", "what", "when",
    "which", "who", "with", "you", "your", "paper", "papers", "only", "rather", "than", "instead", "just",
}

FIELD_WEIGHTS = {
    "paper_summary": 1.4,
    "abstract": 1.25,
    "relevance": 1.35,
    "why_recommend": 1.1,
    "recommendation_reason": 1.1,
}

MODE_ALIASES = {
    "all": "all",
    "sota": "all",
    "static": "static",
    "static-first": "static",
    "spec": "static",
    "runtime": "runtime",
    "behavioral": "behavioral",
    "landscape": "landscape",
}

CANONICAL_TOKEN_MAP = {
    "evaluate": "evaluat",
    "evaluates": "evaluat",
    "evaluated": "evaluat",
    "evaluating": "evaluat",
    "evaluation": "evaluat",
    "evaluations": "evaluat",
    "evaluator": "evaluat",
    "evaluators": "evaluat",
    "runtime": "runtime",
    "enforce": "enforc",
    "enforces": "enforc",
    "enforced": "enforc",
    "enforcement": "enforc",
    "enforcing": "enforc",
    "validate": "valid",
    "validates": "valid",
    "validated": "valid",
    "validation": "valid",
    "validator": "valid",
    "validators": "valid",
    "behavior": "behavior",
    "behavioral": "behavior",
    "behaviour": "behavior",
    "behavioural": "behavior",
    "governance": "govern",
    "governing": "govern",
    "secure": "secur",
    "security": "secur",
    "skills": "skill",
    "papers": "paper",
    "paper": "paper",
}


def normalize_token(token: str) -> str:
    token = token.lower()
    if token in CANONICAL_TOKEN_MAP:
        return CANONICAL_TOKEN_MAP[token]
    if len(token) > 4 and token.endswith("ies"):
        token = token[:-3] + "y"
    elif len(token) > 5 and token.endswith("ing"):
        token = token[:-3]
    elif len(token) > 4 and token.endswith("ed"):
        token = token[:-2]
    elif len(token) > 4 and token.endswith("es"):
        token = token[:-2]
    elif len(token) > 3 and token.endswith("s"):
        token = token[:-1]
    if token in CANONICAL_TOKEN_MAP:
        return CANONICAL_TOKEN_MAP[token]
    return token


def tokenize(text: str) -> List[str]:
    raw_tokens = re.findall(r"[A-Za-z0-9\-\+\.]+", text.lower())
    tokens = []
    for raw in raw_tokens:
        token = normalize_token(raw.strip("."))
        if len(token) < 2 or token in STOPWORDS:
            continue
        tokens.append(token)
    return tokens


def load_records_with_passages(index_path=DEFAULT_INDEX) -> List[dict]:
    if not index_path.exists():
        build_index(DEFAULT_REPORT, index_path)
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    return payload.get("papers", [])


def normalize_mode(mode: str) -> str:
    lowered = mode.strip().lower()
    if lowered not in MODE_ALIASES:
        raise ValueError(f"Unsupported mode: {mode}")
    return MODE_ALIASES[lowered]


def build_passage_stats(papers: List[dict]) -> Tuple[Dict[str, float], int]:
    doc_freq: Counter = Counter()
    total_passages = 0
    for paper in papers:
        for passage in paper.get("passages", []):
            total_passages += 1
            unique_tokens = set(tokenize(passage.get("text", "")))
            for token in unique_tokens:
                doc_freq[token] += 1
    idf = {
        token: math.log((1 + total_passages) / (1 + count)) + 1.0
        for token, count in doc_freq.items()
    }
    return idf, total_passages


def parse_question_intent(question: str) -> Tuple[set, set]:
    lowered = question.lower()
    positive = set(tokenize(question))
    negative = set()

    contrast_patterns = [
        r"rather than ([a-zA-Z0-9 \-]+)",
        r"instead of ([a-zA-Z0-9 \-]+)",
        r"not just ([a-zA-Z0-9 \-]+)",
        r"not only ([a-zA-Z0-9 \-]+)",
    ]
    for pattern in contrast_patterns:
        match = re.search(pattern, lowered)
        if match:
            negative.update(tokenize(match.group(1)))

    # If the user asks "which papers", don't let "paper" drive relevance.
    positive.discard("paper")
    negative.discard("paper")
    positive -= negative
    return positive, negative


def score_passage(query_tokens: Sequence[str], passage_text: str, field: str, idf: Dict[str, float]) -> Tuple[float, List[str]]:
    passage_tokens = tokenize(passage_text)
    if not passage_tokens:
        return 0.0, []
    counts = Counter(passage_tokens)
    matched = []
    score = 0.0
    for token in query_tokens:
        count = counts.get(token, 0)
        if not count:
            continue
        matched.append(token)
        score += (1 + math.log(count)) * idf.get(token, 1.0)
    if not score:
        return 0.0, []
    boost = FIELD_WEIGHTS.get(field, 1.0)
    return round(score * boost, 4), matched


def classify_match(total_score: float, top_passage_score: float, support_count: int) -> str:
    if total_score >= 14 or (top_passage_score >= 8 and support_count >= 2):
        return "direct"
    if total_score >= 8:
        return "partial"
    return "background"


def retrieve(question: str, top_k: int = 5, mode: str = "all") -> dict:
    papers = load_records_with_passages()
    idf, _ = build_passage_stats(papers)
    query_tokens = tokenize(question)
    positive_tokens, negative_tokens = parse_question_intent(question)
    retrieval_tokens = sorted(positive_tokens) if positive_tokens else query_tokens
    normalized_mode = normalize_mode(mode)
    results = []

    for paper in papers:
        scored_passages = []
        field_hits = set()
        aggregate_score = 0.0
        paper_text = "\n".join(
            [
                paper.get("title", ""),
                paper.get("layer", "") or "",
                paper.get("solution", "") or "",
            ]
            + [passage.get("text", "") for passage in paper.get("passages", [])]
        )
        paper_tokens = set(tokenize(paper_text))

        for passage in paper.get("passages", []):
            score, matched = score_passage(retrieval_tokens, passage.get("text", ""), passage.get("field", ""), idf)
            if not score:
                continue
            field_hits.add(passage.get("field", ""))
            aggregate_score += score
            scored_passages.append(
                {
                    "field": passage.get("field", ""),
                    "score": score,
                    "matched_terms": matched,
                    "text": passage.get("text", ""),
                }
            )

        layer_tokens = tokenize(paper.get("layer", "") or "")
        if retrieval_tokens and any(token in layer_tokens for token in retrieval_tokens):
            aggregate_score += 2.0
        if retrieval_tokens and paper.get("title"):
            title_tokens = tokenize(paper["title"])
            title_overlap = len(set(retrieval_tokens) & set(title_tokens))
            aggregate_score += title_overlap * 1.8

        positive_hits = len(positive_tokens & paper_tokens)
        negative_hits = len(negative_tokens & paper_tokens)
        aggregate_score += positive_hits * 2.2
        if negative_hits and not positive_hits:
            aggregate_score -= negative_hits * 2.5
        elif negative_hits and positive_hits:
            aggregate_score -= negative_hits * 0.8

        focus_scores = paper.get("focus_scores", {}) or {}
        mode_score = focus_scores.get(normalized_mode, 0) if normalized_mode != "all" else 0
        if normalized_mode != "all":
            aggregate_score += mode_score * 3.0
            primary_focus = paper.get("primary_focus")
            if primary_focus == normalized_mode:
                aggregate_score += 4.0
            elif normalized_mode not in paper.get("secondary_focuses", []):
                aggregate_score -= 4.5

        if not scored_passages and aggregate_score <= 0:
            continue

        scored_passages.sort(key=lambda item: item["score"], reverse=True)
        top_passage_score = scored_passages[0]["score"] if scored_passages else 0.0
        stance = classify_match(aggregate_score, top_passage_score, len(field_hits))

        results.append(
            {
                "title": paper["title"],
                "ordinal": paper["ordinal"],
                "url": paper.get("url"),
                "layer": paper.get("layer"),
                "solution": paper.get("solution"),
                "score": round(aggregate_score, 4),
                "match_type": stance,
                "support_count": len(field_hits),
                "positive_hits": positive_hits,
                "negative_hits": negative_hits,
                "focus_scores": focus_scores,
                "primary_focus": paper.get("primary_focus"),
                "secondary_focuses": paper.get("secondary_focuses", []),
                "top_passages": scored_passages[:3],
            }
        )

    results.sort(
        key=lambda item: (
            -(item["focus_scores"].get(normalized_mode, 0) if normalized_mode != "all" else 0),
            -item["positive_hits"],
            item["negative_hits"],
            -item["score"],
            -item["support_count"],
            item["ordinal"],
        )
    )
    return {
        "question": question,
        "mode": normalized_mode,
        "query_tokens": retrieval_tokens,
        "positive_tokens": sorted(positive_tokens),
        "negative_tokens": sorted(negative_tokens),
        "results": results[:top_k],
    }


def summarize_state_of_art(mode: str = "all", top_k: int = 10) -> dict:
    papers = load_records_with_passages()
    normalized_mode = normalize_mode(mode)
    ranked = []
    for paper in papers:
        focus_scores = paper.get("focus_scores", {}) or {}
        if normalized_mode == "all":
            score = sum(focus_scores.values())
        else:
            score = focus_scores.get(normalized_mode, 0) * 10
            if paper.get("primary_focus") == normalized_mode:
                score += 5
        ranked.append(
            {
                "title": paper["title"],
                "ordinal": paper["ordinal"],
                "url": paper.get("url"),
                "layer": paper.get("layer"),
                "primary_focus": paper.get("primary_focus"),
                "secondary_focuses": paper.get("secondary_focuses", []),
                "focus_scores": focus_scores,
                "score": score,
            }
        )
    ranked.sort(
        key=lambda item: (
            -(item["focus_scores"].get(normalized_mode, 0) if normalized_mode != "all" else sum(item["focus_scores"].values())),
            -item["score"],
            item["ordinal"],
        )
    )
    return {"mode": normalized_mode, "results": ranked[:top_k]}


def format_text_report(result: dict) -> str:
    lines = [f"Question: {result['question']}", f"Mode: {result.get('mode', 'all')}", ""]
    for idx, item in enumerate(result["results"], start=1):
        lines.append(
            f"{idx}. {item['title']} | {item['match_type']} | score={item['score']} | focus={item.get('primary_focus') or 'n/a'} | layer={item.get('layer') or 'n/a'}"
        )
        if item.get("url"):
            lines.append(f"   {item['url']}")
        if item.get("focus_scores"):
            lines.append(f"   focus_scores: {item['focus_scores']}")
        for passage in item["top_passages"]:
            excerpt = passage["text"].replace("\n", " ")
            if len(excerpt) > 260:
                excerpt = excerpt[:257] + "..."
            matched = ", ".join(sorted(set(passage["matched_terms"])))
            lines.append(f"   - {passage['field']} [{passage['score']}]: {excerpt}")
            if matched:
                lines.append(f"     matched: {matched}")
    return "\n".join(lines)


def format_sota_report(result: dict) -> str:
    lines = [f"State of the art mode: {result['mode']}", ""]
    for idx, item in enumerate(result["results"], start=1):
        lines.append(
            f"{idx}. {item['title']} | focus={item.get('primary_focus') or 'n/a'} | layer={item.get('layer') or 'n/a'} | scores={item['focus_scores']}"
        )
        if item.get("url"):
            lines.append(f"   {item['url']}")
    return "\n".join(lines)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Find which collected papers answer a specific question.")
    parser.add_argument("question", nargs="?", help="The question to map onto the collected corpus")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--mode", default="all", choices=sorted(MODE_ALIASES.keys()))
    parser.add_argument("--sota", action="store_true", help="List the ranked state of the art view for a focus mode")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--rebuild-index", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    if args.rebuild_index or not DEFAULT_INDEX.exists():
        build_index(DEFAULT_REPORT, DEFAULT_INDEX)
    if args.sota:
        result = summarize_state_of_art(mode=args.mode, top_k=args.top_k)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_sota_report(result))
    else:
        if not args.question:
            raise SystemExit("question is required unless --sota is used")
        result = retrieve(args.question, top_k=args.top_k, mode=args.mode)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_text_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
