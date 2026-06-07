#!/usr/bin/env python3
"""
Shared workspace configuration for generic agent-team tooling.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
MEMORY_DIR = ROOT / "memory"


@dataclass(frozen=True)
class WorkspaceConfig:
    root: Path = ROOT
    report_md: Path = ROOT / "AI_Agent_Governance_Three_Layer_Stack_and_Papers.md"
    report_docx: Path = ROOT / "AI_Agent_Governance_Three_Layer_Stack_and_Papers.docx"
    report_pptx: Path = ROOT / "AI_Agent_Governance_Three_Layer_Stack_and_Papers.pptx"
    scout_log: Path = MEMORY_DIR / "agent_governance_scout_log.md"
    corpus_index: Path = DATA_DIR / "paper_corpus.json"
    team_dir: Path = DATA_DIR / "agent_team"


DEFAULT_WORKSPACE = WorkspaceConfig()
