#!/usr/bin/env python3
"""
Agent Governance Research Scout
Only reports and pushes to git when NEW items are found.
"""

import os
import sys
import re
import json
import subprocess
from datetime import datetime

SCOUT_LOG = "/root/.openclaw/workspace/memory/agent_governance_scout_log.md"
REPORT_MD = "/root/.openclaw/workspace/AI_Agent_Governance_Three_Layer_Stack_and_Papers.md"
REPO_DIR = "/root/.openclaw/workspace"

def read_known_items():
    """Read known papers and products from the scout log."""
    known = {"papers": [], "products": []}
    if not os.path.exists(SCOUT_LOG):
        return known
    
    with open(SCOUT_LOG, "r") as f:
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

def update_scout_log(new_items):
    """Update the scout log with new findings."""
    with open(SCOUT_LOG, "r") as f:
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
    
    with open(SCOUT_LOG, "w") as f:
        f.write(content)

def update_report(new_items):
    """Update the markdown report with new findings."""
    with open(REPORT_MD, "r") as f:
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
    
    with open(REPORT_MD, "w") as f:
        f.write(content)

def git_commit_and_push():
    """Commit changes and push to git."""
    os.chdir(REPO_DIR)
    
    # Configure git if not already done
    subprocess.run(["git", "config", "user.email", "evapaper@agent.ai"], capture_output=True)
    subprocess.run(["git", "config", "user.name", "EvaPaper"], capture_output=True)
    
    # Add files
    subprocess.run(["git", "add", SCOUT_LOG], capture_output=True)
    subprocess.run(["git", "add", REPORT_MD], capture_output=True)
    
    # Commit
    today = datetime.now().strftime("%Y-%m-%d")
    result = subprocess.run(
        ["git", "commit", "-m", f"Scout update: New findings on {today}"],
        capture_output=True,
        text=True
    )
    
    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        return False
    
    # Push
    subprocess.run(["git", "push", "origin", "master"], capture_output=True)
    return True

def main():
    """Main scout routine."""
    print("📡 Agent Governance Scout starting...")
    
    # Read known items
    known = read_known_items()
    print(f"📚 Known papers: {len(known['papers'])}")
    print(f"🔧 Known products: {len(known['products'])}")
    
    # Search for new items (this would be done by the agent using kimi_search)
    # For now, this is a placeholder - the actual search happens in the agent context
    new_items = []
    
    if not new_items:
        print("✅ No new findings. Scout finishing silently.")
        return 0
    
    print(f"🎉 Found {len(new_items)} new item(s)!")
    
    # Update scout log
    update_scout_log(new_items)
    print("📝 Scout log updated")
    
    # Update report
    update_report(new_items)
    print("📄 Report updated")
    
    # Git commit and push
    if git_commit_and_push():
        print("🚀 Changes pushed to GitHub")
    
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
