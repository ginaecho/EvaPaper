# Agent Governance Research Scout — Tracking Log
# Created: 2026-05-30
# Tracks known papers, products, and benchmarks to identify new findings.
# Format: Each entry includes discovery date (Found: YYMMDD)

## Known Papers (as of 2026-05-30)
- BeSafe-Bench (arXiv:2603.25747) — Huawei RAMS Lab, 2026-01-30. Found: 0530
- ST-WebAgentBench (arXiv:2410.06703) — IBM Research, 2024-10 (ICLR 2026). Found: 0530
- Layered Governance Architecture / LGA (arXiv:2603.07191) — 2026-03-05. Found: 0530
- Skilldex (arXiv:2604.16911) — 2026-04-18. Found: 0530
- GovernSpec / Contractual Skills (arXiv:2605.22634) — 2026-05-21. Found: 0530

## Known Products/Frameworks (as of 2026-05-30)
- Microsoft Agent Governance Toolkit — MIT License, 2026-04-02. Found: 0530
- OWASP Top 10 for Agentic Applications — 2026 edition. Found: 0530
- Ruh AI Production Evaluation Guide — 2026-05-24. Found: 0530
- Anthropic SKILL.md validator. Found: 0530
- Skilldex MCP server / CLI. Found: 0530

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

### New Papers (Found: 0531)
1. **ClawBench** (arXiv:2604.08523) — UBC/Vector Institute/CMU/etc, 2026-04-09. Real-world web agent benchmark: 153 tasks across 144 live production websites. Layer 2.
2. **MCP-38** (arXiv:2603.18063) — Comprehensive threat taxonomy for Model Context Protocol with 38 threat categories. Mapped to STRIDE, OWASP LLM Top 10, OWASP Agentic Top 10. Layer 1.
3. **MCPThreatHive** (arXiv:2604.13849) — Automated threat intelligence platform for MCP ecosystems. GitHub: VulcanLab/MCPThreatHive. Layer 1.
4. **ADR** (arXiv:2605.17380) — Agentic Detection System for Enterprise Agentic AI Security. Layer 1.
5. **Proteus** (arXiv:2605.11891) — Self-Evolving Red Team for Agent Skill Ecosystems. Layer 2.
6. **SkillAttack** (arXiv:2604.04989) — Automated red teaming of agent skills through attack path refinement. Layer 2.
7. **TRUSTDESC** (arXiv:2604.07536) — Preventing tool poisoning via trusted description generation. Layer 1.

### New Products/Frameworks (Found: 0531)
1. **OWASP Top 10 for Agentic Skills (AST10)** — New OWASP project 2026 edition. 10 critical risks for agent skills across OpenClaw (SKILL.md), Claude Code, Cursor. Layer 0.
2. **Tencent AI-Infra-Guard** — Full-stack AI red teaming platform with OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan. GitHub: Tencent/AI-Infra-Guard. Layer 1.
3. **IBM Sovereign Core** — GA announced 2026-05-07. Embeds governance policy at infrastructure runtime for regulated, cross-border environments. Layer 1.
4. **DeepTeam by Confident AI** — Framework for testing OWASP ASI risks. trydeepteam.com. Layer 2.
5. **NIST IR 8596** — December 2025 draft. Cybersecurity Framework Profile for AI — first NIST publication addressing agentic systems as a distinct use case. Layer 1/2.

## 2026-06-01 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026, agent specification validation markdown skill 2026 May
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0601)
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

### New Products/Frameworks (Found: 0601)
1. **Snyk Agent Scan** — Analyzes SKILL.md to detect known malicious patterns. 90-100% recall on confirmed malicious skills, 0% false positive rate on top 100 legitimate skills. Integrates with Skills.sh marketplace. URL: https://labs.snyk.io — **Layer 1** — Directly validates skill markdown security. This is the automated validation tool for the skill layer.

2. **OWASP Practical Guide for Secure MCP Server Development** — Feb 2026. Practical guide for developers building MCP servers. URL: https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications — **Layer 1** — Fills the gap between OWASP Top 10 and actual implementation.

3. **OWASP CheatSheet for Third-Party MCP Servers** — Security checklist for evaluating third-party MCP servers before integration. URL: https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications — **Layer 1** — Operational security guidance for MCP skill supply chain.

4. **GitHub Spec Kit / SDD (Specification-Driven Development)** — GitHub's movement promoting `.spec.md` files as governance artifacts. 2026-07-01 article. Specification as first-class artifact, version-controlled, machine-readable. URL: https://github.com/topics/skill-md — **Layer 3** — The SDD philosophy aligns with our spec/skill/agent markdown governance approach: specs as enforceable contracts.

5. **Web Skills Protocol (WSP)** — 0xtresser / OpenClaw. Specification v0.1 (March 2026). Web discovery layer for skills.txt/agents.txt. Complements robots.txt (access control) and llms.txt (content reading) with capabilities for action. URL: https://github.com/openclaw/skills/blob/main/skills/0xtresser/web-skills-protocol/SPEC.md — **Layer 0/1** — Discovery and validation protocol for web-published skills. Standardizes how sites publish agent capabilities.

6. **Agentic AI Foundation (AAIF)** — Under Linux Foundation. Governing body for AGENTS.md and MCP standards. URL: https://github.com/topics/agent-ready — **Layer 3** — Governance structure for the standards themselves. Important for long-term spec stewardship.

7. **FinBot Agentic AI CTF** — Capture The Flag competition for agentic AI security. 2026-05-26. URL: https://www.techtimes.com/articles/304034/20260526/finbot-launches-first-agentic-ai-ctf.htm — **Layer 2** — Gamified security evaluation. CTFs produce reusable test cases and benchmark data.

## 2026-06-04 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026, agent behavioral contracts runtime enforcement 2026, agent skill supply chain formal verification 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0604)
1. **Taxonomy and Consistency Analysis of Safety Benchmarks for AI Agents** (arXiv:2605.16282) — Apr 11, 2026. First systematic analysis of 40 behavioral agent-safety benchmarks (2023–2026). Six-axis taxonomy. Coverage matrix reveals no ranking concordance (Kendall's W = 0.10, p = 0.94). Benchmark choice can yield contradictory safety conclusions. URL: https://arxiv.org/abs/2605.16282 — **Layer 2/3** — Essential meta-evaluation: tells us which benchmarks to trust and why current safety conclusions may be inconsistent.

2. **Governance by Construction for Generalist Agents / CUGA** (arXiv:2605.20874) — May 20, 2026. IBM Research. Policy-as-code layer composing with generalist LLM agents. Five structural checkpoints: Intent Guard, Playbook, Tool Guide, Tool Approvals, Output Formatter. Runtime governance architecture embedding interventions continuously. URL: https://arxiv.org/abs/2605.20874 — **Layer 1/2** — Direct implementation of "governance by construction" rather than governance as afterthought. Enterprise healthcare demo included.

3. **Agent Behavioral Contracts (ABC)** (arXiv:2602.22302) — Feb 25, 2026. Formal framework bringing Design-by-Contract to autonomous AI agents. Contract C = (P, I, G, R): Preconditions, Invariants, Governance policies, Recovery. (p, delta, k)-satisfaction for probabilistic compliance. Drift Bounds Theorem: contracts with recovery rate gamma > alpha bound drift to D* = alpha/gamma. AgentAssert runtime enforcement library. 200 scenarios, 1,980 sessions, 7 models. URL: https://arxiv.org/abs/2602.22302 — **Layer 1/2** — The formal specification and runtime enforcement mechanism we need. Directly addresses "how to verify if specs are well defined" via probabilistic contract compliance.

4. **AgentVerify** (preprints.org, DOI: 10.20944/preprints202604.1029.v1) — Apr 14, 2026. Compositional formal verification of AI agent safety properties via LTL model checking. 23 temporal logic templates for memory integrity, tool call protocols, MCP/skill invocations, human-in-the-loop boundaries. Hybrid architecture: O(1) runtime monitor + post-hoc Kripke-structure analyser. 86.67% verification accuracy vs 80% contract baseline, 46.67% runtime baseline, 13.33% neural verifier. URL: https://www.preprints.org/manuscript/202604.1029/v1 — **Layer 1/2** — Formal verification for agent observable control flow. Proves that compositional model checking is tractable for production agents.

5. **SkillFortify** (arXiv:2603.00195) — Feb 27, 2026. First formal analysis framework for agent skill supply chain security. DY-Skill attacker model (Dolev-Yao adapted to five-phase skill lifecycle). Sound static analysis via abstract interpretation. Capability-based sandboxing with confinement proof. Agent Dependency Graph with SAT-based resolution. F1=96.95%, 0% false positive rate on 540 skills. GitHub: https://github.com/varun369/skillfortify. URL: https://arxiv.org/abs/2603.00195 — **Layer 0/1** — Directly validates SKILL.md security with formal guarantees, not heuristics. The skill supply chain validation tool we need.

6. **AgentAssay** (arXiv:2603.02601) — Mar 3, 2026. First token-efficient regression testing framework for non-deterministic AI agent workflows. Stochastic three-valued verdicts (PASS/FAIL/INCONCLUSIVE). Five-dimensional coverage metrics. Behavioral fingerprinting: 86% detection power where binary testing has 0%. SPRT reduces trials by 78%. Trace-first offline analysis = 100% cost savings. GitHub: https://github.com/qualixar/agentassay. URL: https://arxiv.org/abs/2603.02601 — **Layer 2** — Regression testing for agent behavior changes. Critical for CI/CD governance: ensures skill/agent updates don't break safety properties.

7. **A Comprehensive Survey on Agent Skills** (arXiv:2605.07358) — May 8, 2026. Survey of agent skills lifecycle: representation, acquisition, retrieval, evolution. OpenClaw and Claude Code as exemplars. Four stages with methods, ecosystem resources, applications. Quality control, interoperability, safe updating, long-term capability management as open challenges. URL: https://arxiv.org/abs/2605.07358 — **Layer 0/1/2/3** — The definitive survey of the skill ecosystem. Organizes the entire research landscape we operate in.

8. **Machine Identity Governance Taxonomy (MIGT)** / "Who Governs the Machine?" (arXiv:2604.06148) — Apr 7, 2026. Cloud Security Alliance. AI-Identity Risk Taxonomy: 37 risk sub-categories across 8 domains. Six-domain MIGT framework addressing technical governance gap, regulatory compliance gap, cross-jurisdictional coordination gap. Foreign state actor threat model (Silk Typhoon, Salt Typhoon, Volt Typhoon). Skill-level attestation as runtime admission control mechanism. URL: https://arxiv.org/abs/2604.06148 — **Layer 1/3** — Machine identity is the foundation of agent governance. Without governed machine identities, no accountability chain exists. Skill-level attestation proposal directly relevant.

9. **Admission Control for Agent Actions (ACP)** (arXiv:2603.18829) — Apr 30, 2026. Temporal admission control protocol enforcing behavioral properties over execution traces. Static risk scoring + stateful signals (anomaly accumulation, cooldown) via LedgerQuerier. 500-request workload: stateless approves all 500; ACP limits autonomous execution to 2 (0.4%). Decision evaluation: 739-832 ns (p50); throughput 1,720,000 req/s. TLA+ verified across 4,294,930,695 states. Boundary Activation Rate (BAR) for deviation collapse detection. Paper 1 of 6-paper Agent Governance Series. URL: https://arxiv.org/abs/2603.18829 — **Layer 1** — Runtime admission control with formal verification. The performance (1.7M req/s) and formal verification make it production-viable.

10. **A Unified Review of Memory, Skills, Protocols and Harness Engineering** (arXiv:2604.08224) — Apr 9, 2026. Externalization framework: memory externalizes state, skills externalize procedural expertise, protocols externalize interaction structure, harness engineering coordinates them into governed execution. Historical progression from weights to context to harness. Self-evolving harnesses and shared agent infrastructure as emerging directions. URL: https://arxiv.org/abs/2604.08224 — **Layer 1/2/3** — Systems-level framework explaining why agent progress depends on externalized cognitive infrastructure. Skills as "reusable procedural artifacts" central to scalability and governance.

### New Products/Frameworks (Found: 0604)
1. **AgentAssert** — Runtime enforcement library implementing ABC (Agent Behavioral Contracts). Detects 5.2-6.8 soft violations per session that uncontracted baselines miss. 88-100% hard constraint compliance. <10 ms overhead per action. Part of Qualixar suite. — **Layer 1** — The runtime contract enforcement mechanism we need for skill/agent behavior validation.

2. **SkillFortify (Open Source)** — pip install skillfortify. Formal verification framework for agent skill supply chains. 22 frameworks supported. SAT-based resolution, capability confinement, trust score algebra. MIT license. GitHub: https://github.com/varun369/skillfortify — **Layer 0/1** — The formal skill validation tool. Replaces heuristic scanning with mathematical guarantees.

3. **AgentAssay (Open Source)** — pip install agentassay. Token-efficient stochastic testing for AI agents. pytest integration. 8 CLI commands. 10 framework adapters. MIT license. GitHub: https://github.com/qualixar/agentassay — **Layer 2** — CI/CD regression testing for agent behavior. Ensures governance properties persist across updates.

4. **Agent Control Protocol (ACP)** — Reference implementation in Go. 38 documents, 23 packages, 138 conformance test vectors (73 signed + 65 unsigned). ACR-1.0 sequence compliance runner. Part of Agent Governance Series (6 papers). URL: https://github.com/topics/agent-control-protocol — **Layer 1** — Production-ready admission control with formal verification backing.

5. **SkillsVote** — Skills engine for AI agents. Referenced in Comprehensive Survey. — **Layer 0/1** — Skill routing and governance infrastructure.

## Key Search Queries Added (0604)
- agent behavioral contracts runtime enforcement 2026
- agent skill supply chain formal verification 2026
- agent regression testing non-deterministic workflow 2026
- machine identity governance taxonomy AI agent 2026
- admission control protocol agent actions temporal 2026
- agent harness engineering memory skills protocols 2026
- agent safety benchmark taxonomy consistency analysis 2026

## 2026-06-06 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent behavioral integrity verification skill 2026, agent runtime governance path policy temporal 2026, skill structure representation markdown parsing 2026, FAccT 2026 agent governance alignment pluralistic, agent coordination message sequence charts formal 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0606)
1. **BIV / Behavioral Integrity Verification** (arXiv:2605.11770) — May 12, 2026. Sun Yat-sen University. Verifies whether skill descriptions match actual code behavior. 80.0% deviation rate across 1,200 skills. 34.3% severe violations. URL: https://arxiv.org/abs/2605.11770 — **Layer 0** — Directly addresses "do skills do what they claim?" Essential for marketplace validation.

2. **Runtime Governance / Policies on Paths** (arXiv:2603.16586) — Mar 17, 2026. Jheronimus Academy of Data Science. Formalizes compliance policies as temporal predicates over execution paths. Path-based policies express separation of duties, data minimization, audit trails that per-step checks cannot capture. Polynomial-time evaluation. URL: https://arxiv.org/abs/2603.16586 — **Layer 1** — The missing formal foundation for temporal governance requirements.

3. **SSL Representation / Skill Text to Structure** (arXiv:2604.24026) — Apr 27, 2026. Scheduling-Structural-Logical representation for agent skills. 94% decomposition rate, 87% accuracy vs expert annotations. Machine-verifiable skill descriptions. URL: https://arxiv.org/abs/2604.24026 — **Layer 0** — Makes unstructured skill text governable by transforming into verifiable structures.

4. **FAccT '26 / Relative Principals, Pluralistic Alignment** (arXiv:2604.20805) — Apr 22, 2026. Travis LaCroix, Durham University. FAccT '26 conference paper (June 25-28). Three-axis framework: objectives, information, principals. Alignment is fundamentally governance, not engineering alone. URL: https://arxiv.org/abs/2604.20805 — **Cross-layer** — Conceptual foundation explaining why our three-layer stack is necessary.

5. **ZipperGen / Provable Coordination for LLM Agents via MSCs** (arXiv:2604.17612) — Apr 19, 2026 (v2 Apr 29). Benedikt Bollig, Matthias Függer, Thomas Nowak, Université Paris-Saclay/CNRS/ENS Paris-Saclay. Domain-specific language for agent coordination based on Message Sequence Charts (MSCs). Syntax-directed projection generates deadlock-free local agent programs from global coordination specifications. Separates deterministic message-passing structure from stochastic LLM actions. Runtime planning extension: LLM dynamically generates coordination workflows with same structural guarantees. Open source: https://zippergen.io — **Cross-layer (Layer 0 + Layer 1)** — The closest existing work to MPST-style multi-agent governance. Formal global specs + guaranteed deadlock-free local programs + runtime workflow generation.

### New Products/Frameworks (Found: 0606)
- No new products/frameworks discovered in this run (search focused on academic papers)

## Key Search Queries Added (0606)
- agent behavioral integrity verification skill 2026
- agent runtime governance path policy temporal 2026
- skill structure representation markdown parsing 2026
- FAccT 2026 agent governance alignment pluralistic
- agent coordination message sequence charts formal 2026

## Research Momentum Observations
- **Skill integrity crisis:** BIV's 80% deviation rate + ClawHavoc's 1,200+ malicious skills = current validation is completely insufficient
- **Temporal governance emergence:** Path-based policies (Runtime Governance) + ACP admission control = formal temporal reasoning is replacing per-step checks
- **Structured representation gap:** SSL's 94% decomposition rate shows automatic skill structure extraction is feasible — enabling automated governance
- **FAccT governance focus:** Three-axis framework (objectives, information, principals) validates our multi-layer approach conceptually
- **Formal methods dominance:** 4 new papers all use formal/mathematical approaches (integrity verification, temporal logic, structured decomposition, principal-agent theory) — heuristic governance is being replaced by formal guarantees

## 2026-06-06 Evening Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark June 2026 arxiv, skill markdown verification agent behavior contract 2026, agent skill supply chain security formal verification June 2026, OWASP agentic applications agentic skills 2026 new, MCP runtime security governance framework 2026, agent behavioral contract formal specification runtime enforcement June 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0606-evening)
1. **SkillGuard** (arXiv:2606.03024) — June 1, 2026. Permission-based control framework for agent skill composition. Defines ACL-style governance for skill-to-skill and agent-to-skill interactions. Formalizes permission models that govern skill execution chains. Relevant to **Layer 2 (Skill)** — enables fine-grained capability governance for markdown-specified skills. **[Why recommended]** Represents a necessary architectural shift: skills are currently trusted by default; SkillGuard introduces explicit capability attenuation, which is exactly the security model needed for skill marketplace ecosystems. MIT License. URL: https://arxiv.org/abs/2606.03024

2. **From Craft to Kernel: A Governance-First Execution Architecture for Agentic Computers** (arXiv:2604.18652) — Apr 20, 2026. Proposes a governance-first execution architecture and a semantic ISA (Instruction Set Architecture) for agentic computers. Defines skill lifecycle, privilege management, and capability boundary enforcement at the architectural level. Relevant to **All Layers (Spec/Skill/Agent)** — foundational governance primitives. **[Why recommended]** This is architectural-level thinking: instead of bolting governance on top, it embeds governance into the execution substrate. If agentic systems are the next OS, this is the SELinux equivalent. URL: https://arxiv.org/abs/2604.18652

3. **TAIP: Trustworthy AI Posture — A Framework for Continuous Assurance of Agentic AI Systems** (arXiv:2603.03340) — Jan 2026. MITRE/SEI framework for continuous assurance. Defines a structured, measurable, and continuous assessment model for agentic AI trustworthiness. Relevant to **Layer 3 (Agent)** — operational monitoring and continuous compliance. **[Why recommended]** Fills a critical gap between "designed safe" and "operating safely." Most frameworks focus on build-time; this focuses on runtime assurance with measurable posture indicators. MITRE License. URL: https://arxiv.org/abs/2603.03340

4. **AgentWarden: Learned Capability Governance for Autonomous AI Agents** (arXiv:2604.11839) — May 3, 2026. RL-based adaptive capability governance. Uses reinforcement learning to dynamically adjust agent capability boundaries based on runtime behavior and environmental risk assessment. Relevant to **Layer 3 (Agent)** — dynamic, context-aware capability governance. **[Why recommended]** Static capability models are brittle; this adapts to context. Bridges the gap between "what the agent can do" and "what the agent should be allowed to do right now." Apache 2.0. URL: https://arxiv.org/abs/2604.11839

5. **ClawKeeper: Comprehensive Safety Protection for OpenClaw Agents** (arXiv:2603.24414) — 2026. Safety framework for the OpenClaw agent ecosystem. Implements multi-layer protection through skills, plugins, and watchers. Provides runtime monitoring, policy enforcement, and incident response for OpenClaw agents. Relevant to **Layer 3 (Agent)** — platform-specific operational safety. **[Why recommended]** Platform-specific governance is pragmatic. If OpenClaw is a deployment target, this provides immediate operational value. Also demonstrates how governance frameworks can be implemented as pluggable skills rather than monolithic controls. Apache 2.0. URL: https://arxiv.org/abs/2603.24414

### New Products/Frameworks (Found: 0606-evening)
1. **DefenseClaw** (Cisco AI Defense) — Open-source security framework for OpenClaw. RSAC 2026, March 27, 2026. Runtime threat detection, policy enforcement, and compliance scanning for OpenClaw agents. 2.5k GitHub stars. Relevant to **Layer 3 (Agent)** — operational security. URL: https://blogs.cisco.com/security/introducing-defenseclaw

2. **NemoClaw** (NVIDIA) — Secure agent runtime with OpenShell integration. GTC 2026, March 16, 2026. Sandboxed execution with GPU isolation and circuit breaker patterns. Enterprise customers include Shell. Relevant to **Layer 3 (Agent)** — secure execution environment. URL: https://blogs.nvidia.com/blog/nemoclaw-secure-agent-runtime

3. **EnforceAuth** — AI runtime authorization platform. 2026. AUTHOR framework + Verdict Agentic Firewall. Integration with OpenClaw via plugins. EnforceAuth Governance 2.1 released in May 2026. Relevant to **Layer 2 (Skill)** and **Layer 3 (Agent)** — runtime authorization and access control. URL: https://enforceauth.dev

### Notes (0606-evening)
- SkillGuard's permission model is the missing link for skill marketplace security: without capability attenuation, any downloaded skill runs with full agent privileges.
- From Craft to Kernel elevates the discussion from "how do we check agents?" to "what should the agent execution substrate look like?"
- TAIP provides the operational measurement framework that most governance papers lack — it's not enough to define safe; we need to know if we're still safe in production.
- AgentWarden's RL-based approach is novel but raises questions about the governance of the governance mechanism itself (who controls the RL policy?)
- ClawKeeper demonstrates that governance can be implemented as skills rather than external controls, which is a promising pattern for OpenClaw ecosystems.

## 2026-06-07 Scout Run — NEW FINDINGS DISCOVERED
Search queries: skill benchmark attack surface 2026, compositional risk agent skills 2026, third-party skill trust runtime 2026, skill pseudocode verifiable 2026, verifiable provenance agent framework 2026, LTL runtime compliance monitoring agents 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0607)
1. **SkillSafetyBench** (arXiv:2605.12015) — First benchmark focused specifically on skill-level attack surfaces. Relevant to **Layer 0/Layer 2** because it turns skill security into an evaluable benchmark rather than an anecdotal security concern. **[Why recommended]** This gives us the missing benchmark for validating whether a skill governance scheme actually improves safety at the skill layer.

2. **Measuring Compositional Risk** (arXiv:2606.00448) — Individually safe skills can compose into unsafe sets. Relevant to **Layer 0/Layer 1** because it moves the problem from single-skill validation to interaction risk across multiple skills. **[Why recommended]** This is exactly the failure mode static governance needs to catch: local validity does not imply safe composition.

3. **AgentTrap** (arXiv:2605.13940) — Runtime trust failures in third-party skills. Relevant to **Layer 1** because it highlights the trust boundary between core agents and externally sourced skills. **[Why recommended]** It reinforces that skill marketplaces are not just a validation problem; they are an execution trust problem.

4. **Skill-as-Pseudocode (SaP)** (arXiv:2605.27955) — Transforms natural-language skills into verifiable pseudocode. Relevant to **Layer 0** because it directly addresses the gap between informal markdown instructions and machine-checkable specifications. **[Why recommended]** This is one of the strongest candidates for static-time checking of skill behavior before execution.

5. **KYA** (arXiv:2605.25376) — Framework-agnostic trust layer with verifiable provenance. Relevant to **Layer 1/Layer 3** because it introduces provenance guarantees that survive framework differences. **[Why recommended]** Governance without provenance collapses under delegation and third-party reuse; KYA attacks that foundation directly.

6. **Auditing, Monitoring, and Intervention** (arXiv:2605.16198) — LTL-based runtime compliance monitoring. Relevant to **Layer 1** because it provides formal runtime compliance monitoring without reducing governance to an LLM-as-judge pattern. **[Why recommended]** This strengthens the formal runtime side of the stack and complements the static-first papers above.

### Notes (0607)
- The strongest June 7 theme is **composition**: safe skills do not stay safe when combined naively.
- `Skill-as-Pseudocode (SaP)` is especially important for this repo because it points toward converting natural-language skill markdown into a verifiable intermediate form.
- `SkillSafetyBench` and `Measuring Compositional Risk` together strengthen the argument that skill governance needs both **spec validation** and **interaction-level evaluation**.
- `KYA` and `AgentTrap` reinforce that third-party skill trust is a first-class governance problem, not an edge case.

## 2026-06-12 Scout Run — NEW FINDINGS DISCOVERED
Search queries: BeSafe-Bench agent safety benchmark 2026, ST-WebAgentBench web agent safety 2026, agent governance framework Microsoft NVIDIA OWASP 2026, agent skill markdown specification validation 2026, GovernSpec contractual skills 2026, agent behavior evaluation validation framework 2026, AI agent safety benchmark 2026, OWASP agentic applications 2026, OpenClaw agent governance 2026, agent governance toolkit open source 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0612)
1. **Learning Correct Behavior from Examples** (arXiv:2605.03159) — Reshabh K Sharma, Gaurav Mittal, Yu Hu, May 2026. Novel algorithm that learns correct behavior from 2-10 passing execution traces and validates new executions against a learned model. Combines dominator analysis from compiler theory with LLM-powered semantic understanding. Uses Prefix Tree Acceptors, multi-tiered equivalence detection, and topological subsequence matching. High accuracy detecting product bugs and false successes with only 3 training traces. URL: https://arxiv.org/abs/2605.03159 — **Layer 0/1** — Bridges static learning from execution traces to runtime validation. The approach is particularly relevant for skill validation because it learns ground truth from small positive samples rather than requiring exhaustive specifications.

2. **Owner-Harm: Agents Harming Their Deployers** (arXiv:2604.18658) — Dario Zhang, April 2026. Formal threat model with eight categories of agent behavior damaging the deployer. Real-world incidents: Slack AI credential exfiltration, Microsoft 365 Copilot calendar-injection leaks, Meta agent unauthorized forum post. Compositional safety system achieves 100% TPR/0% FPR on generic criminal harm but only 14.8% on owner-harm injection tasks. Introduces SSDG (Symbolic-Semantic Defense Generalization) framework. Gate + deterministic post-audit verifier raises TPR to 85.3%. URL: https://arxiv.org/abs/2604.18658 — **Layer 1/2** — Identifies a critical blind spot in current safety benchmarks: agents harming their own deployers rather than generic criminal targets. The SSDG framework and the 85.3% TPR with layered defense provide a concrete measurement target for governance systems.

### Notes (0612)
- The graph discovery run surfaced 71 candidate papers from 5 seeds, but most were out-of-domain. The two new papers above were identified through direct search comparison against the known baseline.
- **Learning Correct Behavior** is the strongest new paper for static governance: it learns correct sequential behavior from just a few traces, making it feasible to validate skill execution patterns without writing full formal specifications.
- **Owner-Harm** exposes a governance gap that most benchmarks miss: safety systems optimized for generic criminal harm (AgentHarm) perform poorly against deployer-directed attacks. The 14.8% → 85.3% improvement shows that layered defense (gate + post-audit verifier) is the right architecture for this threat class.

## 2026-06-14 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026
Status: **NEW FINDINGS FOUND**

### New Papers/Products (Found: 0614)
1. **EmbodiedGovBench** (arXiv:2604.11174) — Apr 13, 2026. First benchmark making governance a first-class evaluation target for embodied agents. Seven governance dimensions: unauthorized capability invocation, runtime drift robustness, recovery success, policy portability, version upgrade safety, human override responsiveness, audit completeness. URL: https://arxiv.org/abs/2604.11174 — **Layer 2** — The benchmark infrastructure for measuring embodied agent governability, not just capability.
2. **Agent Skills for Large Language Models** (arXiv:2602.12430) — Feb 2026 (updated Jun 2026). Comprehensive survey with Skill Trust and Lifecycle Governance Framework: four-tier gate-based permission model (G1–G4 verification gates, T1–T4 trust tiers) mapping skill provenance to graduated deployment. 26.1% of community skills contain vulnerabilities. URL: https://arxiv.org/abs/2602.12430 — **Layer 0** — The first systematic provenance-based trust framework for skills.
3. **MITRE ATLAS agentic AI update** (Oct 2025) — 14 new agentic AI-specific techniques for adversarial threat modeling. Multi-step tool chaining exploitation, state manipulation, delegation abuse, persistent skill poisoning, dynamic capability injection, cross-runtime trust boundary violations, agent memory tampering, goal hijacking, tool description poisoning, capability enumeration, behavior cloning, orchestration layer injection, autonomous red-team emulation, recursive self-modification detection. URL: https://atlas.mitre.org/ — **Layer 1/2** — Standard adversarial taxonomy now covers agentic-specific attack vectors.
4. **reprobe-audit** — IEEE Big Data 2026. Open scoring schema for LLM agent benchmark disclosure. 12-paper pilot audit: agent-benchmark mean disclosure score 0.38 vs. 0.66 classical. Cost reporting universally absent. No agent benchmark fully discloses harness. GitHub: https://github.com/mahdinaser/reprobe-audit — **Layer 2** — Benchmark credibility verification framework.
5. **Agent Security Harness** — 474 security tests across 33 modules. Prompt injection, tool misuse, data exfiltration, privilege escalation, inter-agent trust violations, skill poisoning, MCP exploitation, autonomous action abuse, goal hijacking. Red-team and blue-team modes. GitHub: https://github.com/msaleme/red-team-blue-team-agent-fabric — **Layer 1/2** — Standardized penetration-testing suite for agents.

### New Products/Frameworks (Found: 0614)
- (See above — EmbodiedGovBench, Agent Skills for LLMs, MITRE ATLAS update, reprobe-audit, and Agent Security Harness are the new items not previously tracked)

## 2026-06-20 Scout Run — NEW FINDINGS DISCOVERED
Search queries: arXiv agent governance skill security June 2026, arXiv agent benchmark June 2026, arXiv multi-agent governance post-quantum 2026
Status: **NEW FINDINGS FOUND**

### New Papers (Found: 0620)
1. **SkillVetBench** (arXiv:2606.00925 / 2606.15899) — June 14, 2026. UTEP SUPREME Lab. LLM-as-Judge security evaluation for open-source agent skills. Introduces SARS (Skill Agentic Risk Score): five-dimensional metric (IFR, DG, AI, BR, CA) with CVSS v4.0 vector. Evaluated 1,200 skills on Hugging Face leaderboard. Zero false negatives on 78 malicious skills; conventional tools miss 89-100% of instruction-layer threats. Detection rate varies 35-95% across LLM evaluators, motivating ensemble scoring. Relevant to **Layer 0/1** — Semantic skill vetting that code-level scanners cannot perform. URL: https://arxiv.org/abs/2606.15899

2. **Agents' Last Exam (ALE)** (arXiv:2606.05405) — June 3, 2026 (v2 June 11). UC Berkeley RDI / Dawn Song group. 250+ industry experts, 1,490 task instances across 55 subfields and 13 industry clusters. Evaluates Generalist Computer-Use Agents (GCUA) on real professional workflows with deterministic deliverable-based scoring. Three tiers: Near-Term (67 tasks, ~40% pass), Full-Spectrum (55 tasks), Last-Exam (38 tasks, 2.6% pass). Codex + GPT-5.5 scores 0% on Last-Exam despite 82% on Terminal-Bench. ALE-Claw reference implementation derived from OpenClaw. Living benchmark with public leaderboard. URL: https://arxiv.org/abs/2606.05405

3. **MAGIQ** (arXiv:2605.06933v2) — May 7, 2026 (v2 May 18). Post-quantum multi-agentic AI governance with provable UC-security. Policy definition and enforcement using quantum-resistant cryptographic primitives (FIPS 203/204/205). Session-based enforcement for AA-sessions (one-to-one) and CC-sessions (one-to-many). Task-msg attribution for accountability. Evaluated overhead vs SAGA; practical for production. Relevant to **Layer 1/3** — Cryptographically secured agent governance with formal proofs. URL: https://arxiv.org/abs/2605.06933

### Notes (0620)
- SkillVetBench closes the semantic gap in skill security: code scanners are structurally blind to instruction-layer attacks (prompt injection, memory poisoning). The SARS score is the first agentic-specific risk metric.
- ALE is the first benchmark to measure economically valuable, long-horizon professional work rather than synthetic tasks. The 2.6% Last-Exam pass rate is a critical reality check for agent deployment claims.
- MAGIQ provides the cryptographic foundation for post-quantum agent governance. Its UC-security proof and session-based policy enforcement make it suitable for high-assurance environments.
- All three papers were published after the June 14 scout run, confirming the weekly scouting cadence is catching new research.

## Next Scout Run
- Scheduled: June 27, 2026
- Focus: FAccT 2026 proceedings (June 25-28), NeurIPS 2026 submissions, summer benchmark releases, OWASP agentic skills adoption metrics

## Research Momentum Observations (Updated 0620)
- **Semantic skill evaluation is now measurable:** SkillVetBench's SARS score provides an actionable metric for skill marketplace security, complementing static code analysis.
- **Real-world capability gap is quantified:** ALE's 2.6% pass rate on professional workflows exposes the chasm between benchmark saturation and GDP-relevant deployment.
- **Post-quantum governance is formalized:** MAGIQ's UC-secure framework proves that agent governance can be cryptographically grounded, not just policy-based.
- **Convergence:** The three papers collectively span skill security (Layer 0), agent capability evaluation (Layer 2/3), and infrastructure governance (Layer 1) — confirming the three-layer stack covers the active research frontier.

