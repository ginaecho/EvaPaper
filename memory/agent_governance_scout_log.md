# Agent Governance Research Scout — Tracking Log
# Created: 2026-05-30
# Tracks known papers, products, and benchmarks to identify new findings.

## Known Papers (as of 2026-05-30)
- BeSafe-Bench (arXiv:2603.25747) — Huawei RAMS Lab, 2026-01-30
- ST-WebAgentBench (arXiv:2410.06703) — IBM Research, 2024-10 (ICLR 2026)
- Layered Governance Architecture / LGA (arXiv:2603.07191) — 2026-03-05
- Skilldex (arXiv:2604.16911) — 2026-04-18
- GovernSpec / Contractual Skills (arXiv:2605.22634) — 2026-05-21

## Known Products/Frameworks
- Microsoft Agent Governance Toolkit — MIT License, 2026-04-02
- OWASP Top 10 for Agentic Applications — 2026 edition
- Ruh AI Production Evaluation Guide — 2026-05-24
- Anthropic SKILL.md validator
- Skilldex MCP server / CLI

## Key Search Queries
- BeSafe-Bench agent safety benchmark
- ST-WebAgentBench web agent safety
- agent governance framework Microsoft NVIDIA OWASP 2026
- agent skill markdown specification validation
- GovernSpec contractual skills
- agent behavior evaluation validation framework 2026
- AI agent safety benchmark 2026
- OWASP agentic applications 2026
- OpenClaw agent governance
- agent governance toolkit open source

## Last Check
- Date: 2026-05-30
- Status: Initial baseline established
- Findings: None (baseline creation)

## 2026-05-31 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026
Status: **NEW FINDINGS FOUND**

### New Papers
1. **ClawBench** (arXiv:2604.08523) — UBC/Vector Institute/CMU/etc, 2026-04-09. Real-world web agent benchmark: 153 tasks across 144 live production websites. Layer 2.
2. **MCP-38** (arXiv:2603.18063) — Comprehensive threat taxonomy for Model Context Protocol with 38 threat categories. Mapped to STRIDE, OWASP LLM Top 10, OWASP Agentic Top 10. Layer 1.
3. **MCPThreatHive** (arXiv:2604.13849) — Automated threat intelligence platform for MCP ecosystems. GitHub: VulcanLab/MCPThreatHive. Layer 1.
4. **ADR** (arXiv:2605.17380) — Agentic Detection System for Enterprise Agentic AI Security. Layer 1.
5. **Proteus** (arXiv:2605.11891) — Self-Evolving Red Team for Agent Skill Ecosystems. Layer 2.
6. **SkillAttack** (arXiv:2604.04989) — Automated red teaming of agent skills through attack path refinement. Layer 2.
7. **TRUSTDESC** (arXiv:2604.07536) — Preventing tool poisoning via trusted description generation. Layer 1.

### New Products/Frameworks
1. **OWASP Top 10 for Agentic Skills (AST10)** — New OWASP project 2026 edition. 10 critical risks for agent skills across OpenClaw (SKILL.md), Claude Code, Cursor. Layer 0.
2. **Tencent AI-Infra-Guard** — Full-stack AI red teaming platform with OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan. GitHub: Tencent/AI-Infra-Guard. Layer 1.
3. **IBM Sovereign Core** — GA announced 2026-05-07. Embeds governance policy at infrastructure runtime for regulated, cross-border environments. Layer 1.
4. **DeepTeam by Confident AI** — Framework for testing OWASP ASI risks. trydeepteam.com. Layer 2.
5. **NIST IR 8596** — December 2025 draft. Cybersecurity Framework Profile for AI — first NIST publication addressing agentic systems as a distinct use case. Layer 1/2.

## 2026-06-01 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026, agent specification validation markdown skill 2026 May
Status: **NEW FINDINGS FOUND**

### New Papers
1. **SkCC** (arXiv:2605.03353) — Portable and Secure Skill Compilation for Cross-Framework LLM Agents. May 5, 2026. Introduces SkIR, a strongly-typed intermediate representation that decouples skill semantics from framework-specific formatting. Static optimizer enforces security constraints, blocking vulnerabilities before deployment. Reduces adaptation complexity from O(m×n) to O(m+n). 94.8% proactive security trigger rate. URL: https://arxiv.org/abs/2605.03353 — **Layer 1/2** — Directly addresses SKILL.md portability and security across frameworks. This is the skill compilation/validation infrastructure we need.

2. **LASM / Systematic Survey** (arXiv:2604.23338) — A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework. Apr 25, 2026. Seven-layer framework (Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, Governance). L7 Governance = accountability and observability layer spanning the stack. Attack temporality dimension (T1-T4). Most dangerous threats at L5-L7 + T3-T4 (covert collusion, memory poisoning, MCP supply-chain compromise). Only 7% of existing research covers this zone. Identifies AgentSafe (formal spec language), AgentIndex (governance maturity benchmark), and audit protocol benchmarks. URL: https://arxiv.org/abs/2604.23338 — **Layer 1/2/3** — The survey maps our exact problem space and identifies the governance gap as the most under-researched zone.

3. **Evidence-Synthesis Framework** (arXiv:2604.19818) — Beyond Task Success: An Evidence-Synthesis Framework for Evaluating, Governing, and Orchestrating Agentic AI. Apr 18, 2026. Core finding: governance-to-action closure gap — evaluation tells us if outcomes were good, governance defines what should be allowed, but neither binds obligations to concrete actions or proves compliance later. Introduces ODTA runtime test (observability, decidability, timeliness, attestability) and minimum action-evidence bundle. URL: https://arxiv.org/abs/2604.19818 — **Layer 2/3** — Bridges the gap between governance specs and runtime validation. Directly relevant to "how to verify if specs are well defined."

4. **AIP / Agent Identity Protocol** (arXiv:2603.24775) — AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A. Mar 25, 2026. 2,000 MCP servers scanned — all lacked authentication. Introduces Invocation-Bound Capability Tokens (IBCTs) with compact (JWT) and chained (Biscuit/Datalog) modes. 100% rejection rate across 600 attack attempts. Reference implementations in Python and Rust. URL: https://arxiv.org/abs/2603.24775 — **Layer 1** — Identity and delegation is the foundation of skill/agent governance. Without verifiable identity, no accountability chain exists.

5. **Trace-Based Assurance Framework** (arXiv:2603.18096) — A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance. Mar 18, 2026. Message-Action Traces (MAT) with explicit step and trace contracts. Machine-checkable verdicts, deterministic replay, stress testing via budgeted counterexample search, structured fault injection. Governance as runtime component enforcing per-agent capability limits and action mediation (allow/rewrite/block). URL: https://arxiv.org/abs/2603.18096 — **Layer 1/2** — Runtime governance with contracts and traceability. The "action mediation at language-to-action boundary" is exactly what we need for skill enforcement.

6. **EmbodiedGovBench** (arXiv:2604.11174) — EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems. Apr 13, 2026. Seven governance dimensions: unauthorized capability invocation, runtime drift robustness, recovery success, policy portability, version upgrade safety, human override responsiveness, audit completeness. URL: https://arxiv.org/abs/2604.11174 — **Layer 2** — Governance-as-first-class evaluation target. The benchmark structure (perturbation operators + governance metrics) can be adapted to non-embodied agent systems.

7. **Healthcare Skills** (arXiv:2605.02709) — An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance. May 4, 2026. First empirical analysis of 557 healthcare skills from 58,159 public skills. Ten dimensions: function, deployment context, autonomy, safety. Finding: general technical risk does not reliably capture clinical risk. Skills act as procedural layer not addressed by current benchmarks. URL: https://arxiv.org/abs/2605.02709 — **Layer 2/3** — Domain-specific evidence that skill governance gaps exist in practice. Shows that current risk frameworks miss skill-level risks.

8. **AgentCity** (arXiv:2604.07007) — AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Power. Apr 8, 2026. Separation of Power (SoP) model on blockchain: agents legislate rules as smart contracts, deterministic software executes within contracts, humans adjudicate through ownership chain. Smart contracts are the law itself — legislative output that governs agent behavior. 50-1,000 agent scale experiment. URL: https://arxiv.org/abs/2604.07007 — **Layer 3** — Constitutional governance at scale. The "smart contracts as law" concept is a governance specification that is machine-enforceable.

9. **Auditable Agents** (arXiv:2604.05485) — Auditable Agents: Measuring and Enforcing Accountability in LLM-Based Systems. Apr 7, 2026. Five dimensions: action recoverability, lifecycle coverage, policy checkability, responsibility attribution, evidence integrity. Three mechanism classes: detect, enforce, recover. Auditability Card proposed. 617 security findings across six prominent open-source projects show basic prerequisites are unmet. 8.3 ms median overhead for pre-execution mediation. URL: https://arxiv.org/abs/2604.05485 — **Layer 1/2** — Accountability requires auditability. The framework directly measures whether an agent system can be governed after deployment.

10. **SentinelAgent** (arXiv:2604.02767) — SentinelAgent: Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems. Apr 3, 2026. Delegation Chain Calculus (DCC) with seven properties (authority narrowing, policy preservation, forensic reconstructibility, cascade containment, scope-action conformance, output schema conformance, intent preservation). 100% TPR at 0% FPR on DelegationBench v4 (516 scenarios, 10 attack categories). TLA+ verified across 2.7 million states. URL: https://arxiv.org/abs/2604.02767 — **Layer 1** — Formal verification of delegation chains. The properties (P1-P7) are exactly the kind of verifiable guarantees we need for skill/agent governance.

11. **Implicit Execution Tracing** (arXiv:2603.17445) — When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution. Mar 18, 2026. IET embeds agent-specific statistical signals into token generation, making output text a self-verifying execution record. Accurate attribution under identity removal, boundary corruption, privacy-preserving redaction. URL: https://arxiv.org/abs/2603.17445 — **Layer 1/2** — Provenance-by-design for multi-agent systems. Enables accountability when execution logs are unavailable.

### New Products/Frameworks
1. **Snyk Agent Scan** — Analyzes SKILL.md to detect known malicious patterns. 90-100% recall on confirmed malicious skills, 0% false positive rate on top 100 legitimate skills. Integrates with Skills.sh marketplace. URL: https://labs.snyk.io — **Layer 1** — Directly validates skill markdown security. This is the automated validation tool for the skill layer.

2. **OWASP Practical Guide for Secure MCP Server Development** — Feb 2026. Practical guide for developers building MCP servers. URL: https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications — **Layer 1** — Fills the gap between OWASP Top 10 and actual implementation.

3. **OWASP CheatSheet for Third-Party MCP Servers** — Security checklist for evaluating third-party MCP servers before integration. URL: https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications — **Layer 1** — Operational security guidance for MCP skill supply chain.

4. **GitHub Spec Kit / SDD (Specification-Driven Development)** — GitHub's movement promoting `.spec.md` files as governance artifacts. 2026-07-01 article. Specification as first-class artifact, version-controlled, machine-readable. URL: https://github.com/topics/skill-md — **Layer 3** — The SDD philosophy aligns with our spec/skill/agent markdown governance approach: specs as enforceable contracts.

5. **Web Skills Protocol (WSP)** — 0xtresser / OpenClaw. Specification v0.1 (March 2026). Web discovery layer for skills.txt/agents.txt. Complements robots.txt (access control) and llms.txt (content reading) with capabilities for action. URL: https://github.com/openclaw/skills/blob/main/skills/0xtresser/web-skills-protocol/SPEC.md — **Layer 0/1** — Discovery and validation protocol for web-published skills. Standardizes how sites publish agent capabilities.

6. **Agentic AI Foundation (AAIF)** — Under Linux Foundation. Governing body for AGENTS.md and MCP standards. URL: https://github.com/topics/agent-ready — **Layer 3** — Governance structure for the standards themselves. Important for long-term spec stewardship.

7. **FinBot Agentic AI CTF** — Capture The Flag competition for agentic AI security. 2026-05-26. URL: https://www.techtimes.com/articles/304034/20260526/finbot-launches-first-agentic-ai-ctf.htm — **Layer 2** — Gamified security evaluation. CTFs produce reusable test cases and benchmark data.
- **CRITICAL:** Scout only reports and pushes to git when NEW findings are discovered
- If no new findings: finish silently (NO_REPLY, no git push, no report)
- This avoids noise and only surfaces actual new research
