#!/usr/bin/env python3
"""Generate the EvaPaper research dashboard from the report and scout log."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

from paper_corpus import PaperRecord, parse_report, parse_scout_log
from workspace_config import DEFAULT_WORKSPACE


TOPICS = {
    "specification": {
        "label": "Specification & validation",
        "color": "#e4572e",
        "keywords": (
            "skill.md", "specification", "schema", "contract", "pseudocode",
            "static analysis", "representation", "compiler", "well-defined",
        ),
    },
    "runtime": {
        "label": "Runtime enforcement",
        "color": "#1d6f75",
        "keywords": (
            "runtime", "sandbox", "admission control", "policy enforcement",
            "monitoring", "audit", "intervention", "capability", "authorization",
        ),
    },
    "evaluation": {
        "label": "Evaluation & benchmarks",
        "color": "#f3a712",
        "keywords": (
            "benchmark", "evaluation", "red team", "testing", "assay",
            "behavioral safety", "trustworthiness", "regression",
        ),
    },
    "supply_chain": {
        "label": "Skill & tool security",
        "color": "#963484",
        "keywords": (
            "skill supply chain", "third-party", "tool poisoning", "mcp",
            "marketplace", "skillattack", "skillguard", "dependency",
        ),
    },
    "identity": {
        "label": "Identity & provenance",
        "color": "#4267ac",
        "keywords": (
            "identity", "provenance", "delegation", "attribution", "attestation",
            "accountability", "machine identity",
        ),
    },
    "coordination": {
        "label": "Coordination & composition",
        "color": "#5b8e3e",
        "keywords": (
            "multi-agent", "coordination", "composition", "compositional",
            "message sequence", "orchestration", "agent economy",
        ),
    },
    "policy": {
        "label": "Policy & governance landscape",
        "color": "#636363",
        "keywords": (
            "governance", "taxonomy", "survey", "framework", "constitutional",
            "alignment", "owasp", "nist", "continuous assurance",
        ),
    },
}

TOPIC_PRECEDENCE = (
    "specification",
    "supply_chain",
    "identity",
    "coordination",
    "evaluation",
    "runtime",
    "policy",
)

TOPIC_OVERRIDES = {
    "BeSafe-Bench (BSB)": "evaluation",
    "ST-WebAgentBench": "evaluation",
    "Skilldex": "specification",
    "GovernSpec / Contractual Skills": "specification",
    "Layered Governance Architecture (LGA)": "runtime",
    "TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling": "runtime",
}


@dataclass(frozen=True)
class DashboardPaper:
    title: str
    url: str | None
    discovered: date
    topic: str
    layers: tuple[int, ...]


def _normalize_title(title: str) -> str:
    title = re.sub(r"\s*\(arXiv:[^)]+\)", "", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def _parse_found_date(token: str, year: int = 2026) -> date:
    match = re.match(r"(?P<month>\d{2})(?P<day>\d{2})", token)
    if not match:
        raise ValueError(f"Unsupported discovery date: {token}")
    return date(year, int(match.group("month")), int(match.group("day")))


def _paper_id(text: str) -> str | None:
    arxiv = re.search(r"(?:arxiv\.org/(?:abs|pdf)/|arXiv:|arXiv ID:\s*)(\d{4}\.\d{4,5})", text, re.IGNORECASE)
    if arxiv:
        return f"arxiv:{arxiv.group(1)}"
    preprint = re.search(r"(10\.20944/preprints\d{6}\.\d+\.v\d+)", text, re.IGNORECASE)
    if preprint:
        return f"doi:{preprint.group(1).lower()}"
    return None


def _extract_discovery_dates(log_path: Path, report_path: Path) -> tuple[dict[str, date], dict[str, date]]:
    title_dates: dict[str, date] = {}
    id_dates: dict[str, date] = {}
    log = log_path.read_text(encoding="utf-8")

    current_found: date | None = None
    for line in log.splitlines():
        heading = re.match(r"### New Papers \(Found: ([^)]+)\)", line)
        if heading:
            current_found = _parse_found_date(heading.group(1))
            continue
        baseline = re.match(r"- (?:\*\*)?(.+?)(?:\*\*)?.*Found:\s*(\d{4})", line)
        if baseline:
            discovered = _parse_found_date(baseline.group(2))
            title_dates[_normalize_title(baseline.group(1))] = discovered
            identifier = _paper_id(line)
            if identifier:
                id_dates[identifier] = discovered
            continue
        numbered = re.match(r"\d+\.\s+\*\*(.+?)\*\*", line)
        if numbered and current_found:
            title_dates[_normalize_title(numbered.group(1))] = current_found
            identifier = _paper_id(line)
            if identifier:
                id_dates[identifier] = current_found

    report = report_path.read_text(encoding="utf-8")
    addendum_pattern = re.compile(
        r"### ([A-Z][a-z]+ \d{1,2}, 2026) scout addendum.*?"
        r"(?=\n### [A-Z][a-z]+ \d{1,2}, 2026 scout addendum|\n\*\*The Three-Layer Stack|\n## Papers & Products)",
        re.DOTALL,
    )
    for section in addendum_pattern.finditer(report):
        discovered = datetime.strptime(section.group(1), "%B %d, %Y").date()
        for title in re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", section.group(0), re.MULTILINE):
            title_dates.setdefault(_normalize_title(title), discovered)
        for identifier_text in re.findall(r"(?:arXiv:?\s*`?|\()(\d{4}\.\d{4,5})", section.group(0), re.IGNORECASE):
            id_dates.setdefault(f"arxiv:{identifier_text}", discovered)
    return title_dates, id_dates


def _record_text(record: PaperRecord) -> str:
    fields = " ".join(record.fields.values())
    return f"{record.title} {record.layer or ''} {fields}".lower()


def classify_topic(record: PaperRecord) -> str:
    if record.title in TOPIC_OVERRIDES:
        return TOPIC_OVERRIDES[record.title]
    text = _record_text(record)
    scores = {
        topic: sum(text.count(keyword) for keyword in config["keywords"])
        for topic, config in TOPICS.items()
    }
    return max(TOPIC_PRECEDENCE, key=lambda topic: (scores[topic], -TOPIC_PRECEDENCE.index(topic)))


def parse_layers(record: PaperRecord) -> tuple[int, ...]:
    text = f"{record.layer or ''} {_record_text(record)}"
    layers = sorted({int(value) for value in re.findall(r"\bLayer\s*([0-3])\b", text, re.IGNORECASE)})
    return tuple(layers)


def collect_papers(report_path: Path, log_path: Path) -> list[DashboardPaper]:
    title_dates, id_dates = _extract_discovery_dates(log_path, report_path)
    report_records = parse_report(report_path)
    log_records = parse_scout_log(log_path, starting_ordinal=len(report_records) + 100)
    records: dict[str, PaperRecord] = {}
    for record in [*log_records, *report_records]:
        searchable = " ".join(
            [record.title, record.url or "", *record.fields.values()]
        )
        identifier = _paper_id(searchable)
        if identifier:
            records[identifier] = record

    fallback = min([*title_dates.values(), *id_dates.values()], default=date(2026, 5, 30))
    papers = []
    for identifier, record in records.items():
        normalized_title = _normalize_title(record.title)
        papers.append(
            DashboardPaper(
                title=record.title,
                url=record.url,
                discovered=id_dates.get(identifier, title_dates.get(normalized_title, fallback)),
                topic=classify_topic(record),
                layers=parse_layers(record),
            )
        )
    return sorted(papers, key=lambda paper: (paper.discovered, paper.title.lower()))


def _topic_payload(counter: Counter[str], total: int) -> list[dict]:
    return [
        {
            "id": topic,
            "label": TOPICS[topic]["label"],
            "color": TOPICS[topic]["color"],
            "count": counter[topic],
            "ratio": counter[topic] / total if total else 0,
        }
        for topic in TOPIC_PRECEDENCE
    ]


def build_dashboard_data(papers: Iterable[DashboardPaper]) -> dict:
    papers = list(papers)
    topic_counts = Counter(paper.topic for paper in papers)
    layer_counts = Counter(layer for paper in papers for layer in paper.layers)
    by_run: dict[date, list[DashboardPaper]] = defaultdict(list)
    for paper in papers:
        by_run[paper.discovered].append(paper)

    cumulative = 0
    runs = []
    previous_counts: Counter[str] = Counter()
    for run_date in sorted(by_run):
        run_papers = by_run[run_date]
        run_counts = Counter(paper.topic for paper in run_papers)
        cumulative += len(run_papers)
        current_counts = previous_counts + run_counts
        leader = max(TOPIC_PRECEDENCE, key=lambda topic: (run_counts[topic], -TOPIC_PRECEDENCE.index(topic)))
        runs.append(
            {
                "date": run_date.isoformat(),
                "new_papers": len(run_papers),
                "cumulative": cumulative,
                "leading_topic": TOPICS[leader]["label"],
                "topics": {topic: run_counts[topic] for topic in TOPIC_PRECEDENCE},
                "cumulative_topics": {topic: current_counts[topic] for topic in TOPIC_PRECEDENCE},
            }
        )
        previous_counts = current_counts

    latest_date = max((paper.discovered for paper in papers), default=date.today())
    recent_cutoff = runs[-3]["date"] if len(runs) >= 3 else (runs[0]["date"] if runs else latest_date.isoformat())
    recent_counts = Counter(
        paper.topic for paper in papers if paper.discovered.isoformat() >= recent_cutoff
    )
    trending = sorted(
        TOPIC_PRECEDENCE,
        key=lambda topic: (recent_counts[topic], topic_counts[topic]),
        reverse=True,
    )[:3]

    return {
        "generated_from_latest_scout": latest_date.isoformat(),
        "paper_count": len(papers),
        "scout_run_count": len(runs),
        "topic_mix": _topic_payload(topic_counts, len(papers)),
        "layer_mix": [
            {
                "layer": layer,
                "label": {
                    0: "Spec",
                    1: "Runtime",
                    2: "Behavior",
                    3: "Ecosystem",
                }[layer],
                "count": layer_counts[layer],
            }
            for layer in range(4)
        ],
        "runs": runs,
        "trending_topics": [
            {
                "id": topic,
                "label": TOPICS[topic]["label"],
                "recent_count": recent_counts[topic],
                "total_count": topic_counts[topic],
                "color": TOPICS[topic]["color"],
            }
            for topic in trending
        ],
        "papers": [
            {
                "title": paper.title,
                "url": paper.url,
                "discovered": paper.discovered.isoformat(),
                "topic": paper.topic,
                "topic_label": TOPICS[paper.topic]["label"],
                "layers": list(paper.layers),
            }
            for paper in papers
        ],
        "methodology": {
            "ratio": "Each paper receives one primary topic so topic ratios sum to 100%.",
            "layers": "Layer counts are multi-label and may exceed the total paper count.",
            "trend": "Trend lines use discovery dates from scout runs, not publication dates.",
        },
    }


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>EvaPaper Research Signal</title>
  <style>
    :root { --ink:#17201f; --paper:#f3efe4; --panel:#fffdf6; --line:#c9c1b1; --muted:#706c63; --accent:#e4572e; }
    * { box-sizing:border-box; }
    body { margin:0; color:var(--ink); background:var(--paper); font-family:"Avenir Next","Gill Sans",sans-serif; }
    body::before { content:""; position:fixed; inset:0; pointer-events:none; opacity:.28; background-image:radial-gradient(#817b70 0.55px,transparent 0.55px); background-size:7px 7px; }
    main { position:relative; width:min(1480px,calc(100% - 32px)); margin:0 auto; padding:36px 0 64px; }
    header { display:grid; grid-template-columns:1.5fr .7fr; gap:24px; align-items:end; border-top:8px solid var(--ink); padding-top:20px; }
    .kicker,.eyebrow { text-transform:uppercase; letter-spacing:.15em; font-size:11px; font-weight:800; }
    h1 { margin:7px 0 4px; max-width:900px; font-family:Georgia,serif; font-size:clamp(42px,7vw,94px); line-height:.88; letter-spacing:-.055em; }
    .subtitle { max-width:720px; color:var(--muted); font-size:16px; }
    .stamp { justify-self:end; border:1px solid var(--ink); padding:14px 18px; min-width:220px; background:var(--panel); }
    .stamp strong { display:block; font:700 27px Georgia,serif; margin-top:5px; }
    .metrics { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; margin:28px 0; background:var(--line); border:1px solid var(--line); }
    .metric { background:var(--panel); padding:18px; min-height:118px; }
    .metric b { display:block; margin-top:18px; font:700 38px Georgia,serif; }
    .grid { display:grid; grid-template-columns:1fr 1.45fr; gap:18px; }
    .panel { background:rgba(255,253,246,.92); border:1px solid var(--line); padding:20px; min-width:0; }
    .panel h2 { margin:4px 0 18px; font:700 25px Georgia,serif; }
    .wide { grid-column:1/-1; }
    .topic-row { display:grid; grid-template-columns:minmax(150px,1fr) 2.2fr 54px; gap:10px; align-items:center; margin:13px 0; }
    .bar { height:13px; background:#ded8ca; overflow:hidden; }
    .bar i { display:block; height:100%; width:var(--w); background:var(--c); }
    .ratio { text-align:right; font-variant-numeric:tabular-nums; font-weight:800; }
    .legend { display:flex; flex-wrap:wrap; gap:8px 16px; margin:4px 0 14px; font-size:12px; }
    .legend span::before { content:""; display:inline-block; width:9px; height:9px; margin-right:6px; background:var(--c); }
    svg { width:100%; height:auto; overflow:visible; }
    .axis { stroke:#bcb4a4; stroke-width:1; }
    .chart-label { fill:#706c63; font-size:11px; }
    .trend-line { fill:none; stroke-width:3; vector-effect:non-scaling-stroke; }
    .run-dot { stroke:var(--panel); stroke-width:2; }
    .layers { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; align-items:end; min-height:250px; }
    .layer { display:flex; flex-direction:column; justify-content:flex-end; min-width:0; }
    .layer-bar { height:var(--h); min-height:8px; background:var(--ink); position:relative; }
    .layer-bar b { position:absolute; top:-28px; font:700 20px Georgia,serif; }
    .layer small { margin-top:8px; color:var(--muted); }
    .signals { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
    .signal { border-top:5px solid var(--c); padding:12px 0; }
    .signal b { display:block; font:700 21px Georgia,serif; }
    .signal strong { font-size:34px; }
    table { width:100%; border-collapse:collapse; font-size:13px; }
    th,td { padding:10px 8px; text-align:left; border-bottom:1px solid #d9d2c4; }
    th { position:sticky; top:0; background:var(--panel); text-transform:uppercase; letter-spacing:.08em; font-size:10px; }
    td a { color:var(--ink); font-weight:700; text-decoration-thickness:1px; text-underline-offset:3px; }
    .pill { display:inline-block; padding:3px 7px; border:1px solid currentColor; font-size:10px; font-weight:800; text-transform:uppercase; }
    .method { color:var(--muted); font-size:12px; margin-top:18px; }
    @media(max-width:850px) {
      header,.grid { grid-template-columns:1fr; }
      .stamp { justify-self:start; }
      .metrics { grid-template-columns:1fr 1fr; }
      .wide { grid-column:auto; }
      .signals { grid-template-columns:1fr; }
      .topic-row { grid-template-columns:1fr 1.4fr 45px; font-size:12px; }
      .table-wrap { overflow-x:auto; }
    }
  </style>
</head>
<body>
<main>
  <header>
    <div><div class="kicker">EvaPaper / Research intelligence</div><h1>Agent governance signal.</h1><p class="subtitle">Topic concentration, layer coverage, and the direction of research discovered across scout runs.</p></div>
    <div class="stamp"><span class="eyebrow">Latest evidence</span><strong id="latest-date"></strong><span id="latest-note"></span></div>
  </header>
  <section class="metrics" id="metrics"></section>
  <section class="grid">
    <article class="panel"><div class="eyebrow">Distribution</div><h2>What the corpus studies</h2><div id="topic-mix"></div></article>
    <article class="panel"><div class="eyebrow">Momentum</div><h2>Cumulative topic growth</h2><div class="legend" id="legend"></div><svg id="trend" viewBox="0 0 820 330" role="img" aria-label="Cumulative paper topics over scout runs"></svg></article>
    <article class="panel"><div class="eyebrow">Coverage</div><h2>Governance layers</h2><div class="layers" id="layers"></div><p class="method">Multi-layer papers count in every applicable layer.</p></article>
    <article class="panel"><div class="eyebrow">Last three scout windows</div><h2>Topics gaining attention</h2><div class="signals" id="signals"></div><p class="method">Momentum is based on discovery dates, not publication dates.</p></article>
    <article class="panel wide"><div class="eyebrow">Evidence ledger</div><h2>Paper inventory</h2><div class="table-wrap"><table><thead><tr><th>Found</th><th>Paper</th><th>Primary topic</th><th>Layers</th></tr></thead><tbody id="papers"></tbody></table></div><p class="method" id="method"></p></article>
  </section>
</main>
<script id="dashboard-data" type="application/json">__DATA__</script>
<script>
const data=JSON.parse(document.getElementById("dashboard-data").textContent);
const pct=n=>`${Math.round(n*100)}%`;
const topicById=Object.fromEntries(data.topic_mix.map(x=>[x.id,x]));
document.getElementById("latest-date").textContent=new Date(`${data.generated_from_latest_scout}T12:00:00`).toLocaleDateString("en",{month:"short",day:"numeric",year:"numeric"});
document.getElementById("latest-note").textContent=`${data.runs.at(-1)?.new_papers||0} papers in latest run`;
const leaders=[...data.topic_mix].sort((a,b)=>b.count-a.count);
document.getElementById("metrics").innerHTML=[
  ["Indexed papers",data.paper_count],
  ["Scout runs",data.scout_run_count],
  ["Largest topic",leaders[0]?.label||"—"],
  ["Corpus share",pct(leaders[0]?.ratio||0)]
].map(([label,value])=>`<div class="metric"><span class="eyebrow">${label}</span><b>${value}</b></div>`).join("");
document.getElementById("topic-mix").innerHTML=data.topic_mix.map(t=>`<div class="topic-row"><span>${t.label}</span><span class="bar"><i style="--w:${pct(t.ratio)};--c:${t.color}"></i></span><span class="ratio">${pct(t.ratio)}</span></div>`).join("");
document.getElementById("legend").innerHTML=data.topic_mix.map(t=>`<span style="--c:${t.color}">${t.label}</span>`).join("");
const svg=document.getElementById("trend"), W=820,H=330,pad={l:42,r:16,t:12,b:40}, runs=data.runs, max=Math.max(1,...runs.flatMap(r=>Object.values(r.cumulative_topics)));
const x=i=>pad.l+(runs.length===1?0:i*(W-pad.l-pad.r)/(runs.length-1)), y=v=>H-pad.b-v*(H-pad.t-pad.b)/max;
let chart=`<line class="axis" x1="${pad.l}" y1="${H-pad.b}" x2="${W-pad.r}" y2="${H-pad.b}"/>`;
for(let i=0;i<=4;i++){const v=Math.round(max*i/4);chart+=`<line class="axis" opacity=".35" x1="${pad.l}" y1="${y(v)}" x2="${W-pad.r}" y2="${y(v)}"/><text class="chart-label" x="4" y="${y(v)+4}">${v}</text>`;}
runs.forEach((r,i)=>{if(i===0||i===runs.length-1||i%2===0)chart+=`<text class="chart-label" text-anchor="middle" x="${x(i)}" y="${H-12}">${r.date.slice(5)}</text>`;});
data.topic_mix.forEach(t=>{const pts=runs.map((r,i)=>`${x(i)},${y(r.cumulative_topics[t.id])}`).join(" ");chart+=`<polyline class="trend-line" stroke="${t.color}" points="${pts}"/>`;});
svg.innerHTML=chart;
const layerMax=Math.max(1,...data.layer_mix.map(x=>x.count));
document.getElementById("layers").innerHTML=data.layer_mix.map(x=>`<div class="layer"><div class="layer-bar" style="--h:${Math.max(8,x.count/layerMax*190)}px"><b>${x.count}</b></div><small>Layer ${x.layer}<br><strong>${x.label}</strong></small></div>`).join("");
document.getElementById("signals").innerHTML=data.trending_topics.map(t=>`<div class="signal" style="--c:${t.color}"><strong>${t.recent_count}</strong><b>${t.label}</b><span>${t.total_count} total</span></div>`).join("");
document.getElementById("papers").innerHTML=[...data.papers].reverse().map(p=>`<tr><td>${p.discovered.slice(5)}</td><td>${p.url?`<a href="${p.url}">${p.title}</a>`:p.title}</td><td><span class="pill" style="color:${topicById[p.topic].color}">${p.topic_label}</span></td><td>${p.layers.length?p.layers.map(x=>`L${x}`).join(" · "):"—"}</td></tr>`).join("");
document.getElementById("method").textContent=`${data.methodology.ratio} ${data.methodology.layers} ${data.methodology.trend}`;
</script>
</body>
</html>
"""


def render_dashboard(data: dict) -> str:
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=True).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__DATA__", payload)


def write_dashboard(
    report_path: Path = DEFAULT_WORKSPACE.report_md,
    log_path: Path = DEFAULT_WORKSPACE.scout_log,
    data_path: Path = DEFAULT_WORKSPACE.dashboard_data,
    html_path: Path = DEFAULT_WORKSPACE.dashboard_html,
) -> dict:
    data = build_dashboard_data(collect_papers(report_path, log_path))
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    html_path.write_text(render_dashboard(data), encoding="utf-8")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DEFAULT_WORKSPACE.report_md)
    parser.add_argument("--scout-log", type=Path, default=DEFAULT_WORKSPACE.scout_log)
    parser.add_argument("--data", type=Path, default=DEFAULT_WORKSPACE.dashboard_data)
    parser.add_argument("--html", type=Path, default=DEFAULT_WORKSPACE.dashboard_html)
    args = parser.parse_args()
    data = write_dashboard(args.report, args.scout_log, args.data, args.html)
    print(
        f"Dashboard updated: {data['paper_count']} papers across "
        f"{data['scout_run_count']} scout runs -> {args.html}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
