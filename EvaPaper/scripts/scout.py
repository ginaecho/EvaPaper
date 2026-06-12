#!/usr/bin/env python3
"""
Agent Governance Research Scout
Only reports and pushes to git when NEW items are found.
"""

import os
import sys
import re
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

from paper_graph import discover_from_query
from governance_dashboard import write_dashboard
from workspace_config import DEFAULT_WORKSPACE

WORKSPACE = DEFAULT_WORKSPACE
SCOUT_LOG = WORKSPACE.scout_log
REPORT_MD = WORKSPACE.report_md
REPO_DIR = WORKSPACE.root

def read_known_items(scout_log: Path = SCOUT_LOG):
    """Read known papers and products from the scout log."""
    known = {"papers": [], "products": []}
    if not scout_log.exists():
        return known
    
    with scout_log.open("r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract known papers
    papers_section = re.search(r"## Known Papers.*?(?=##|$)", content, re.DOTALL)
    if papers_section:
        for line in papers_section.group(0).split("\n"):
            if line.startswith("- ") and "arXiv" in line:
                arxiv_id = re.search(r"arXiv:(\d+\.\d+)", line)
                if arxiv_id:
                    known["papers"].append(arxiv_id.group(1))
    
    # Extract known products
    products_section = re.search(r"## Known Products.*?(?=##|$)", content, re.DOTALL)
    if products_section:
        for line in products_section.group(0).split("\n"):
            if line.startswith("- "):
                known["products"].append(line[2:].strip().split(" —")[0])
    
    return known

def update_scout_log(new_items, scout_log: Path = SCOUT_LOG):
    """Update the scout log with new findings."""
    with scout_log.open("r", encoding="utf-8") as f:
        content = f.read()
    
    # Add new items to the appropriate section
    for item in new_items:
        if item["type"] == "paper":
            # Add to papers section
            papers_section_end = re.search(r"(## Known Papers.*?)(?=## |$)", content, re.DOTALL)
            if papers_section_end:
                insert_pos = papers_section_end.end()
                new_line = f"- {item['title']} (arXiv:{item['arxiv_id']}) — {item['authors']}, {item['date']}\n"
                content = content[:insert_pos] + new_line + content[insert_pos:]
    
    # Update last check section
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(
        r"## Last Check.*?(?=## |$)",
        f"## Last Check\n- Date: {today}\n- Status: New findings detected\n- Findings: {len(new_items)} new item(s)\n",
        content,
        flags=re.DOTALL
    )
    
    with scout_log.open("w", encoding="utf-8") as f:
        f.write(content)

def update_report(new_items, report_md: Path = REPORT_MD):
    """Update the markdown report with new findings."""
    with report_md.open("r", encoding="utf-8") as f:
        content = f.read()
    
    # Add new items to the papers section
    for item in new_items:
        if item["type"] == "paper":
            paper_entry = f"""
### {len(re.findall(r'### \d+\.', content)) + 1}. {item['title']}

- **arXiv ID:** {item['arxiv_id']}
- **URL:** https://arxiv.org/abs/{item['arxiv_id']}
- **PDF:** https://arxiv.org/pdf/{item['arxiv_id']}
- **Authors:** {item['authors']}
- **Date:** {item['date']}

**Abstract:**
> {item['abstract']}

**Why I recommend this paper:**
{item['recommendation']}

**Relevance to our topic:**
{item['relevance']}

**Which layer:** **{item['layer']}**

**Is it a solution we're looking into?** {item['solution']}

**Recommendation reason:** {item['reason']}

---
"""
            # Find the end of papers section and insert
            papers_end = content.find("## The Three-Layer Stack in Detail")
            if papers_end > 0:
                content = content[:papers_end] + paper_entry + "\n" + content[papers_end:]
    
    with report_md.open("w", encoding="utf-8") as f:
        f.write(content)

def git_commit_and_push(repo_dir: Path = REPO_DIR, scout_log: Path = SCOUT_LOG, report_md: Path = REPORT_MD, push: bool = False):
    """Commit changes and push to git."""
    os.chdir(repo_dir)
    
    # Configure git if not already done
    subprocess.run(["git", "config", "user.email", "evapaper@agent.ai"], capture_output=True)
    subprocess.run(["git", "config", "user.name", "EvaPaper"], capture_output=True)
    
    # Add files
    subprocess.run(["git", "add", str(scout_log)], capture_output=True)
    subprocess.run(["git", "add", str(report_md)], capture_output=True)
    subprocess.run(["git", "add", str(DEFAULT_WORKSPACE.dashboard_data)], capture_output=True)
    subprocess.run(["git", "add", str(DEFAULT_WORKSPACE.dashboard_html)], capture_output=True)
    subprocess.run(["git", "add", str(DEFAULT_WORKSPACE.research_opportunities)], capture_output=True)
    
    # Commit
    today = datetime.now().strftime("%Y-%m-%d")
    result = subprocess.run(
        ["git", "commit", "-m", f"Scout update: New findings on {today}"],
        capture_output=True,
        text=True
    )
    
    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        return False
    
    if push:
        subprocess.run(["git", "push"], capture_output=True)
    return True

def main():
    """Main scout routine for a generic agent team."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--discover",
        help="Run graph-backed discovery for a topic query instead of the no-op scout placeholder",
    )
    parser.add_argument("--seed-limit", type=int, default=5)
    parser.add_argument("--neighbors-per-seed", type=int, default=10)
    parser.add_argument("--from-year", type=int, default=None)
    parser.add_argument("--scout-log", type=Path, default=SCOUT_LOG)
    parser.add_argument("--report-md", type=Path, default=REPORT_MD)
    parser.add_argument("--repo-dir", type=Path, default=REPO_DIR)
    parser.add_argument("--commit", action="store_true", help="Commit local scout/report updates")
    parser.add_argument("--push", action="store_true", help="Push after commit")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.discover:
        result = discover_from_query(
            query=args.discover,
            seed_limit=args.seed_limit,
            neighbors_per_seed=args.neighbors_per_seed,
            from_year=args.from_year,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"📡 Graph discovery for: {args.discover}")
            print(f"🌱 Seed papers: {len(result['seeds'])}")
            print(f"🕸️ Candidate papers: {len(result['candidates'])}")
            for candidate in result["candidates"][:10]:
                print(
                    f"- {candidate['title']} ({candidate.get('year')}) "
                    f"[score={candidate['score']}, citations={candidate['citation_count']}]"
                )
                if candidate.get("url"):
                    print(f"  {candidate['url']}")
        return 0

    print("📡 Agent-team scout starting...")
    
    # Read known items
    known = read_known_items(args.scout_log)
    print(f"📚 Known papers: {len(known['papers'])}")
    print(f"🔧 Known products: {len(known['products'])}")
    
    # Team-owned scouting hook:
    # 1. scout agent collects candidates via public graph APIs
    # 2. analyst agents classify and justify candidates
    # 3. librarian agent converts approved candidates into new_items entries
    new_items = []
    
    if not new_items:
        print("✅ No new findings. Scout finishing silently.")
        return 0
    
    print(f"🎉 Found {len(new_items)} new item(s)!")
    
    # Update scout log
    update_scout_log(new_items, args.scout_log)
    print("📝 Scout log updated")
    
    # Update report
    update_report(new_items, args.report_md)
    print("📄 Report updated")

    write_dashboard(args.report_md, args.scout_log)
    print("📊 Research dashboard updated")
    
    if args.commit:
        if git_commit_and_push(args.repo_dir, args.scout_log, args.report_md, push=args.push):
            print("🚀 Scout changes committed" + (" and pushed" if args.push else ""))
    
    # Report findings
    print("\n" + "="*60)
    print("📢 NEW FINDINGS REPORT")
    print("="*60)
    for item in new_items:
        print(f"\n🔍 {item['title']}")
        print(f"   URL: https://arxiv.org/abs/{item['arxiv_id']}")
        print(f"   Layer: {item['layer']}")
        print(f"   Why: {item['reason']}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
