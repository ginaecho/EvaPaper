from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "AI_Agent_Governance_Three_Layer_Stack_and_Papers.md"

RUN_PATTERN = re.compile(
    r"### Run (?P<ts>[^\n]+)\n"
    r"(?:- .*\n)*?"
    r"- \*\*Mode:\*\* (?P<mode>[^\n]+)\n"
    r"(?:- .*\n)*?"
    r"- \*\*Input tokens:\*\* (?P<input>\d+)\n"
    r"- \*\*Output tokens:\*\* (?P<output>\d+)\n"
    r"- \*\*Total tokens:\*\* (?P<total>\d+)\n"
    r"- \*\*Estimated cost \(USD\):\*\* (?P<cost>[0-9.]+)",
    re.MULTILINE,
)


@dataclass
class RunCost:
    timestamp: datetime
    mode: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost_usd: float


def parse_timestamp(value: str) -> datetime:
    return datetime.strptime(value.strip(), "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)


def parse_runs(report_path: Path) -> list[RunCost]:
    text = report_path.read_text(encoding="utf-8")
    runs: list[RunCost] = []
    for match in RUN_PATTERN.finditer(text):
        runs.append(
            RunCost(
                timestamp=parse_timestamp(match.group("ts")),
                mode=match.group("mode").strip(),
                input_tokens=int(match.group("input")),
                output_tokens=int(match.group("output")),
                total_tokens=int(match.group("total")),
                cost_usd=float(match.group("cost")),
            )
        )
    return runs


def summarize(runs: list[RunCost], day: str) -> str:
    day_runs = [run for run in runs if run.timestamp.strftime("%Y-%m-%d") == day]
    total_input = sum(run.input_tokens for run in day_runs)
    total_output = sum(run.output_tokens for run in day_runs)
    total_tokens = sum(run.total_tokens for run in day_runs)
    total_cost = sum(run.cost_usd for run in day_runs)

    lines = [
        f"Date: {day}",
        f"Runs: {len(day_runs)}",
        f"Input tokens: {total_input}",
        f"Output tokens: {total_output}",
        f"Total tokens: {total_tokens}",
        f"Total cost (USD): {total_cost:.6f}",
    ]

    if day_runs:
        lines.append("")
        lines.append("Runs:")
        for run in day_runs:
            lines.append(
                f"- {run.timestamp.strftime('%H:%M:%S UTC')} | mode={run.mode} | "
                f"input={run.input_tokens} | output={run.output_tokens} | "
                f"total={run.total_tokens} | cost=${run.cost_usd:.6f}"
            )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize daily token/cost totals from workflow run logs.")
    parser.add_argument("--date", default=None, help="UTC date in YYYY-MM-DD format. Defaults to today (UTC).")
    parser.add_argument("--report", default=str(REPORT_PATH), help="Markdown report path to parse.")
    args = parser.parse_args()

    day = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    runs = parse_runs(Path(args.report))
    print(summarize(runs, day))


if __name__ == "__main__":
    main()
