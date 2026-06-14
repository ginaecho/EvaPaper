#!/usr/bin/env python3
"""Patch governance-dashboard.json with June 14 scout findings, then regenerate HTML."""

import json
import re
from pathlib import Path

# ── paths ──────────────────────────────────────────────────────────
JSON_PATH = Path("data/governance_dashboard.json")
HTML_PATH = Path("governance-dashboard.html")

# ── data ───────────────────────────────────────────────────────────
data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

# The 8 June 14 findings (some already in dashboard from June 12 run)
# We add all 8 as a new scout run; the 4 arXiv papers are already in the graph
# The 4 new product/framework items need new nodes.

JUNE_14_ITEMS = [
    {"id": "arxiv:2604.11174", "title": "EmbodiedGovBench", "topic": "evaluation", "layers": [2], "new": False},
    {"id": "arxiv:2602.12430", "title": "Agent Skills for Large Language Models", "topic": "policy", "layers": [0], "new": False},
    {"id": "owasp:mcp-guide", "title": "OWASP Practical Guide for Secure MCP Server Development", "topic": "supply_chain", "layers": [1], "new": True},
    {"id": "mitre:atlas-agentic", "title": "MITRE ATLAS agentic AI update", "topic": "policy", "layers": [1, 2], "new": True},
    {"id": "nist:ir-8596", "title": "NIST IR 8596 — Cybersecurity Framework Profile for AI", "topic": "policy", "layers": [1, 3], "new": True},
    {"id": "ieee:reprobe-audit", "title": "reprobe-audit — IEEE Big Data 2026 benchmark disclosure schema", "topic": "evaluation", "layers": [2], "new": True},
    {"id": "github:agent-security-harness", "title": "Agent Security Harness — 474-test security scanner", "topic": "evaluation", "layers": [1, 2], "new": True},
    {"id": "wsp:draft", "title": "Web Skills Protocol (WSP) — March 2026 draft", "topic": "specification", "layers": [0], "new": True},
]

# Topic colors map
TOPIC_COLORS = {
    "specification": "#e4572e",
    "supply_chain": "#963484",
    "identity": "#4267ac",
    "coordination": "#5b8e3e",
    "evaluation": "#f3a712",
    "runtime": "#1d6f75",
    "policy": "#636363",
}

TOPIC_LABELS = {
    "specification": "Specification & validation",
    "supply_chain": "Skill & tool security",
    "identity": "Identity & provenance",
    "coordination": "Coordination & composition",
    "evaluation": "Evaluation & benchmarks",
    "runtime": "Runtime enforcement",
    "policy": "Policy & governance landscape",
}

# ── 1. Add new nodes to association graph ─────────────────────────
existing_ids = {n["id"] for n in data["association_graph"]["nodes"]}
new_nodes = []
for item in JUNE_14_ITEMS:
    if item["id"] in existing_ids:
        continue
    node = {
        "id": item["id"],
        "title": item["title"],
        "url": None,
        "topic": item["topic"],
        "topic_label": TOPIC_LABELS[item["topic"]],
        "color": TOPIC_COLORS[item["topic"]],
        "layers": item["layers"],
        "discovered": "2026-06-14",
        "degree": 1,
    }
    new_nodes.append(node)
    data["association_graph"]["nodes"].append(node)

# ── 2. Add minimal edges for new nodes (connect to same-topic nodes) ──
for new_node in new_nodes:
    for existing in data["association_graph"]["nodes"]:
        if existing["id"] == new_node["id"]:
            continue
        if existing["topic"] == new_node["topic"]:
            shared_layers = set(existing.get("layers", [])) & set(new_node.get("layers", []))
            weight = 2.0 + len(shared_layers) * 0.5
            edge = {
                "source": new_node["id"],
                "target": existing["id"],
                "kind": "conceptual",
                "weight": round(weight, 3),
                "reason": f"same topic; shared L{','.join(str(l) for l in shared_layers)}" if shared_layers else "same topic",
                "shared_terms": [],
            }
            data["association_graph"]["edges"].append(edge)
            break  # Just one edge per new node to keep it simple

# ── 3. Update topic mix ──────────────────────────────────────────
# Count all topics from nodes
topic_counts = {}
for node in data["association_graph"]["nodes"]:
    t = node["topic"]
    topic_counts[t] = topic_counts.get(t, 0) + 1

total_nodes = len(data["association_graph"]["nodes"])
for tm in data["topic_mix"]:
    tm["count"] = topic_counts.get(tm["id"], 0)
    tm["ratio"] = tm["count"] / total_nodes if total_nodes > 0 else 0

# ── 4. Update layer mix ──────────────────────────────────────────
layer_counts = {0: 0, 1: 0, 2: 0, 3: 0}
for node in data["association_graph"]["nodes"]:
    for l in node.get("layers", []):
        layer_counts[l] = layer_counts.get(l, 0) + 1

for lm in data["layer_mix"]:
    lm["count"] = layer_counts.get(lm["layer"], 0)

# ── 5. Add new scout run ─────────────────────────────────────────
# Count topics for June 14
june14_topics = {}
for item in JUNE_14_ITEMS:
    t = item["topic"]
    june14_topics[t] = june14_topics.get(t, 0) + 1

# Cumulative topics after June 14
cumulative_topics = {}
for tm in data["topic_mix"]:
    cumulative_topics[tm["id"]] = tm["count"]

new_run = {
    "date": "2026-06-14",
    "new_papers": 8,
    "cumulative": total_nodes,
    "leading_topic": "Policy & governance landscape",
    "topics": {t: june14_topics.get(t, 0) for t in ["specification", "supply_chain", "identity", "coordination", "evaluation", "runtime", "policy"]},
    "cumulative_topics": cumulative_topics,
}
data["runs"].append(new_run)

# ── 6. Update trending topics ────────────────────────────────────
# Recalculate from last 2 runs (June 12 + June 14)
recent_counts = {}
for run in data["runs"][-2:]:
    for t, c in run.get("topics", {}).items():
        recent_counts[t] = recent_counts.get(t, 0) + c

trending = []
for t, recent in sorted(recent_counts.items(), key=lambda x: -x[1]):
    total = cumulative_topics.get(t, 0)
    if total > 0:
        trending.append({
            "id": t,
            "label": TOPIC_LABELS[t],
            "recent_count": recent,
            "total_count": total,
            "color": TOPIC_COLORS[t],
        })

data["trending_topics"] = trending[:3]

# ── 7. Update counts ─────────────────────────────────────────────
data["paper_count"] = total_nodes
data["scout_run_count"] = len(data["runs"])
data["generated_from_latest_scout"] = "2026-06-14"

# ── 8. Add wiki pages for new nodes ──────────────────────────────
wiki = data["knowledge_wiki"]

# Helper to find or create a wiki page
def find_page(page_id):
    for p in wiki["pages"]:
        if p.get("id") == page_id:
            return p
    return None

def add_page(page_id, page_type, title, content, links=None):
    existing = find_page(page_id)
    if existing:
        existing["content"] = content
        if links:
            existing["links"] = links
    else:
        wiki["pages"].append({
            "id": page_id,
            "type": page_type,
            "title": title,
            "content": content,
            "links": links or [],
        })

for node in new_nodes:
    add_page(
        node["id"],
        "paper",
        node["title"],
        f"{node['title']}.\n\nTopic: {node['topic_label']}.\nLayers: {', '.join(f'L{l}' for l in node['layers'])}.\nDiscovered: 2026-06-14.",
        [],
    )

# Update topic and layer pages
for t in set(n["topic"] for n in new_nodes):
    tp = f"topic:{t}"
    topic_nodes = [n["id"] for n in data["association_graph"]["nodes"] if n["topic"] == t]
    add_page(
        tp,
        "topic",
        TOPIC_LABELS[t],
        f"{topic_counts.get(t, 0)} papers on {TOPIC_LABELS[t]}.",
        topic_nodes,
    )

for l in set(l for n in new_nodes for l in n.get("layers", [])):
    lp = f"layer:{l}"
    layer_nodes = [n["id"] for n in data["association_graph"]["nodes"] if l in n.get("layers", [])]
    add_page(
        lp,
        "layer",
        f"Layer {l}",
        f"{layer_counts.get(l, 0)} papers mapped to Layer {l}.",
        layer_nodes,
    )

# Update overview page
overview = find_page("overview")
if overview:
    overview["subtitle"] = f"{total_nodes} papers compiled into a living research wiki"
    overview["links"] = [
        "topic:specification", "topic:supply_chain", "topic:identity", "topic:coordination",
        "topic:evaluation", "topic:runtime", "topic:policy",
        "layer:0", "layer:1", "layer:2", "layer:3",
    ]

# ── 9. Write updated JSON ────────────────────────────────────────
JSON_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated JSON: {total_nodes} papers, {len(data['runs'])} runs, {len(data['association_graph']['edges'])} edges")

# ── 10. Patch HTML ───────────────────────────────────────────────
html = HTML_PATH.read_text(encoding="utf-8")

# Replace the embedded JSON
old_json_match = re.search(r'<script id="dashboard-data" type="application/json">(.*?)</script>', html, re.DOTALL)
if old_json_match:
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    html = html.replace(old_json_match.group(0), f'<script id="dashboard-data" type="application/json">\n{new_json_str}\n</script>')

# Update header stats
html = re.sub(r'class="stat-value">\d+</div>\s*<div class="stat-label">papers in corpus', f'class="stat-value">{total_nodes}</div>\n            <div class="stat-label">papers in corpus', html)
html = re.sub(r'class="stat-value">\d+</div>\s*<div class="stat-label">scout runs', f'class="stat-value">{len(data["runs"])}</div>\n            <div class="stat-label">scout runs', html)

HTML_PATH.write_text(html, encoding="utf-8")
print(f"Updated HTML: {HTML_PATH}")
