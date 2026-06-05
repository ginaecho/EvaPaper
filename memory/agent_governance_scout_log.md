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

## 2026-06-04 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent governance safety benchmark 2026, agent skill markdown specification validation governance 2026, OWASP agentic applications framework 2026, agent behavioral contracts runtime enforcement 2026, agent skill supply chain formal verification 2026
Status: **NEW FINDINGS FOUND**

### New Papers
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

### New Products/Frameworks
1. **AgentAssert** — Runtime enforcement library implementing ABC (Agent Behavioral Contracts). Detects 5.2-6.8 soft violations per session that uncontracted baselines miss. 88-100% hard constraint compliance. <10 ms overhead per action. Part of Qualixar suite. — **Layer 1** — The runtime contract enforcement mechanism we need for skill/agent behavior validation.

2. **SkillFortify (Open Source)** — pip install skillfortify. Formal verification framework for agent skill supply chains. 22 frameworks supported. SAT-based resolution, capability confinement, trust score algebra. MIT license. GitHub: https://github.com/varun369/skillfortify — **Layer 0/1** — The formal skill validation tool. Replaces heuristic scanning with mathematical guarantees.

3. **AgentAssay (Open Source)** — pip install agentassay. Token-efficient stochastic testing for AI agents. pytest integration. 8 CLI commands. 10 framework adapters. MIT license. GitHub: https://github.com/qualixar/agentassay — **Layer 2** — CI/CD regression testing for agent behavior. Ensures governance properties persist across updates.

4. **Agent Control Protocol (ACP)** — Reference implementation in Go. 38 documents, 23 packages, 138 conformance test vectors (73 signed + 65 unsigned). ACR-1.0 sequence compliance runner. Part of Agent Governance Series (6 papers). URL: https://github.com/topics/agent-control-protocol — **Layer 1** — Production-ready admission control with formal verification backing.

5. **SkillsVote** — Skills engine for AI agents. Referenced in Comprehensive Survey. — **Layer 0/1** — Skill routing and governance infrastructure.

## Key Search Queries Added
- agent behavioral contracts runtime enforcement 2026
- agent skill supply chain formal verification 2026
- agent regression testing non-deterministic workflow 2026
- machine identity governance taxonomy AI agent 2026
- admission control protocol agent actions temporal 2026
- agent harness engineering memory skills protocols 2026
- agent safety benchmark taxonomy consistency analysis 2026

## Last Check
- Date: 2026-06-04
- Status: 10 new papers + 5 new products/frameworks discovered
- Findings: Significant formal methods momentum — ABC, AgentVerify, SkillFortify, AgentAssay, ACP all provide mathematically grounded governance mechanisms. The shift from heuristic to formal guarantees is accelerating. Agent Governance Series (6 papers) by Marcelo Fernandez is a major emerging body of work.

## 2026-06-05 Scout Run — NEW FINDINGS DISCOVERED
Search queries: agent behavioral integrity verification skill 2026, agent runtime governance path policy temporal 2026, skill structure representation markdown parsing 2026, FAccT 2026 agent governance alignment pluralistic
Status: **NEW FINDINGS FOUND**

### New Papers
1. **BIV / Behavioral Integrity Verification** (arXiv:2605.11770) — May 12, 2026. Sun Yat-sen University. Verifies whether skill descriptions match actual code behavior. 80.0% deviation rate across 1,200 skills. 34.3% severe violations. URL: https://arxiv.org/abs/2605.11770 — **Layer 0** — Directly addresses "do skills do what they claim?" Essential for marketplace validation.

2. **Runtime Governance / Policies on Paths** (arXiv:2603.16586) — Mar 17, 2026. Jheronimus Academy of Data Science. Formalizes compliance policies as temporal predicates over execution paths. Path-based policies express separation of duties, data minimization, audit trails that per-step checks cannot capture. Polynomial-time evaluation. URL: https://arxiv.org/abs/2603.16586 — **Layer 1** — The missing formal foundation for temporal governance requirements.

3. **SSL Representation / Skill Text to Structure** (arXiv:2604.24026) — Apr 27, 2026. Scheduling-Structural-Logical representation for agent skills. 94% decomposition rate, 87% accuracy vs expert annotations. Machine-verifiable skill descriptions. URL: https://arxiv.org/abs/2604.24026 — **Layer 0** — Makes unstructured skill text governable by transforming into verifiable structures.

4. **FAccT '26 / Relative Principals, Pluralistic Alignment** (arXiv:2604.20805) — Apr 22, 2026. Travis LaCroix, Durham University. FAccT '26 conference paper (June 25-28). Three-axis framework: objectives, information, principals. Alignment is fundamentally governance, not engineering alone. URL: https://arxiv.org/abs/2604.20805 — **Cross-layer** — Conceptual foundation explaining why our three-layer stack is necessary.

### New Products/Frameworks
- No new products/frameworks discovered today (search focused on academic papers)

## Key Search Queries Added
- agent behavioral integrity verification skill 2026
- agent runtime governance path policy temporal 2026
- skill structure representation markdown parsing 2026
- FAccT 2026 agent governance alignment pluralistic

## Research Momentum Observations
- **Skill integrity crisis:** BIV's 80% deviation rate + ClawHavoc's 1,200+ malicious skills = current validation is completely insufficient
- **Temporal governance emergence:** Path-based policies (Runtime Governance) + ACP admission control = formal temporal reasoning is replacing per-step checks
- **Structured representation gap:** SSL's 94% decomposition rate shows automatic skill structure extraction is feasible — enabling automated governance
- **FAccT governance focus:** Three-axis framework (objectives, information, principals) validates our multi-layer approach conceptually
- **Formal methods dominance:** 4 new papers all use formal/mathematical approaches (integrity verification, temporal logic, structured decomposition, principal-agent theory) — heuristic governance is being replaced by formal guarantees

## Next Scout Run
- Scheduled: June 12, 2026
- Focus: FAccT 2026 conference proceedings (June 25-28), OWASP Top 10 adoption metrics, skill marketplace integrity implementations, ACP/AgentAssert production deployments
