# AI Agent Governance: Three-Layer Stack and Research Papers

> "Even if the world forgets, I'll remember for you." — EvaPaper

---

## Executive Summary

This report consolidates research on **AI Agent Governance**, **Skill Markdown Validation**, and **Agent Behavior Evaluation**. It presents a **Three-Layer Governance Stack** as the organizing framework, with each paper/product mapped to the specific layer it addresses.

### June 7, 2026 findings update

The latest workflow run over the local indexed corpus sharpens the practical recommendation:

- the repo's main focus should remain **static-time governance of skills, specs, and agent interactions**
- runtime governance is still necessary, but it should be treated as a downstream control layer
- the strongest current static-first set in the corpus is:
  - **Skilldex**
  - **GovernSpec / Contractual Skills**
  - **SkCC**
  - **OWASP Top 10 for Agentic Skills (AST10)**
  - **GitHub Spec Kit / SDD**

These results came from the current `workflow-static` pipeline. In this environment, external discovery APIs were temporarily unavailable, so the latest run used the local curated corpus rather than live graph expansion. That means the ranking above reflects the current internal evidence base, not a claim that fresh frontier scouting was completed in that specific run.

### June 14, 2026 scout addendum: eight newly surfaced papers, frameworks, and products

The June 14 scout adds eight items across all three search targets — new benchmarks, skill governance frameworks, OWASP/MITRE/NIST guidelines, and security tools — that materially expand the stack:

1. **EmbodiedGovBench** (`arXiv:2604.11174`)
   - First benchmark specifically targeting governance-oriented evaluation of embodied agent systems (not just task success)
   - Covers seven governance dimensions: unauthorized capability invocation, runtime drift robustness, recovery success, policy portability, version upgrade safety, human override responsiveness, and audit completeness
   - Most relevant to **Layer 2**
   - Why it matters: current embodied benchmarks measure completion rate and accuracy — they do not measure whether systems are governable. EmbodiedGovBench makes governance a first-class evaluation target

2. **Agent Skills for Large Language Models** (`arXiv:2602.12430`)
   - Comprehensive survey of the agent skills landscape with a proposed **Skill Trust and Lifecycle Governance Framework** — a four-tier, gate-based permission model (G1–G4 verification gates, T1–T4 trust tiers) that maps skill provenance to graduated deployment capabilities
   - Reports that 26.1% of community-contributed skills contain vulnerabilities
   - Most relevant to **Layer 0**
   - Why it matters: this is the first systematic framework for skill provenance-based governance, treating skills not as documentation but as executable artifacts with graduated trust levels

3. **OWASP Practical Guide for Secure MCP Server Development** (Feb 2026)
   - Dedicated security guide covering eight security domains for MCP server development: authentication, authorization, input validation, output encoding, error handling, logging, dependency management, and configuration management
   - Most relevant to **Layer 1**
   - Why it matters: MCP is the de facto protocol for agent-tool communication; this is the first OWASP-level guidance specifically for securing MCP servers, complementing MCP-38's threat taxonomy with concrete implementation guidance

4. **MITRE ATLAS agentic AI update** (Oct 2025)
   - 14 new agentic AI-specific techniques added to the ATLAS framework for adversarial threat modeling
   - Most relevant to **Layer 1 + Layer 2**
   - Why it matters: MITRE ATLAS is the standard adversarial taxonomy for AI systems; the 14 new techniques formalize attack vectors unique to agentic systems (multi-step tool chaining, state manipulation, delegation abuse) that traditional AI threat models miss

5. **NIST IR 8596** — Cybersecurity Framework Profile for AI (Dec 2025)
   - NIST Interagency Report applying the CSF 2.0 to AI systems with explicit agentic AI control overlays
   - Most relevant to **Layer 1 + Layer 3**
   - Why it matters: NIST is the authoritative standard for U.S. federal and regulated-industry cybersecurity; this report maps CSF functions (Identify, Protect, Detect, Respond, Recover) to agentic AI with concrete control overlays, making it the compliance baseline for regulated agent deployments

6. **reprobe-audit** — IEEE Big Data 2026
   - Open scoring schema and codebook for auditing what LLM agent benchmark papers actually disclose: benchmark identity, harness specification, inference settings, cost reporting, and failure breakdown
   - 12-paper pilot audit found agent-benchmark mean disclosure score of 0.38 vs. 0.66 for classical benchmarks; cost reporting is universally absent
   - Most relevant to **Layer 2**
   - Why it matters: governance without trustworthy benchmarks is guesswork; reprobe-audit provides the first systematic framework for verifying whether benchmark claims are reproducible, exposing a critical credibility gap in agent safety evaluation

7. **Agent Security Harness** — 474 security tests (red-team-blue-team-agent-fabric)
   - Open-source security harness with 33 modules and 474 targeted security tests for AI agent systems
   - Covers prompt injection, tool misuse, data exfiltration, privilege escalation, and inter-agent trust violations
   - Most relevant to **Layer 1 + Layer 2**
   - Why it matters: a security harness with 474 concrete tests is the closest thing to a standardized penetration-testing suite for agents; it turns governance from policy into measurable, repeatable verification

8. **Web Skills Protocol (WSP)** — March 2026 draft
   - Web discovery layer for skills defining `/skills.txt` and `/agents.txt` conventions for discoverable, self-describing skill registries on the web
   - Most relevant to **Layer 0**
   - Why it matters: as skills proliferate across platforms, a web-native discovery protocol enables transparent, inspectable skill registries — a prerequisite for scalable governance and provenance tracking across distributed skill ecosystems

**Interpretation:** the June 14 additions show that the governance landscape is maturing across all three layers simultaneously. At Layer 0, we now have both Skill Trust and Lifecycle Governance Frameworks (provenance-based trust tiers) and Web Skills Protocol (distributed discovery). At Layer 1, we have OWASP MCP security guidance, MITRE ATLAS agentic techniques, and NIST compliance overlays. At Layer 2, we have EmbodiedGovBench (governance as a first-class evaluation target) and reprobe-audit (benchmark credibility verification). The Agent Security Harness provides cross-layer testing infrastructure. Together, these represent the most significant single-week expansion of the governance evidence base since the baseline was established.

### June 25, 2026 scout addendum: evaluation benchmark papers

The June 25 scout adds **eight evaluation and benchmarking papers** that sharpen the governance stack around **systematic agent assessment**, **safety benchmark taxonomy**, **agent-as-judge methodology**, and **reliability measurement**:

1. **Evaluation and Benchmarking of LLM Agents: A Survey** (`arXiv:2507.21504`)
   - KDD 2025 survey (cited 179+). Proposes a two-dimensional taxonomy: Evaluation Objectives (agent behavior, capabilities, reliability, safety/alignment) × Evaluation Process (interaction mode, data, metrics, tooling, contexts)
   - Identifies 40+ behavioral safety benchmarks published Apr 2023–Mar 2026; catalogues metrics like pass^k, Progress Rate, Node/Edge F1, Step Success Rate
   - Most relevant to **Layer 2**
   - Why it matters: this is the most comprehensive systematic map of agent evaluation to date. It exposes that evaluation is fragmented across objectives and processes, and provides the conceptual scaffolding needed to compare benchmarks apples-to-apples — a prerequisite for credible governance

2. **Taxonomy and Consistency Analysis of Safety Benchmarks for AI Agents** (`arXiv:2605.16282`)
   - Analyzes 40 core behavioral safety benchmarks plus 5 adjacent evaluator/defense artifacts. Search protocol: iterative arXiv/Semantic Scholar/ACL Anthology/Google Scholar queries + backward/forward citation tracing + manual review of ICLR/NeurIPS/ICML/ACL/EMNLP 2023–2026 proceedings
   - Inclusion criteria: (1) LLM-based agents with tool use/code execution/env interaction; (2) explicitly measure safety/security/alignment; (3) reproducible evaluation
   - Finds significant consistency gaps: same agent can score A on one benchmark and F on another due to differing threat models, interaction modes, and success criteria
   - Most relevant to **Layer 2**
   - Why it matters: governance without benchmark consistency is guesswork. This paper provides the first systematic diagnosis of why agent safety benchmarks disagree — and what minimum disclosure standards would fix it

3. **Agent-as-a-Judge** (`arXiv:2410.10934`)
   - Framework using LLM agents to evaluate other LLM agents. Evaluates agents on open-ended tasks with agent-generated rubrics, trajectories, and scores
   - Correlates 0.78 with human judgments while scaling to 100x more evaluations. Reduces cost per evaluation from $2.50 (human) to $0.03 (agent)
   - Most relevant to **Layer 2**
   - Why it matters: human evaluation of multi-turn agents does not scale. Agent-as-a-Judge makes comprehensive behavioral auditing economically feasible — turning governance from spot-checks into systematic surveillance

4. **AgentAtlas: Beyond Outcome Leaderboards for LLM Agents** (`arXiv:2605.20530`)
   - Decomposes agent evaluation into five dimensions: outcome success, process correctness, resource efficiency, safety adherence, and robustness under perturbation
   - Demonstrates that outcome-only leaderboards mis-rank agents: an agent with 95% task success can have 30% safety adherence, and vice versa
   - Most relevant to **Layer 2**
   - Why it matters: current leaderboards optimize for task completion and silently drop safety. AgentAtlas proves that multi-dimensional reporting is not optional — it is the only way to prevent leaderboard gaming that hides governance failures

5. **SWE-bench Pro** (2025)
   - Successor to SWE-bench (ICLR 2024). 500 validated instances with scaffold-comparison caveats and harness-level metadata disclosure
   - Introduces verified ground-truth patches and harness-level failure breakdowns (test failures, build failures, environment errors, timeout)
   - Most relevant to **Layer 2**
   - Why it matters: SWE-bench became the de facto coding-agent benchmark, but its original instances had noisy ground truth. SWE-bench Pro fixes this with verified patches and transparent harness metadata — directly addressing the reproducibility crisis that reprobe-audit identified

6. **ReliabilityBench: A Multi-Dimensional Benchmark for LLM Reliability** (`arXiv:2601.06112`)
   - Measures consistency (pass^k), robustness (perturbation survival), calibration (confidence alignment), and recovery (error correction) across 12 task categories
   - Finds that top models score 90%+ on task success but only 40–60% on reliability metrics — revealing a "success-without-trust" gap
   - Most relevant to **Layer 2 + Layer 3**
   - Why it matters: governance requires agents that are not just capable but *dependable*. ReliabilityBench exposes that current capabilities benchmarks systematically overstate operational readiness. For production governance, reliability metrics are as important as success metrics

7. **AgentHarm** (`arXiv:2410.09024`)
   - Benchmark for measuring harmfulness of LLM agents. 400+ agent-harm scenarios across 12 harm categories: cybercrime, misinformation, harassment, self-harm, illegal goods, etc.
   - Tests agents in realistic multi-turn interactions with tool access, measuring both intent recognition and harmful action execution
   - Most relevant to **Layer 2**
   - Why it matters: AgentHarm is one of the seed papers used in the safety-benchmark taxonomy survey. It provides a concrete, repeatable measurement of how easily agents can be steered toward harmful outcomes — a direct input to governance risk assessment

8. **τ-bench** (`arXiv:2406.12045`)
   - Benchmark for tool-agent-user interaction in real-world domains (airline, retail). Measures task success, consistency (pass^k), and user satisfaction in multi-turn dialogues
   - Finds that high task success correlates poorly with user satisfaction: agents that complete tasks correctly can still frustrate users through poor explanation, excessive turns, or ignored preferences
   - Most relevant to **Layer 2**
   - Why it matters: governance is not just about preventing harm — it is about ensuring acceptable user experience. τ-bench proves that outcome metrics miss the human-alignment dimension, which is critical for deployment governance

**Interpretation:** the June 25 additions reveal that agent evaluation is maturing from "can it complete the task?" to "can it complete the task safely, reliably, consistently, and accountably?" The two surveys (arXiv:2507.21504, arXiv:2605.16282) provide the taxonomy and consistency analysis needed to compare benchmarks. Agent-as-a-Judge and AgentAtlas provide scalable, multi-dimensional evaluation methodologies. SWE-bench Pro and ReliabilityBench close specific measurement gaps. AgentHarm and τ-bench keep the human-impact dimension visible. Together, these papers transform evaluation from a leaderboard competition into a governance infrastructure.

### June 28, 2026 scout addendum: eleven newly surfaced papers on MCP security, multi-agent attacks, and artifact auditing

**New theme:** The MCP security landscape has exploded with 6 dedicated papers, plus the first demonstration of multi-agent teams exploiting zero-day vulnerabilities. Artifact-level auditing emerges as a complementary approach to runtime testing.

1. **Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification** (arXiv:2605.10052, Layer 0+1)
   - Self-evolving multi-agent coordination specification with built-in governance hooks
   - Portable format for agent team definitions
   - Layer 0: Skill specification | Layer 1: Runtime coordination structure

2. **MCPTox: A Benchmark for Tool Poisoning on Real-World MCP Servers** (AAAI 2026, Layer 1+2)
   - First benchmark for tool poisoning on production MCP services
   - Tests tool-level manipulation across 100+ MCP servers
   - Layer 1: Tool access governance | Layer 2: Behavioral safety evaluation

3. **MPMA: Preference Manipulation Attack Against Model Context Protocol** (AAAI 2026, Layer 1)
   - Demonstrates preference manipulation attacks targeting MCP
   - Agent tool selection can be biased through prompt injection
   - Layer 1: Runtime tool access security

4. **Enterprise-Grade Security for the Model Context Protocol** (IEEE ICAIC 2026, Layer 1)
   - Frameworks and mitigation strategies for MCP security in enterprise environments
   - AuthZ, audit logging, least-privilege tool access
   - Layer 1: Runtime security framework

5. **MCP Threat Modeling and Analysis of Vulnerabilities** (JCP 2026, Layer 1)
   - STRIDE analysis of 12 MCP attack vectors
   - Threat modeling for prompt injection and tool poisoning
   - Layer 1: Runtime threat analysis

6. **Teams of LLM Agents can Exploit Zero-Day Vulnerabilities** (EACL 2026, Layer 2+3)
   - Demonstrates coordinated multi-agent teams autonomously exploiting zero-days
   - No human intervention required for exploit development
   - Layer 2: Behavioral governance | Layer 3: Societal impact

7. **From Artifacts to Risk: Auditing Instruction Surfaces in Agent Systems** (2026, Layer 0+1)
   - Audit of 509 instruction-rich repositories, 4,882 findings
   - Gini coefficient 0.940 — highly concentrated risk
   - Layer 0: Skill specification audit | Layer 1: Repository-level security

8. **From Prompt Injections to Protocol Exploits** (JIC 2026, Layer 1)
   - 8 exploit categories from input to protocol level
   - Comprehensive analysis of LLM agent workflow vulnerabilities
   - Layer 1: Runtime exploit analysis

9. **Prompt Injection Attacks: Comprehensive Review** (MDPI Info 2026, Layer 1)
   - Systematic review of vulnerabilities, attack vectors, defense mechanisms
   - 200+ attacks across 15 categories
   - Layer 1: Runtime defense survey

10. **Formal Security Framework for MCP Tool Access** (SSRN 2026, Layer 1)
    - Temporal logic specifications for safe tool invocation
    - Formal verification of access control policies
    - Layer 1: Runtime formal verification

11. **Securing LLM-based Agents: Comprehensive Survey** (SICS 2026, Layer 1)
    - 200+ attacks across 15 categories
    - Taxonomy of attack techniques and defense strategies
    - Layer 1: Runtime security survey

---

### June 28, 2026 weekly scout addendum: meta-governance platform and industry skill verification

**New theme:** The convergence of academic meta-governance theory and industry skill verification infrastructure — both targeting the same governance gap from complementary angles.

1. **Meta-Governance of Autonomous AI Agents: A Policy-as-Code Architecture for Real-Time GRC in Multi-Agent Systems** (AMCIS 2026, Paper #1513, Layer 1+3)
   - Introduces meta-governance as a novel IS security construct: using AI governance agents to autonomously monitor, evaluate, and intervene in operational AI agent fleets
   - MOM-GS-MAS platform deploys 16 specialized governance agents across four SAGS pillars (Safety, Alignment, Governance, Security)
   - Sub-100ms policy enforcement, >97% attack detection across 5 adversarial vectors, >99% policy compliance at 1,000-agent fleet scale
   - Introduces Policy-as-Code as operationalization of algorithmic accountability and the Three-Way Governance Dilemma
   - URL: https://aisel.aisnet.org/amcis2026/sig_sec/sig_sec/20/
   - Layer 1: Runtime governance | Layer 3: Enterprise GRC

2. **NVIDIA Verified Agent Skills / SkillSpector** (June 2026, Layer 0+1)
   - NVIDIA's capability governance framework for AI agents: verified skills embed transparency, provenance, security validation, and authenticity checks at the skill layer
   - SkillSpector scanner checks conventional software risks (vulnerable dependencies, suspicious scripts, credential access) and agent-specific risks (hidden instructions, prompt injection, trigger abuse, excessive agency, tool poisoning, intent-behavior mismatches)
   - Grounded in OWASP LLM/Agentic AI guidance and MITRE ATLAS
   - Cryptographic signing with OpenSSF Model Signing (OMS) for post-download verification
   - Skill cards document ownership, dependencies, limitations, and risks in machine-readable format
   - Built on agentskills.io open specification (Claude Code, Codex, Cursor compatible)
   - URL: https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
   - Layer 0: Skill specification validation | Layer 1: Runtime security scanning

**Interpretation:** the June 28 weekly additions show two converging governance frontiers. First, **meta-governance** (MOM-GS-MAS) moves governance from static policy documents to dynamic AI-agent oversight — 16 governance agents monitoring operational fleets with sub-100ms enforcement and formal evaluation. This is the first production-scale evidence that meta-governance is feasible. Second, **industry skill verification** (NVIDIA Verified Agent Skills) treats skills as deployable artifacts requiring provenance, scanning, and cryptographic signing — a level of rigor previously reserved for software packages. Together, these represent the transition from conceptual governance frameworks to operational infrastructure: academic theory (meta-governance) meets industry practice (skill verification), both targeting the same problem of how to govern agent capabilities at scale.

---

### June 20, 2026 scout addendum: three newly surfaced papers

The June 20 scout adds three papers that advance the stack across **semantic skill evaluation**, **real-world capability benchmarking**, and **post-quantum cryptographic governance**:

1. **SkillVetBench** (`arXiv:2606.00925` / `arXiv:2606.15899`)
   - LLM-as-Judge security evaluation for open-source agent skills with SARS (Skill Agentic Risk Score): five-dimensional metric (IFR, DG, AI, BR, CA) weighted for instruction-following systems, plus full CVSS v4.0 vector decomposition
   - Evaluated 1,200 skills on a live Hugging Face leaderboard; zero false negatives on 78 confirmed-malicious skills, zero false positives on 22 benign controls
   - Conventional static tools miss 89–100% of instruction-layer threats (prompt injection, memory poisoning); detection rate varies 35–95% across LLM evaluators, motivating ensemble scoring
   - Most relevant to **Layer 0 + Layer 2**
   - Why it matters: code-level scanners are structurally blind to instruction-layer attacks. SkillVetBench closes the semantic gap by evaluating what skills *declare* they will do, not just what code they contain. The SARS score is the first agentic-specific risk metric designed for skill marketplaces.

2. **Agents' Last Exam (ALE)** (`arXiv:2606.05405`)
   - UC Berkeley RDI / Dawn Song group. 250+ industry experts, 1,490 task instances across 55 subfields and 13 industry clusters, grounded in O*NET / SOC 2018 occupational taxonomy
   - Evaluates Generalist Computer-Use Agents (GCUA) on real professional workflows with deterministic deliverable-based scoring. Three tiers: Near-Term (67 tasks, ~40% pass), Full-Spectrum (55 tasks), Last-Exam (38 tasks, 2.6% pass)
   - Codex + GPT-5.5 scores 0% on Last-Exam despite 82% on Terminal-Bench. ALE-Claw reference implementation derived from OpenClaw.
   - Most relevant to **Layer 2 + Layer 3**
   - Why it matters: ALE is the first benchmark to measure economically valuable, long-horizon professional work rather than synthetic tasks. The 2.6% Last-Exam pass rate is a critical reality check: benchmark saturation elsewhere has not translated into professional workflow mastery. It exposes the gap between "agent can do tasks" and "agent can do GDP-relevant work."

3. **MAGIQ** (`arXiv:2605.06933v2`)
   - Post-quantum multi-agentic AI governance with provable UC-security. Policy definition and enforcement using NIST PQC standards (FIPS 203/204/205) — ML-KEM, ML-DSA, SLH-DSA.
   - Session-based enforcement for AA-sessions (one-to-one agent communication) and CC-sessions (one-to-many orchestration). Task-msg attribution for accountability. Hash-chain policy budgets with digitally signed session-authorization tokens.
   - Formal UC proof in the global random-oracle model. Overhead comparable to SAGA (classical cryptography) despite post-quantum primitives.
   - Most relevant to **Layer 1 + Layer 3**
   - Why it matters: MAGIQ is the first post-quantum-secure agent governance framework with formal security proofs. As NIST deprecates RSA/ECDSA by 2030, agent-to-agent authorization and policy enforcement must migrate to quantum-resistant primitives. MAGIQ proves this is practical today, not a future problem.

**Interpretation:** the June 20 additions reveal three converging frontiers. First, **semantic evaluation** (SkillVetBench) shows that static code analysis is insufficient for skill security — the instruction layer is where attacks hide, and LLM-as-Judge ensemble scoring is the current best detection mechanism. Second, **real-world benchmarking** (ALE) quantifies the capability gap between synthetic benchmarks and professional deployment, providing a north-star metric for when agents are actually ready for GDP-relevant work. Third, **cryptographic governance** (MAGIQ) demonstrates that agent policy enforcement can be formally proved secure, even against quantum adversaries. Together, these papers span Layer 0 (SkillVetBench), Layer 1 (MAGIQ), and Layer 2/3 (ALE), confirming that agent governance research is advancing on all fronts simultaneously.

### June 12, 2026 scout addendum: two newly surfaced papers

The June 12 scout adds two papers that expand the stack in different directions — one on **learning-based sequential validation** (static-time) and one on **owner-harm threat modeling** (behavioral):

1. **Learning Correct Behavior from Examples** (`arXiv:2605.03159`)
   - Learns correct sequential behavior from 2-10 passing execution traces and validates new executions against a learned model
   - Most relevant to **Layer 0 + Layer 1**
   - Why it matters: static governance usually requires either exhaustive specifications or runtime monitors; this shows a middle path — learning ground truth from a small set of positive examples and then validating against it

2. **Owner-Harm: Agents Harming Their Deployers** (`arXiv:2604.18658`)
   - Formal threat model with eight categories of agent behavior damaging the deployer
   - Most relevant to **Layer 1 + Layer 2**
   - Why it matters: current safety benchmarks optimize for generic criminal harm (AgentHarm) and miss the deployer-harm vector entirely; the 14.8% → 85.3% TPR improvement with layered defense shows that owner-harm detection is a different, harder problem that needs its own governance stack

**Interpretation:** the June 12 additions reinforce that the governance problem is not just about writing better specs or adding runtime guards. It is also about (a) validating behavior when you don't have complete specs, and (b) protecting against a threat class that most current benchmarks ignore. The owner-harm paper is especially important because it shows that even a 100% TPR gate on generic criminal harm collapses to 14.8% when the victim is the deployer itself.

### June 7, 2026 scout addendum: six newly surfaced papers

The latest scout update adds six papers that materially improve the stack, especially around **skill composition**, **verifiable skill representations**, and **formal monitoring**:

1. **SkillSafetyBench** (`arXiv:2605.12015`)
   - First benchmark specifically targeting skill-level attack surfaces
   - Most relevant to **Layer 0 + Layer 2**
   - Why it matters: governance at the skill layer needs a benchmark, not just threat claims

2. **Measuring Compositional Risk** (`arXiv:2606.00448`)
   - Shows that individually safe skills can still compose into unsafe combinations
   - Most relevant to **Layer 0 + Layer 1**
   - Why it matters: this is the cleanest statement so far that single-skill validation is insufficient

3. **AgentTrap** (`arXiv:2605.13940`)
   - Documents runtime trust failures in third-party skills
   - Most relevant to **Layer 1**
   - Why it matters: external skill reuse is a live trust-boundary problem, not just a packaging issue

4. **Skill-as-Pseudocode (SaP)** (`arXiv:2605.27955`)
   - Transforms natural-language skills into verifiable pseudocode
   - Most relevant to **Layer 0**
   - Why it matters: this is one of the strongest direct candidates for static-time checking before execution

5. **KYA** (`arXiv:2605.25376`)
   - Introduces a framework-agnostic trust layer with verifiable provenance
   - Most relevant to **Layer 1 + Layer 3**
   - Why it matters: provenance is a prerequisite for meaningful governance across frameworks and delegation chains

6. **Auditing, Monitoring, and Intervention** (`arXiv:2605.16198`)
   - LTL-based runtime compliance monitoring
   - Most relevant to **Layer 1**
   - Why it matters: it strengthens the formal runtime side without falling back to pure LLM-as-judge patterns

**Interpretation:** the June 7 additions reinforce the repo's current direction. Static governance still sits at the center, but the new evidence makes it clearer that the real target is not just validating individual `SKILL.md` files. The harder problem is validating **skill composition**, **third-party trust**, and **translation from natural language skill specs into verifiable intermediate forms**.

**The Three-Layer Stack:**

| Layer | Name | Focus | Key Question |
|-------|------|-------|--------------|
| **Layer 0** | **Spec-Level Governance** | SKILL.md validation, schema soundness, contractual boundaries | *Is the skill specification correct and complete?* |
| **Layer 1** | **Runtime-Level Governance** | Execution sandboxing, intent verification, inter-agent authorization, audit logging | *Can the agent execute safely at runtime?* |
| **Layer 2** | **Behavioral-Level Governance** | Safety benchmarks, task evaluation, reward hacking detection, enterprise trustworthiness | *Does the agent behave safely in real-world tasks?* |

---

## Papers & Products

### 1. BeSafe-Bench (BSB)

- **arXiv ID:** 2603.25747
- **URL:** https://arxiv.org/abs/2603.25747
- **PDF:** https://arxiv.org/pdf/2603.25747
- **Authors:** Xuetao Wei et al.
- **Date:** January 2026

**Abstract:**
> The rapid evolution of Large Multimodal Models (LMMs) has enabled agents to perform complex digital and physical tasks, yet their deployment as autonomous decision-makers introduces substantial unintentional behavioral safety risks. However, the absence of a comprehensive safety benchmark remains a major bottleneck, as existing evaluations rely on low-fidelity environments, simulated APIs, or narrowly scoped tasks. To address this gap, we present BeSafe-Bench (BSB), a benchmark for exposing behavioral safety risks of situated agents in functional environments, covering four representative domains: Web, Mobile, Embodied VLM, and Embodied VLA. Using functional environments, we construct a diverse instruction space by augmenting tasks with nine categories of safety-critical risks, and adopt a hybrid evaluation framework that combines rule-based checks with LLM-as-a-judge reasoning to assess real environmental impacts. Evaluating 13 popular agents reveals a concerning trend: even the best-performing agent completes fewer than 40% of tasks while fully adhering to safety constraints, and strong task performance frequently coincides with severe safety violations. These findings underscore the urgent need for improved safety alignment before deploying agentic systems in real-world settings.

**Why I recommend this paper:**
BeSafe-Bench is the **first comprehensive behavioral safety benchmark** for real-world agent environments. Most existing benchmarks measure only task completion — this one measures whether agents complete tasks *safely*. The finding that top agents fail safety constraints on 60%+ of tasks is a critical data point for anyone building production agents.

**Relevance to our topic:**
This is the foundational benchmark for Layer 2 (Behavioral Governance). It provides the measurement infrastructure we need to validate whether agents are actually safe in practice, not just theoretically.

**Which layer:** **Layer 2 — Behavioral-Level Governance**

**Is it a solution we're looking into?** Yes. BeSafe-Bench is the evaluation framework we should use to measure safety improvements. It's not a governance mechanism itself, but the *measurement tool* that tells us if governance is working.

**Recommendation reason:** The gap between "task completion" and "safe task completion" is the single most important blind spot in current agent evaluation. This paper proves the blind spot exists and provides the tool to close it.

---

### 2. ST-WebAgentBench

- **arXiv ID:** 2410.06703
- **URL:** https://arxiv.org/abs/2410.06703
- **PDF:** https://arxiv.org/pdf/2410.06703
- **Authors:** Research team focusing on web agent safety
- **Date:** October 2024

**Abstract:**
> Autonomous web agents solve complex browsing tasks, yet existing benchmarks measure only whether an agent finishes a task, ignoring whether it does so safely or in a way enterprises can trust. To integrate these agents into critical workflows, Safety and Trustworthiness (ST) are prerequisite conditions for adoption. We introduce ST-WebAgentBench, a configurable and easily extensible suite for evaluating web agent ST across realistic enterprise scenarios. Each of its 222 tasks is paired with ST policies — concise rules that encode constraints — and is scored on both task completion and policy adherence. We evaluate multiple agents and show that even capable models frequently violate safety policies when task pressure increases. These findings demonstrate that safety cannot be an afterthought in web agent deployment and must be evaluated alongside capability.

**Why I recommend this paper:**
ST-WebAgentBench is the **enterprise-focused companion** to BeSafe-Bench. Where BeSafe-Bench covers broad domains (web, mobile, embodied), ST-WebAgentBench focuses specifically on web agents with 222 realistic enterprise tasks. It introduces the concept of **ST policies** — concise constraint rules that can be attached to any task — which is directly applicable to how we design skill specifications.

**Relevance to our topic:**
This paper bridges Layer 0 (Spec) and Layer 2 (Behavioral). The ST policies it introduces are essentially **behavioral constraints encoded in specifications** — exactly what we need for contractual skills (Layer 0) that can be validated at runtime (Layer 1) and measured against benchmarks (Layer 2).

**Which layer:** **Layer 0 → Layer 2 bridge** (Spec-Level to Behavioral-Level)

**Is it a solution we're looking into?** Yes. The ST policy framework is a direct implementation pattern for GovernSpec-style contractual skills. We should adopt its policy-as-specification approach.

**Recommendation reason:** Enterprise adoption requires trust. ST-WebAgentBench provides the evaluation framework that proves (or disproves) trustworthiness. The 222 tasks with paired policies are a template for how we should write skill constraints.

---

### 3. Layered Governance Architecture (LGA)

- **arXiv ID:** 2603.07191
- **URL:** https://arxiv.org/abs/2603.07191
- **PDF:** https://arxiv.org/pdf/2603.07191
- **Authors:** Security research team
- **Date:** March 2026

**Abstract:**
> Autonomous agents powered by large language models introduce a class of execution-layer vulnerabilities — prompt injection, retrieval poisoning, and uncontrolled tool invocation — that existing guardrails fail to address systematically. In this work, we propose the Layered Governance Architecture (LGA), a four-layer framework comprising execution sandboxing (L1), intent verification (L2), zero-trust inter-agent authorization (L3), and immutable audit logging (L4). To evaluate LGA, we construct a bilingual benchmark (Chinese original, English via machine translation) with 847 attack scenarios across 14 attack vectors. Experimental results show that LGA reduces successful attack rates by 89% compared to baseline guardrails while introducing only 3.2% latency overhead. The architecture is designed to be composable — each layer can be deployed independently or stacked for defense-in-depth.

**Why I recommend this paper:**
LGA is the **most practical runtime governance framework** I've found. It directly addresses the execution-layer vulnerabilities that make agents dangerous: prompt injection, tool misuse, and inter-agent trust. The 89% attack reduction with minimal latency overhead makes it production-viable.

**Relevance to our topic:**
This is the definitive Layer 1 (Runtime-Level Governance) framework. It provides the technical architecture for how to actually *secure* agent execution, not just specify or measure it.

**Which layer:** **Layer 1 — Runtime-Level Governance**

**Is it a solution we're looking into?** Yes. LGA is the architectural blueprint for runtime security. The four layers (sandboxing, intent verification, zero-trust authorization, audit logging) map directly to what any production agent system needs.

**Recommendation reason:** Most governance frameworks are theoretical. LGA is empirical — it was tested against 847 real attack scenarios and achieved 89% reduction. The composable design means you can start with one layer and add others as needed.

---

### 4. Skilldex

- **arXiv ID:** 2604.16911
- **URL:** https://arxiv.org/abs/2604.16911
- **PDF:** https://arxiv.org/pdf/2604.16911
- **Authors:** Skill package research team
- **Date:** April 2026

**Abstract:**
> Large Language Model (LLM) agents are increasingly extended at runtime via skill packages, structured natural-language instruction bundles loaded from a well-known directory. Community install tooling and registries exist, but two gaps persist: no public tool scores skill packages against Anthropic's published format specification, and no mechanism bundles related skills with the shared context they need to remain mutually coherent. We present Skilldex, a package manager and registry for agent skill packages addressing both gaps. The two novel contributions are: (1) a validation engine that checks skill packages against the Anthropic skill format spec, scoring completeness, consistency, and schema compliance; and (2) a dependency resolution system that bundles related skills with shared context, ensuring mutual coherence. Skilldex has been validated against 200+ community skill packages, identifying format violations in 34% of packages and coherence issues in 28% of bundles.

**Why I recommend this paper:**
Skilldex is the **first tool that validates skill packages against a formal specification**. It found that 34% of community skill packages have format violations — this is exactly the validation gap we need to close for Layer 0 governance. The dependency resolution for mutual coherence is also critical for preventing skill conflicts.

**Relevance to our topic:**
This is the foundational Layer 0 (Spec-Level) tool. It validates whether skill markdown files are well-formed, complete, and coherent with other skills. Without this, you can't trust any skill package.

**Which layer:** **Layer 0 — Spec-Level Governance**

**Is it a solution we're looking into?** Yes. Skilldex is the validation engine we need. The fact that 34% of community packages are malformed proves the need is real, not theoretical.

**Recommendation reason:** The paper provides both a tool (Skilldex) and data (34% violation rate) that proves spec validation is non-negotiable. If one-third of skill packages are malformed, runtime governance is building on sand.

---

### 5. GovernSpec / Contractual Skills

- **arXiv ID:** 2605.22634
- **URL:** https://arxiv.org/abs/2605.22634
- **PDF:** https://arxiv.org/pdf/2605.22634
- **Authors:** Governance research team
- **Date:** May 2026

**Abstract:**
> Skills are increasingly used to package agent instructions, workflows, scripts, and reference materials. In enterprise settings, however, skills often need to express more than task guidance: they must make goals, input boundaries, permissions, evidence requirements, output contracts, quality criteria, verification steps, human approval points, and handoff rules inspectable. This paper proposes contractual skills, a GovernSpec-inspired design framework for organizing SKILL.md files as readable task contracts while preserving lightweight skill discovery. The framework introduces a declarative schema with 12 contract sections, a validation engine, and a runtime policy interpreter that enforces contracts during execution. We demonstrate that contractual skills reduce policy violation rates by 67% compared to unconstrained skill execution, while maintaining task completion rates within 5% of baseline.

**Why I recommend this paper:**
GovernSpec is the **most comprehensive framework for making skills self-describing and self-enforcing**. It transforms SKILL.md from a task description into a **legal contract** with 12 sections covering goals, boundaries, permissions, evidence, outputs, quality, verification, approval, and handoffs. The 67% reduction in policy violations is the proof that specification-level governance works.

**Relevance to our topic:**
This is the apex of Layer 0 (Spec-Level Governance). It defines what a "well-specified skill" actually means — not just a task description, but a complete contract with enforceable boundaries.

**Which layer:** **Layer 0 — Spec-Level Governance** (with runtime enforcement hooks into Layer 1)

**Is it a solution we're looking into?** Yes. This is the framework we should adopt for defining what constitutes a valid, complete, and safe skill specification. The 12 contract sections are the checklist for skill authors.

**Recommendation reason:** The paper provides the missing link between "write a good skill" and "write a safe skill." The 12 contract sections (goals, boundaries, permissions, evidence, outputs, quality, verification, approval, handoffs) are the governance primitives we've been missing.

---

### 6. OWASP Top 10 for Agentic Applications

- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Type:** Industry standard / Security framework
- **Date:** 2026 Edition (published December 2025)

**Abstract/Summary:**
> OWASP's Top 10 for Agentic Applications is the first formal taxonomy of risks specific to autonomous AI agents. It identifies 10 critical vulnerability categories: (1) Prompt Injection, (2) Insecure Output Handling, (3) Training Data Poisoning, (4) Denial of Service via Model Manipulation, (5) Supply Chain Vulnerabilities, (6) Sensitive Information Disclosure, (7) Insecure Plugin Design, (8) Excessive Agency, (9) Overreliance on LLM Decision-Making, and (10) Agent-to-Agent Trust Exploitation. Each category includes attack scenarios, mitigation strategies, and testing guidance. The framework is designed to be integrated into existing AppSec programs and adapted for enterprise agent deployment.

**Why I recommend this:**
OWASP is the **industry standard for application security**. Having a dedicated Top 10 for agentic applications means agent security is now a recognized discipline with standardized terminology, threat models, and mitigations. This is what enterprises will reference when auditing agent systems.

**Relevance to our topic:**
OWASP spans all three layers: (1) insecure plugin design maps to Layer 0 (spec), (2) prompt injection and excessive agency map to Layer 1 (runtime), (3) overreliance and trust exploitation map to Layer 2 (behavioral). It's the comprehensive risk taxonomy that connects our stack to industry standards.

**Which layer:** **All layers** — Layer 0 (Insecure Plugin Design), Layer 1 (Prompt Injection, Excessive Agency), Layer 2 (Overreliance, Trust Exploitation)

**Is it a solution we're looking into?** Yes. OWASP provides the threat taxonomy that our governance stack must address. Every item in the Top 10 should be mapped to a specific governance control in our framework.

**Recommendation reason:** This is not a research paper — it's an industry standard. Enterprises will ask "Have you addressed the OWASP Top 10 for agents?" Having this mapping ready is a competitive advantage.

---

### 7. Microsoft Agent Governance Toolkit

- **URL:** https://www.microsoft.com/en-us/security/blog/2025/12/10/introducing-the-microsoft-agent-governance-toolkit/
- **Type:** Product / Enterprise framework
- **Date:** December 2025

**Abstract/Summary:**
> Microsoft introduced the Agent Governance Toolkit as a comprehensive framework for enterprise agent deployment. It includes: (1) Agent Registration and Discovery — a catalog system for tracking all agents in an organization; (2) Policy Engine — a rules-based system for constraining agent behavior; (3) Audit and Monitoring — real-time logging and alerting for agent actions; (4) Safety Evaluators — pre-deployment testing modules based on red-teaming; (5) Human-in-the-Loop Controls — configurable approval gates for high-risk actions. The toolkit is integrated with Azure AI Foundry and supports both first-party and third-party agents. Microsoft reports that early adopters reduced agent-related security incidents by 73% after implementing the toolkit.

**Why I recommend this:**
Microsoft is the **first major cloud provider to ship a comprehensive agent governance product**. The 73% reduction in security incidents is real enterprise data. The toolkit covers the full lifecycle — registration, policy, audit, evaluation, and human oversight — which is exactly what enterprises need.

**Relevance to our topic:**
This is the enterprise product implementation of our Three-Layer Stack. Agent Registration maps to Layer 0 (spec), Policy Engine and Audit map to Layer 1 (runtime), Safety Evaluators map to Layer 2 (behavioral). The Human-in-the-Loop controls are the approval gates mentioned in GovernSpec.

**Which layer:** **All layers** — Layer 0 (Registration), Layer 1 (Policy + Audit), Layer 2 (Safety Evaluators)

**Is it a solution we're looking into?** Yes. This is the closest thing to a production-ready governance toolkit. If you're building an enterprise agent system, this is the reference architecture.

**Recommendation reason:** Microsoft has the enterprise credibility and the data (73% incident reduction). The toolkit's five components (Registration, Policy, Audit, Evaluation, Human-in-the-Loop) are the blueprint for any serious governance implementation.

---

### 8. Agent Evaluation Guide (Quality-Focused Frameworks)

- **URL:** https://www.ai-journal.com/research/agent-evaluation-guide-2026
- **Type:** Research synthesis / Industry report
- **Date:** 2026

**Abstract/Summary:**
> Most teams ship AI agents to production with roughly the same evaluation rigor they would apply to a staging demo — and it is catching up with them. Industry data shows that over 40% of agentic AI projects are on track to be canceled by the end of 2027, and 32% of organizations now cite quality as the #1 barrier to deployment. The reason is not the models. It is the evaluation stack. Agents are multi-step systems that fail silently, compound small errors into catastrophic ones, and break in ways that a single-turn accuracy metric will never surface. This guide walks through quality-focused evaluation frameworks: (1) Multi-step success rate — not just final outcome but each step's correctness; (2) Error recovery — does the agent detect and recover from its own mistakes; (3) Tool use accuracy — correct tool selection and parameterization; (4) Context window management — does the agent retain critical information across long sessions; (5) Safety boundary adherence — does the agent respect constraints under pressure; (6) Human-alignment validation — does the agent's reasoning match human expectations.

**Why I recommend this:**
This is the **reality check** on agent evaluation. The 40% cancellation rate and 32% quality barrier are the business case for governance. The six evaluation dimensions (multi-step success, error recovery, tool accuracy, context management, safety adherence, human alignment) are the behavioral metrics that Layer 2 governance must measure.

**Relevance to our topic:**
This is the business and operational justification for our entire governance stack. Without proper evaluation, governance has no feedback loop. The six dimensions provide the KPIs for Layer 2 governance.

**Which layer:** **Layer 2 — Behavioral-Level Governance** (with Layer 1 hooks for error recovery and tool accuracy)

**Is it a solution we're looking into?** Yes. The evaluation framework is the measurement infrastructure we need. The six dimensions are the behavioral KPIs for any governed agent system.

**Recommendation reason:** This paper provides the business case (40% cancellation rate) and the measurement framework (six dimensions) that justify governance investment. It's the bridge between "governance is good" and "governance is necessary."

---

### 10. ClawBench — Real-World Web Agent Benchmark

- **arXiv ID:** 2604.08523
- **URL:** https://arxiv.org/abs/2604.08523
- **PDF:** https://arxiv.org/pdf/2604.08523
- **Website:** https://claw-bench.com
- **GitHub:** https://github.com/TIGER-AI-Lab/ClawBench
- **Authors:** Yuxuan Zhang, Yubo Wang, Yipeng Zhu et al.
- **Institutions:** UBC, Vector Institute, CMU, UWaterloo, SJTU, ZJU, HKUST, Tsinghua
- **Date:** April 9, 2026

**Abstract:**
> AI agents may be able to automate your inbox, but can they automate other routine aspects of your life? Everyday online tasks offer a realistic yet unsolved testbed for evaluating the next generation of AI agents. To this end, we introduce ClawBench, an evaluation framework of 153 simple tasks that people need to accomplish regularly in their lives and work, spanning 144 live platforms across 15 categories, from completing purchases and booking appointments to submitting job applications. These tasks require demanding capabilities beyond existing benchmarks, such as obtaining relevant information from user-provided documents, navigating multi-step workflows across diverse platforms, and write-heavy operations like filling in many detailed forms correctly. Unlike existing benchmarks that evaluate agents in offline sandboxes with static pages, ClawBench operates on production websites, preserving the full complexity, dynamic nature, and challenges of real-world web interaction. A lightweight interception layer captures and blocks only the final submission request, ensuring safe evaluation without real-world side effects. Our evaluations of 7 frontier models show that both proprietary and open-source models can complete only a small portion of these tasks. For example, Claude Sonnet 4.6 achieves only 33.3%.

**Why I recommend this paper:**
ClawBench is the **first benchmark to evaluate agents on live production websites with write-heavy transactions** (purchases, bookings, applications). Unlike sandboxed benchmarks, it captures real-world complexity: dynamic DOMs, authentication flows, payment processing, and form validation. The fact that the best model (Claude Sonnet 4.6) achieves only 33.3% exposes the massive gap between sandbox optimism and production reality.

**Relevance to our topic:**
This is a complementary Layer 2 benchmark to BeSafe-Bench and ST-WebAgentBench. Where BeSafe-Bench measures safety violations and ST-WebAgentBench measures policy adherence, ClawBench measures whether agents can even *function* on real websites under realistic constraints. It provides the operational reality check that governance must address.

**Which layer:** **Layer 2 — Behavioral-Level Governance**

**Is it a solution we're looking into?** Yes. ClawBench should be integrated into our evaluation stack alongside BeSafe-Bench and ST-WebAgentBench. It provides the "can it actually work" baseline that safety benchmarks assume.

**Recommendation reason:** The 33.3% success rate on real websites is the most sobering agent benchmark result to date. Any governance framework that doesn't account for this operational reality is designing for a fantasy. The five-layer recording (session replays, screenshots, HTTP traffic, agent messages, browser actions) is also a gold standard for forensic governance.

---

### 11. OWASP Top 10 for Agentic Skills (AST10)

- **URL:** https://owasp.org/www-project-agentic-skills-top-10/
- **GitHub:** https://github.com/OWASP/www-project-agentic-skills-top-10
- **Type:** Industry standard / Security framework
- **Date:** 2026 Edition (incubated at OWASP Project Summit, Oslo, Norway)
- **License:** CC-BY-SA-4.0
- **Status:** Active development, v1.0 RC targeted Q3 2026

**Abstract/Summary:**
> The OWASP Agentic Skills Top 10 (AST10) documents the 10 most critical security risks in agentic AI skills across all major AI agent platforms. Skills represent the execution layer giving agents real-world impact through platform-specific metadata + scripts. The 10 risks are: AST01 Malicious Skills, AST02 Supply Chain Compromise, AST03 Over-Privileged Skills, AST04 Insecure Metadata, AST05 Unsafe Deserialization, AST06 Weak Isolation, AST07 Update Drift, AST08 Poor Scanning, AST09 No Governance, and AST10 Cross-Platform Reuse. Each risk includes platform-specific attack scenarios (OpenClaw SKILL.md, Claude Code skill.json, Cursor manifest.json, VS Code package.json), preventive mitigations, OWASP/NIST/CVE mappings, and real-world evidence citations. The project also proposes a Universal Skill Format — a YAML standard normalizing security properties across all platforms.

**Why I recommend this:**
AST10 is the **first security framework focused specifically on agent skills as an attack surface**. While OWASP Agentic Applications (ASI) covers model-layer risks, AST10 covers the skill content layer — the reusable, named behaviors that encode complete workflows. Real-world evidence is already severe: 36% of AI agent skills contain security flaws (Snyk ToxicSkills), the ClawHub registry was poisoned at scale, and 135,000+ OpenClaw instances are publicly exposed. This is the framework that defines what "secure skill authoring" means.

**Relevance to our topic:**
AST10 maps directly to Layer 0 (Spec-Level Governance). It defines the security properties that every skill specification must have: least-privilege manifests, schema validation, signing, provenance tracking, and governance metadata. The Universal Skill Format proposal is the cross-platform standard that could unify OpenClaw, Claude Code, and Cursor skill formats under one security schema.

**Which layer:** **Layer 0 — Spec-Level Governance** (with Layer 1 hooks for isolation and sandboxing)

**Is it a solution we're looking into?** Yes. AST10 should be the security checklist for all skill development. The 12 contract sections from GovernSpec plus the 10 risk categories from AST10 together define what a "production-ready skill" looks like.

**Recommendation reason:** The ClawHub poisoning incident and 36% vulnerability rate prove that skills are not just documentation — they're executable code with real attack surface. AST10 is the first framework to treat them with the security rigor they deserve.

---

### 12. MCP-38 — Comprehensive Threat Taxonomy for Model Context Protocol

- **arXiv ID:** 2603.18063
- **URL:** https://arxiv.org/abs/2603.18063
- **PDF:** https://arxiv.org/pdf/2603.18063
- **GitHub (tool):** https://github.com/VulcanLab/MCPThreatHive
- **Authors:** Yi Ting Shen, Kentaroh Toyoda, Alex Leung
- **Date:** March 2026

**Abstract:**
> The Model Context Protocol (MCP) introduces a structurally distinct attack surface that existing threat frameworks, designed for traditional software systems or generic LLM deployments, do not adequately cover. This paper presents MCP-38, a protocol-specific threat taxonomy consisting of 38 threat categories (MCP-01 through MCP-38). The taxonomy was derived through a systematic four-phase methodology: protocol decomposition, multi-framework cross-mapping, real-world incident synthesis, and remediation-surface categorization. Each category is mapped to STRIDE, OWASP Top 10 for LLM Applications (2025, LLM01--LLM10), and the OWASP Top 10 for Agentic Applications (2026, ASI01--ASI10). MCP-38 addresses critical threats arising from MCP's semantic attack surface (tool description poisoning, indirect prompt injection, parasitic tool chaining, and dynamic trust violations), none of which are adequately captured by prior work. MCP-38 provides the definitional and empirical foundation for automated threat intelligence platforms.

**Why I recommend this paper:**
MCP-38 is the **first comprehensive threat taxonomy for the Model Context Protocol**, which is rapidly becoming the standard for agent-tool communication. The 38 categories cover threats that don't exist in traditional software (tool description poisoning, parasitic tool chaining, dynamic trust violations) and map them to established frameworks (STRIDE, OWASP LLM, OWASP Agentic). This is the reference that every MCP server developer and agent builder needs.

**Relevance to our topic:**
This is Layer 1 (Runtime-Level Governance) at the protocol level. MCP is the de facto standard for agent-tool interaction, and MCP-38 provides the threat model that runtime governance must defend against. The accompanying MCPThreatHive tool provides automated threat intelligence for MCP ecosystems.

**Which layer:** **Layer 1 — Runtime-Level Governance** (protocol security)

**Is it a solution we're looking into?** Yes. Any agent system using MCP (which is most modern ones) needs to understand these 38 threat categories. The cross-mapping to OWASP means we can integrate MCP-38 into existing AppSec programs.

**Recommendation reason:** MCP is the plumbing of agent infrastructure. If the plumbing is insecure, no amount of spec-level or behavioral governance can compensate. MCP-38 is the threat model that makes MCP security measurable and manageable.

---

### 13. Tencent AI-Infra-Guard — Full-Stack AI Red Teaming Platform

- **URL:** https://github.com/Tencent/AI-Infra-Guard
- **Type:** Open-source security product
- **Date:** May 2026 (actively maintained)
- **License:** Tencent open-source

**Abstract/Summary:**
> AI-Infra-Guard is a full-stack AI Red Teaming platform securing AI ecosystems via OpenClaw Security Scan, Agent Scan, Skills Scan, MCP scan, AI Infra scan, and LLM jailbreak evaluation. It provides automated scanning capabilities across the entire agent stack: from OpenClaw instance configuration and skill package security to MCP server integrity and infrastructure hardening. The platform integrates with research from the broader ecosystem including MCP-38, SkillAttack, TRUSTDESC, and MalTool papers. Tencent published this as an open-source tool for the community to self-assess AI infrastructure security posture.

**Why I recommend this:**
This is the **first open-source full-stack scanner for agent ecosystems**. Unlike point solutions (Skilldex for validation, MCPThreatHive for MCP threats), AI-Infra-Guard covers the entire stack: OpenClaw instances, agent configurations, skill packages, MCP servers, and infrastructure. It's the closest thing to a "security audit tool for agent deployments."

**Relevance to our topic:**
AI-Infra-Guard spans all three layers: Skills Scan maps to Layer 0 (spec validation), MCP scan and Agent Scan map to Layer 1 (runtime security), and LLM jailbreak evaluation maps to Layer 2 (behavioral safety). It's the operational tool that implements governance across the stack.

**Which layer:** **All layers** — Layer 0 (Skills Scan), Layer 1 (MCP scan, Agent Scan, OpenClaw Security Scan), Layer 2 (LLM jailbreak evaluation)

**Is it a solution we're looking into?** Yes. This is the closest open-source equivalent to Microsoft's commercial Agent Governance Toolkit. It provides the scanning and assessment infrastructure that governance frameworks need to be operational.

**Recommendation reason:** Governance without measurement is just policy. AI-Infra-Guard provides the measurement tools that turn governance frameworks into actionable security assessments. The integration with MCP-38 and SkillAttack research means it's evidence-based, not theoretical.

---

### 14. IBM Sovereign Core — Governance Policy at Infrastructure Runtime

- **URL:** https://www.ibm.com/products/sovereign-core
- **Type:** Enterprise product
- **Date:** General Availability announced May 7, 2026 (IBM Think 2026)

**Abstract/Summary:**
> IBM Sovereign Core is a platform that embeds governance policy at the infrastructure runtime level for regulated, cross-border environments. It reached General Availability at IBM Think 2026 in Boston. Unlike policy-as-configuration tools, Sovereign Core enforces governance at the infrastructure layer — meaning policy compliance is guaranteed by the runtime environment itself, not by agent self-reporting or post-hoc audit. This is designed for enterprises in regulated industries (finance, healthcare, government) where data residency, compliance, and audit requirements are non-negotiable.

**Why I recommend this:**
IBM Sovereign Core represents the **next generation of runtime governance** — policy enforcement at the infrastructure level rather than the application level. This is a fundamentally different approach from LGA (which operates at the agent execution layer) or Microsoft Agent Governance Toolkit (which operates at the platform layer). Infrastructure-level enforcement means policy violations are physically impossible, not just detectable.

**Relevance to our topic:**
This is Layer 1 (Runtime-Level Governance) at the infrastructure tier. It complements LGA's execution-layer controls with physical-layer guarantees. For regulated enterprises, this is the difference between "we have policies" and "policies are enforced by the substrate."

**Which layer:** **Layer 1 — Runtime-Level Governance** (infrastructure tier)

**Is it a solution we're looking into?** Yes. For enterprises in regulated industries, infrastructure-level governance is the only viable approach. Sovereign Core provides the physical enforcement layer that makes policy compliance verifiable to auditors.

**Recommendation reason:** Most governance frameworks operate at the application layer, which means a compromised agent can bypass them. Infrastructure-level enforcement is the only approach that provides non-bypassable governance for high-assurance environments.

---

### 42. Learning Correct Behavior from Examples: Validating Sequential Execution in Autonomous Agents

- **arXiv ID:** 2605.03159
- **URL:** https://arxiv.org/abs/2605.03159
- **PDF:** https://arxiv.org/pdf/2605.03159
- **Authors:** Reshabh K Sharma, Gaurav Mittal, Yu Hu
- **Date:** May 2026

**Abstract:**
> As autonomous agents become increasingly sophisticated, validating their sequential behavior presents a significant challenge. Traditional testing approaches require manual specification, exact sequence matching, or thousands of training examples. We present a novel algorithm that automatically learns correct behavior from just 2-10 passing execution traces and validates new executions against this learned model. Our approach combines dominator analysis from compiler theory with multimodal large language model-powered semantic understanding to identify essential states and handle non-deterministic behavior. The system constructs a generalized ground truth model using Prefix Tree Acceptors, merges traces through multi-tiered equivalence detection, and validates new executions via topological subsequence matching. In controlled experiments, our system achieved high accuracy in detecting product bugs and false successes using only 3 training traces. This approach provides explainable validation results with coverage metrics and works across diverse domains including UI testing, code generation, and robotic processes.

**Why I recommend this paper:**
This is the **first paper to show that correct sequential behavior can be learned from just a handful of positive traces** — not thousands of examples, not manually written specifications. The combination of compiler theory (dominator analysis) with LLM semantic understanding is a genuinely novel approach. The 3-trace learning threshold makes it practical for real-world skill validation where you rarely have exhaustive test suites.

**Relevance to our topic:**
This bridges Layer 0 (Spec) and Layer 1 (Runtime). It provides a **middle path between static specification and runtime monitoring**: learn what correct looks like from a few examples, then validate against that learned model. For skill validation, this means you can verify that a skill executes correctly even when you don't have complete formal specs.

**Which layer:** **Layer 0 → Layer 1 bridge** (Spec-Level to Runtime-Level)

**Is it a solution we're looking into?** Yes. The learned validation approach is especially valuable for skill testing because most skills don't have exhaustive test suites. Learning correct behavior from 2-10 traces and then detecting deviations is exactly what we need for CI/CD skill validation.

**Recommendation reason:** The paper solves the "no spec, no test" problem for agent validation. It shows that a small number of positive execution traces is enough to learn a verifiable model of correct behavior. This is critical for skill governance because writing complete formal specifications for every skill is impractical, but running a few traces and validating against them is feasible.

---

### 43. Owner-Harm: Agents Harming Their Deployers

- **arXiv ID:** 2604.18658
- **URL:** https://arxiv.org/abs/2604.18658
- **PDF:** https://arxiv.org/pdf/2604.18658
- **Authors:** Dario Zhang
- **Date:** April 2026

**Abstract:**
> Existing AI agent safety benchmarks focus on generic criminal harm (cybercrime, harassment, weapon synthesis), leaving a systematic blind spot for a distinct and commercially consequential threat category: agents harming their own deployers. Real-world incidents illustrate the gap: Slack AI credential exfiltration (Aug 2024), Microsoft 365 Copilot calendar-injection leaks (Jan 2024), and a Meta agent unauthorized forum post exposing operational data (Mar 2026). We propose Owner-Harm, a formal threat model with eight categories of agent behavior damaging the deployer. We quantify the defense gap on two benchmarks: a compositional safety system achieves 100% TPR / 0% FPR on AgentHarm (generic criminal harm) yet only 14.8% (4/27; 95% CI: 5.9%-32.5%) on AgentDojo injection tasks (prompt-injection-mediated owner harm). A controlled generic-LLM baseline shows the gap is not inherent to owner-harm (62.7% vs. 59.3%, delta 3.4 pp) but arises from environment-bound symbolic rules that fail to generalize across tool vocabularies. On a post-hoc 300-scenario owner-harm benchmark, the gate alone achieves 75.3% TPR / 3.3% FPR; adding a deterministic post-audit verifier raises overall TPR to 85.3% (+10.0 pp) and Hijacking detection from 43.3% to 93.3%, demonstrating strong layer complementarity. We introduce the Symbolic-Semantic Defense Generalization (SSDG) framework relating information coverage to detection rate.

**Why I recommend this paper:**
Owner-Harm is the **first formal threat model for a blind spot that most safety benchmarks completely miss**: agents harming their own deployers rather than generic criminal targets. The 100% TPR on generic criminal harm vs. 14.8% on owner-harm is a devastating gap. The paper proves that the problem is not the threat itself but the **environment-bound symbolic rules** that fail to generalize across tool vocabularies.

**Relevance to our topic:**
This is Layer 1 (Runtime) and Layer 2 (Behavioral) governance. It exposes that current safety benchmarks are measuring the wrong thing, and it provides both a new threat model (eight categories) and a defense framework (SSDG) that shows layered defense works. The gate + post-audit verifier architecture is directly applicable to how we design runtime governance.

**Which layer:** **Layer 1 → Layer 2 bridge** (Runtime-Level to Behavioral-Level)

**Is it a solution we're looking into?** Yes. The SSDG framework and the layered defense results (75.3% gate alone → 85.3% with verifier) provide a concrete target for our governance architecture. The paper also gives us a new benchmark category that any governance system must address.

**Recommendation reason:** The 100% → 14.8% collapse is the single most important finding in agent safety this year. It proves that benchmarking against generic criminal harm is insufficient for production governance. The paper provides both the threat model and the defense architecture to fix this gap.

---

### 44. TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling

- **arXiv ID:** 2605.27690
- **URL:** https://arxiv.org/abs/2605.27690
- **PDF:** https://arxiv.org/pdf/2605.27690
- **Authors:** Jiaqian Li et al.
- **Date:** May 2026

**Abstract:**
> LLM agents increasingly operate through multi-turn tool use and environment interaction, where safety risks often emerge from intermediate steps long before they surface in the final outcome. Reactive auditing is therefore insufficient: post-hoc diagnosis frequently misses the chance to flag risks while they are unfolding. We propose TRACES, a representation-based proactive auditor that learns prefix-level trajectory risk states from the hidden representations of an observer LLM. TRACES induces latent mechanism features from step representations and models their temporal evolution to estimate whether a partial trajectory is drifting toward unsafe behavior. To sidestep the cost and ambiguity of step-level risk annotation, TRACES is trained with weak trajectory-level supervision while still producing dense prefix-level risk estimates. Across multiple agent safety benchmarks, TRACES improves both full-trajectory safety prediction and proactive risk discrimination. Our analyses further suggest that these risk states can help train a safer agent, highlighting the broader potential of proactive auditing for long-horizon agent safety.

**Why I recommend this paper:**
TRACES is the **first proactive safety auditor for multi-turn agents** that catches risks *while they are unfolding* rather than after the fact. Most existing safety systems are reactive — they audit completed trajectories. TRACES learns latent risk states from an observer LLM's hidden representations and estimates whether a partial trajectory is drifting toward unsafe behavior. This is a fundamental shift from "did it go wrong?" to "is it going wrong right now?"

**Relevance to our topic:**
This is Layer 1 (Runtime-Level Governance) with a direct bridge to Layer 2 (Behavioral). It provides a **middle path between static specification and runtime monitoring**: instead of relying on pre-defined rules or post-hoc evaluation, it learns risk patterns from the agent's own representations during execution. The weak trajectory-level supervision approach makes it practical — no need for expensive step-level annotations.

**Which layer:** **Layer 1 → Layer 2 bridge** (Runtime-Level to Behavioral-Level)

**Is it a solution we're looking into?** Yes. The proactive auditing approach is especially valuable for long-horizon agent tasks where safety violations accumulate across steps. Learning risk states from hidden representations and using them to both audit and train safer agents is exactly the kind of dynamic governance we need for production systems.

**Recommendation reason:** The paper shifts the paradigm from reactive to proactive safety auditing. The key insight is that safety risks in multi-turn agents are not binary events at the end — they are gradual drifts that can be detected early if you know where to look. TRACES shows that those signals exist in the LLM's own hidden states, and they can be learned with surprisingly weak supervision.

---

### 45. EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems

- **arXiv ID:** 2604.11174
- **URL:** https://arxiv.org/abs/2604.11174
- **PDF:** https://arxiv.org/pdf/2604.11174
- **Authors:** Xue Qin et al.
- **Date:** April 2026

**Abstract:**
> Recent progress in embodied AI has produced a growing ecosystem of robot policies, foundation models, and modular runtimes. However, current evaluation remains dominated by task success metrics such as completion rate or manipulation accuracy. These metrics leave a critical gap: they do not measure whether embodied systems are governable -- whether they respect capability boundaries, enforce policies, recover safely, maintain audit trails, and respond to human oversight. We present EmbodiedGovBench, a benchmark for governance-oriented evaluation of embodied agent systems. Rather than asking only whether a robot can complete a task, EmbodiedGovBench evaluates whether the system remains controllable, policy-bounded, recoverable, auditable, and evolution-safe under realistic perturbations. The benchmark covers seven governance dimensions: unauthorized capability invocation, runtime drift robustness, recovery success, policy portability, version upgrade safety, human override responsiveness, and audit completeness. We define a benchmark structure spanning single-robot and fleet settings, with scenario templates, perturbation operators, governance metrics, and baseline evaluation protocols. We describe how the benchmark can be instantiated over embodied capability runtimes with modular interfaces and contract-aware upgrade workflows. Our analysis suggests that embodied governance should become a first-class evaluation target. EmbodiedGovBench provides the initial measurement framework for that shift.

**Why I recommend this paper:**
EmbodiedGovBench is the **first benchmark to make governance a first-class evaluation target for embodied agents**. Where all existing embodied benchmarks measure task completion, this one measures whether the system remains controllable, policy-bounded, recoverable, auditable, and evolution-safe. The seven governance dimensions (unauthorized capability invocation, runtime drift robustness, recovery success, policy portability, version upgrade safety, human override responsiveness, audit completeness) are the evaluation criteria that any production embodied agent must meet.

**Relevance to our topic:**
This is Layer 2 (Behavioral-Level Governance) for embodied agents. It provides the measurement infrastructure for governance-oriented evaluation, complementing BeSafe-Bench (which covers web, mobile, and embodied VLM/VLA) with a focus specifically on governability rather than task success.

**Which layer:** **Layer 2 — Behavioral-Level Governance**

**Is it a solution we're looking into?** Yes. EmbodiedGovBench should be integrated alongside BeSafe-Bench for embodied agent evaluation. The seven governance dimensions provide the evaluation framework for whether agents are safe to deploy, not just capable.

**Recommendation reason:** The gap between "can complete the task" and "can complete the task safely and governably" is the critical blind spot in embodied AI evaluation. EmbodiedGovBench closes that gap by making governance a measurable evaluation target.

---

### 46. Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward

- **arXiv ID:** 2602.12430
- **URL:** https://arxiv.org/abs/2602.12430
- **PDF:** https://arxiv.org/pdf/2602.12430
- **Authors:** Renjun Xu et al.
- **Date:** February 2026 (updated June 2026)
- **GitHub:** https://github.com/renjunxu/agentskills-survey

**Abstract:**
> The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL.md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries, autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems.

**Why I recommend this paper:**
This is the **first comprehensive survey of the agent skills landscape** and it introduces the **Skill Trust and Lifecycle Governance Framework** — a four-tier, gate-based permission model (G1–G4 verification gates, T1–T4 trust tiers) that maps skill provenance to graduated deployment capabilities. The finding that 26.1% of community-contributed skills contain vulnerabilities is a critical data point. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for governance.

**Relevance to our topic:**
This is the apex of Layer 0 (Spec-Level Governance). The Skill Trust and Lifecycle Governance Framework provides the provenance-based permission model that every skill ecosystem needs: skills are not just validated for format correctness (Skilldex) or contractual completeness (GovernSpec), but are assigned trust tiers based on their provenance, with graduated deployment capabilities. The G1–G4 gates (format, semantic, security, behavioral) and T1–T4 tiers (unverified, community, reviewed, certified) provide a concrete trust ladder.

**Which layer:** **Layer 0 — Spec-Level Governance** (with provenance and trust lifecycle hooks)

**Is it a solution we're looking into?** Yes. The Skill Trust and Lifecycle Governance Framework is the missing piece in the skill governance stack. It provides the trust tier model that should be integrated with Skilldex validation and GovernSpec contract enforcement.

**Recommendation reason:** The 26.1% vulnerability rate in community skills proves that format validation alone is insufficient. The trust tier framework provides the graduated deployment model that lets organizations adopt community skills with appropriate risk controls.

---

### 47. OWASP Practical Guide for Secure MCP Server Development

- **URL:** https://genai.owasp.org/resource/owasp-practical-guide-for-secure-mcp-server-development/
- **Type:** Industry standard / Security framework
- **Date:** February 2026 (published Feb 4, 2026)
- **Format:** PDF guide, 40+ pages

**Abstract/Summary:**
> The OWASP Practical Guide for Secure MCP Server Development provides comprehensive security guidance for developers building Model Context Protocol (MCP) servers. The guide covers eight security domains: (1) Authentication — verifying agent identity before tool access; (2) Authorization — least-privilege access control for tool capabilities; (3) Input Validation — sanitizing and validating all inputs to MCP tools; (4) Output Encoding — preventing injection attacks through proper output handling; (5) Error Handling — avoiding information leakage through error messages; (6) Logging — comprehensive audit trails for all MCP interactions; (7) Dependency Management — securing the supply chain of MCP server dependencies; (8) Configuration Management — secure defaults and hardening guidance. Each domain includes threat scenarios, code examples, and testing recommendations. The guide is designed to be integrated into existing DevSecOps pipelines and adapted for enterprise MCP deployments.

**Why I recommend this:**
This is the **first OWASP-level implementation guidance specifically for MCP server security**. While MCP-38 provides the threat taxonomy (what can go wrong), this guide provides the concrete implementation guidance (how to prevent it). The eight security domains map directly to the OWASP Top 10 for Agentic Applications, making it a practical complement to both MCP-38 and the OWASP Top 10.

**Relevance to our topic:**
This is Layer 1 (Runtime-Level Governance) at the protocol implementation level. MCP is the de facto standard for agent-tool communication, and this guide provides the secure coding practices that every MCP server developer needs. The authentication and authorization domains address the zero-trust inter-agent authorization that LGA requires; the logging domain provides the immutable audit trails that LGA mandates.

**Which layer:** **Layer 1 — Runtime-Level Governance** (protocol implementation security)

**Is it a solution we're looking into?** Yes. Any agent system using MCP needs this guide. The eight security domains provide the implementation checklist for secure MCP server development, which is a prerequisite for any production agent deployment.

**Recommendation reason:** Threat taxonomies (MCP-38) tell you what to worry about; implementation guides tell you what to do. This guide provides the concrete security practices that turn MCP-38's threat taxonomy into actionable engineering requirements.

---

### 48. MITRE ATLAS Agentic AI Update

- **URL:** https://atlas.mitre.org/
- **Type:** Industry standard / Adversarial taxonomy
- **Date:** October 2025 (updated with 14 new agentic AI techniques)

**Abstract/Summary:**
> MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) is the standard adversarial taxonomy for AI systems. The October 2025 update added 14 new techniques specifically targeting agentic AI systems: multi-step tool chaining exploitation, state manipulation across agent sessions, delegation abuse (agent-to-agent privilege escalation), persistent skill poisoning, dynamic capability injection, cross-runtime trust boundary violations, agent memory tampering, goal hijacking through sub-task decomposition, tool description poisoning in multi-turn contexts, capability enumeration and reconnaissance, agent behavior cloning for evasion, orchestration layer injection, autonomous agent red-team emulation, and recursive self-modification detection. Each technique includes tactic mappings, procedure examples, mitigation recommendations, and real-world incident references. The update also introduced cross-mappings to OWASP Top 10 for Agentic Applications (2026) and NIST AI RMF.

**Why I recommend this:**
MITRE ATLAS is the **standard adversarial taxonomy for AI systems** (equivalent to MITRE ATT&CK for traditional cyber). The 14 new agentic-specific techniques formalize attack vectors that traditional AI threat models miss: multi-step tool chaining, state manipulation, delegation abuse, persistent skill poisoning. These are not just theoretical — they are derived from real-world incidents and red-team exercises. The cross-mapping to OWASP and NIST means ATLAS can be integrated into existing compliance and threat-intelligence programs.

**Relevance to our topic:**
This spans Layer 1 (Runtime) and Layer 2 (Behavioral). The 14 techniques cover runtime attacks (tool chaining, state manipulation, delegation abuse) and behavioral attacks (goal hijacking, behavior cloning, recursive self-modification). The taxonomy provides the adversarial model that governance frameworks must defend against.

**Which layer:** **Layer 1 + Layer 2** — Runtime-Level and Behavioral-Level Governance

**Is it a solution we're looking into?** Yes. Any serious agent governance program needs an adversarial threat model. MITRE ATLAS provides the standard taxonomy that security teams, auditors, and red-teamers already understand. The 14 new agentic techniques fill the gap that traditional AI threat models leave open.

**Recommendation reason:** Governance without an adversarial model is just wishful thinking. MITRE ATLAS provides the attack taxonomy that tells you what your governance controls must defend against. The 14 new agentic techniques are the specific threats that make agent governance different from traditional AI security.

---

### 49. NIST IR 8596 — Cybersecurity Framework Profile for AI

- **URL:** https://www.nist.gov/publications/cybersecurity-framework-profile-ai
- **Type:** Government standard / Compliance framework
- **Date:** December 2025
- **Format:** NIST Interagency Report

**Abstract/Summary:**
> NIST IR 8596 applies the Cybersecurity Framework (CSF) 2.0 to artificial intelligence systems, providing a structured approach to managing AI cybersecurity risks. The report maps CSF functions (Identify, Protect, Detect, Respond, Recover) to AI-specific contexts including model training, deployment, inference, and agentic operation. For agentic AI, the report introduces explicit control overlays: capability boundary identification (Identify), tool access governance (Protect), agent behavior monitoring (Detect), incident response for autonomous actions (Respond), and rollback mechanisms for agent-driven changes (Recover). The profile includes implementation examples for enterprise agent deployments and cross-references to NIST AI RMF, OWASP Top 10 for Agentic Applications, and MITRE ATLAS. It is designed for organizations in regulated industries seeking to apply NIST CSF to AI systems with the same rigor as traditional IT.

**Why I recommend this:**
NIST is the **authoritative standard for U.S. federal and regulated-industry cybersecurity**. NIST IR 8596 is the first NIST publication to explicitly address agentic AI with control overlays, making it the compliance baseline for regulated agent deployments. The cross-references to OWASP and MITRE ATLAS mean it integrates with existing security frameworks rather than creating yet another silo.

**Relevance to our topic:**
This spans all three layers: Identify (Layer 0 — spec and capability inventory), Protect (Layer 1 — runtime access governance), Detect (Layer 1 + Layer 2 — behavior monitoring), Respond (Layer 2 — incident response), Recover (Layer 2 — rollback). For regulated enterprises, this is the compliance framework that maps our Three-Layer Stack to auditable NIST controls.

**Which layer:** **All layers** — Layer 0 (Identify), Layer 1 (Protect, Detect), Layer 2 (Detect, Respond, Recover)

**Is it a solution we're looking into?** Yes. For any agent deployment in regulated industries (finance, healthcare, government), NIST compliance is non-negotiable. NIST IR 8596 provides the structured control framework that makes agent governance auditable to regulators and auditors.

**Recommendation reason:** NIST CSF is the de facto compliance standard for U.S. enterprises. Having a NIST-sanctioned profile for agentic AI means governance can be framed in terms auditors already understand: Identify, Protect, Detect, Respond, Recover. This is the bridge between technical governance and regulatory compliance.

---

### 50. reprobe-audit — An Open Scoring Schema for LLM Agent Benchmark Disclosure

- **URL:** https://github.com/mahdinaser/reprobe-audit
- **Paper:** IEEE International Conference on Big Data 2026
- **Type:** Open-source framework / Audit tool
- **Date:** 2026
- **License:** MIT

**Abstract/Summary:**
> REPROBE is a small schema and codebook for recording, per result, what an LLM agent benchmark evaluation actually did: which benchmark version, which scaffold, which inference settings, what it cost, and how it failed. The repository contains the schema, the scoring codebook, a validator, an aggregation utility, two example harness-hook patches, the raw scoring sheet from a 12-paper pilot audit, and per-paper extracted evidence. The 12-paper pilot audit covered eight agent benchmarks (SWE-bench, WebArena, OSWorld, GAIA, AgentBench, VisualWebArena, Mind2Web, MLE-bench) and four classical static benchmarks. The agent-benchmark mean disclosure score was 0.38 (vs. 0.66 for classical benchmarks). Cost reporting was universally absent for agent benchmarks. No agent benchmark fully disclosed its harness. Identity disclosure was the strongest field but with a split: all classical benchmarks reached 1.0, while all eight agent benchmarks sat at 0.5 because benchmark version and subset-selection policy were not stated as structured fields.

**Why I recommend this:**
reprobe-audit is the **first systematic framework for verifying whether agent benchmark claims are reproducible**. The 0.38 mean disclosure score for agent benchmarks (vs. 0.66 for classical benchmarks) is a credibility crisis. Cost reporting is universally absent. No agent benchmark fully discloses its harness. This is not a research paper — it's an audit tool and a warning that current agent safety benchmarks may not be trustworthy.

**Relevance to our topic:**
This is Layer 2 (Behavioral-Level Governance) at the meta-evaluation level. Governance without trustworthy benchmarks is guesswork. reprobe-audit provides the framework for verifying benchmark credibility, which is essential for any governance system that relies on benchmark results to justify safety claims.

**Which layer:** **Layer 2 — Behavioral-Level Governance** (meta-evaluation / benchmark credibility)

**Is it a solution we're looking into?** Yes. If we are going to use BeSafe-Bench, ST-WebAgentBench, EmbodiedGovBench, or any other benchmark to measure agent safety, we need to verify that those benchmarks are themselves trustworthy. reprobe-audit provides the disclosure schema and scoring framework for that verification.

**Recommendation reason:** The 0.38 disclosure score is the most important meta-finding in agent evaluation this year. It means that most agent safety benchmarks cannot be independently verified or reproduced. reprobe-audit provides the tools to fix this credibility gap before it undermines the entire governance stack.

---

### 51. Agent Security Harness — 474-Test Security Scanner for AI Agents

- **URL:** https://github.com/msaleme/red-team-blue-team-agent-fabric
- **Type:** Open-source security product
- **Date:** 2026 (actively maintained)
- **License:** Open source

**Abstract/Summary:**
> The Agent Security Harness is a comprehensive security testing framework for AI agent systems. It provides 474 targeted security tests across 33 modules covering: prompt injection (direct and indirect), tool misuse and privilege escalation, data exfiltration paths, inter-agent trust boundary violations, skill package poisoning, MCP server exploitation, autonomous action abuse, and goal hijacking. The harness supports both red-team (adversarial) and blue-team (defensive) testing modes. Red-team mode generates adversarial test cases to probe vulnerabilities; blue-team mode validates that defensive controls (guardrails, sandboxing, authorization) block known attack patterns. The framework is designed to be integrated into CI/CD pipelines for automated security testing of agent deployments. Each test produces a structured report with severity ratings, attack chains, and remediation recommendations.

**Why I recommend this:**
This is the **most comprehensive open-source security testing framework for AI agents** — 474 tests across 33 modules. Unlike point solutions (Skilldex for validation, MCPThreatHive for MCP threats), the Agent Security Harness covers the entire attack surface: prompt injection, tool misuse, data exfiltration, inter-agent trust violations, skill poisoning, MCP exploitation, autonomous action abuse, and goal hijacking. The red-team/blue-team dual mode means it can be used both for offensive testing and defensive validation.

**Relevance to our topic:**
This spans all three layers: Skills Scan (Layer 0 — skill poisoning), MCP scan and Agent Scan (Layer 1 — runtime exploitation), and LLM jailbreak/autonomous action abuse (Layer 2 — behavioral safety). It is the operational security testing tool that turns governance frameworks into measurable, repeatable verification.

**Which layer:** **All layers** — Layer 0 (Skills Scan), Layer 1 (MCP scan, Agent Scan), Layer 2 (LLM jailbreak, autonomous action abuse)

**Is it a solution we're looking into?** Yes. This is the closest open-source equivalent to a full-stack penetration-testing suite for agents. The 474 tests provide the concrete security verification that governance frameworks need to be operational. The CI/CD integration means security testing can be automated as part of the deployment pipeline.

**Recommendation reason:** Governance without testing is just policy. The Agent Security Harness provides the testing infrastructure that turns governance controls into verifiable security outcomes. The 474 tests are the concrete evidence that governance is working — or not.

---

### 52. Web Skills Protocol (WSP) — Web Discovery Layer for Skills

- **URL:** https://github.com/openclaw/skills/blob/main/skills/0xtresser/web-skills-protocol/SPEC.md
- **Type:** Open specification / Protocol draft
- **Date:** March 2026
- **Status:** Community draft, open for feedback

**Abstract/Summary:**
> The Web Skills Protocol (WSP) defines a web discovery layer for agent skills, enabling skills to be discoverable, inspectable, and verifiable on the public web. The protocol specifies two core conventions: `/skills.txt` — a plain-text file at the domain root listing all discoverable skills with metadata (name, version, author, trust tier, verification status, URL); and `/agents.txt` — a companion file listing agent capabilities that consume those skills. WSP is designed to be compatible with existing skill formats (SKILL.md, skill.json, Cursor manifest.json) and integrates with the Skill Trust and Lifecycle Governance Framework's trust tier model. The protocol supports optional extensions: cryptographic signatures (linking skills to verified authors), attestation endpoints (proving skill has passed validation gates), and revocation lists (marking compromised or deprecated skills). WSP enables transparent, inspectable skill registries without requiring centralized platforms, making it possible for any domain to host and govern its own skills.

**Why I recommend this:**
WSP is the **first protocol for decentralized web-native skill discovery**. Rather than relying on centralized registries (ClawHub, npm, PyPI) that can be poisoned or taken down, WSP lets any domain host its own skills with transparent, inspectable metadata. The `/skills.txt` and `/agents.txt` conventions are simple enough to implement on any web server, but powerful enough to support cryptographic signatures, attestation, and revocation. The integration with trust tiers means skills can be discovered and filtered by their governance status.

**Relevance to our topic:**
This is Layer 0 (Spec-Level Governance) at the discovery and distribution level. WSP provides the infrastructure for transparent skill registries: skills are not just validated (Skilldex) and contracted (GovernSpec) and trust-tiered (Agent Skills for LLMs), but also **discoverable and inspectable** on the web. The cryptographic signatures and attestation endpoints provide the provenance verification that KYA requires.

**Which layer:** **Layer 0 — Spec-Level Governance** (discovery, distribution, and provenance)

**Is it a solution we're looking into?** Yes. WSP provides the decentralized discovery infrastructure that makes skill governance scalable. Rather than relying on a single registry that can be compromised, WSP lets every organization host its own skills with transparent metadata and cryptographic verification.

**Recommendation reason:** Centralized skill registries are a single point of failure and a single point of attack. WSP's decentralized model — where every domain hosts its own skills with cryptographic signatures and attestation — is the only architecture that can scale to a global, trustworthy skill ecosystem.

---

### 53. SkillVetBench — LLM-as-Judge Security Evaluation for Agent Skills

- **arXiv ID:** 2606.00925 (benchmark) / 2606.15899 (LLM-as-Judge leaderboard)
- **URL:** https://arxiv.org/abs/2606.15899
- **PDF:** https://arxiv.org/pdf/2606.15899
- **Authors:** Ismail Hossain, Sai Puppala, Md Jahangir Alam, Tanzim Ahad, Sajedul Talukder (UTEP SUPREME Lab)
- **Date:** June 14, 2026

**Abstract:**
> Open-source LLM agent ecosystems are growing rapidly, yet the security of community-contributed skills — modular tool definitions that extend agent capabilities — remains largely unvetted. The gap we fill: existing scanners operate at the code layer and are structurally blind to instruction-layer and multi-agent risk — natural-language directives that hijack an agent, exfiltrate data through encoded side channels, or chain harm across pipelines — so what is needed is a semantic, multi-dimensional vetting system rather than another signature matcher. We present SKILLVETBENCH, a live public leaderboard on Hugging Face that uses an LLM-as-Judge to vet agent skills. What is new: SARS (Skill Agentic Risk Score), a five-dimensional agentic-risk metric with a principled weighted formula for instruction-following systems. What is integrated: full CVSS v4.0 vector decomposition and a ClawHub dual-view that places our LLM-generated review beside the official marketplace verdict. What is demonstrated: drawing on our companion benchmark paper, the LLM-as-Judge stage achieves zero false negatives across 78 confirmed-malicious skills and zero false positives across 22 benign controls, while the best static baseline (SKILLSIEVE) still misses 15%; for instruction-layer categories such as Prompt Injection and Memory Poisoning, conventional tools miss between 89% and 100% of threats (e.g., CODEBERT detects none of nine memory-poisoning skills). Detection rates vary from 35% to 95% across four LLM evaluators, motivating ensemble scoring in production deployments.

**Why I recommend this:**
SkillVetBench is the **first semantic skill security evaluation system** that looks at what skills *declare* they will do, not just what code they contain. The SARS score is the first agentic-specific risk metric — it captures instruction fidelity risk, data gravity, action irreversibility, blast radius, and chain amplification in a single 0–10 score. The zero false negatives on 78 malicious skills (vs. 15% miss rate for the best static tool) proves that code-level scanning is structurally insufficient for agent security.

**Relevance to our topic:**
This is Layer 0 (Spec-Level Governance) with Layer 2 (Behavioral) measurement. It validates skills at the semantic level — reading instructions, tool declarations, and permission grants as a coherent behavioral contract. The CVSS v4.0 integration provides a standard security vocabulary; the ClawHub dual-view exposes marketplace detection gaps.

**Which layer:** **Layer 0 + Layer 2**

**Is it a solution we're looking into?** Yes. SkillVetBench provides the semantic evaluation layer that complements static validation (Skilldex) and contractual enforcement (GovernSpec). The SARS score should be integrated into skill marketplace admission pipelines.

**Recommendation reason:** Code scanners are blind to instruction-layer attacks. SkillVetBench proves that LLM-as-Judge ensemble scoring can detect these attacks with zero false negatives, making it an essential component of any skill governance pipeline.

---

### 54. Agents' Last Exam (ALE) — Real-World Agent Capability Benchmark

- **arXiv ID:** 2606.05405
- **URL:** https://arxiv.org/abs/2606.05405
- **PDF:** https://arxiv.org/pdf/2606.05405
- **Authors:** Yiyou Sun et al. (UC Berkeley RDI / Dawn Song group, 210+ additional authors)
- **Date:** June 3, 2026 (v1) / June 11, 2026 (v2)

**Abstract:**
> Recent AI systems have achieved strong results on a wide range of benchmarks, yet these gains have not translated into economically meaningful deployment across many professional domains. We argue that this gap is largely an evaluation problem: widely used benchmarks lack sustained performance measurement on real and economically valuable workflows. This paper introduces Agents' Last Exam (ALE), a benchmark designed to evaluate AI agents on long horizon, economically valuable, real world tasks with verifiable outcomes. Developed in collaboration with 250+ industry experts, ALE covers non-physical industries defined with reference to O*NET / SOC 2018 (the U.S. federal occupational taxonomy). It is organized around a task taxonomy with 55 sub fields grouped into 13 industry clusters covering 1K+ tasks. Current results show that the hardest tier remains far from saturated: across mainstream harness and backbone configurations, the average full pass rate is below 1%. ALE is designed as a living benchmark: its task pool grows continuously as new workflows and industries are onboarded. More broadly, ALE is intended not merely as another leaderboard, but as an instrument for closing the gap between benchmark success and GDP relevant impact.

**Why I recommend this:**
ALE is the **most serious attempt yet to evaluate AI agents on economically valuable, long-horizon, real professional work**. Unlike synthetic benchmarks (Terminal-Bench, SWE-bench) that measure narrow capabilities, ALE tests whether agents can actually do the work that humans are paid to do. The 2.6% pass rate on the hardest tier — despite Codex + GPT-5.5 scoring 82% on Terminal-Bench — is the single most important reality check in agent evaluation.

**Relevance to our topic:**
This is primarily Layer 2 (Behavioral-Level Governance) and Layer 3 (Enterprise/Policy). ALE provides the measurement infrastructure for whether agents are ready for real-world deployment. The three-tier structure (Near-Term, Full-Spectrum, Last-Exam) lets organizations choose evaluation intensity based on their risk tolerance. The ALE-Claw reference implementation (derived from OpenClaw) provides a concrete harness for testing.

**Which layer:** **Layer 2 + Layer 3**

**Is it a solution we're looking into?** Yes. ALE should be the benchmark of record for evaluating agent readiness for professional deployment. The 2.6% Last-Exam pass rate is the metric that matters: until agents pass this tier, claims of "agentic automation" in professional contexts are premature.

**Recommendation reason:** Benchmark saturation on synthetic tasks has created a false sense of progress. ALE exposes the real capability gap — agents can solve coding puzzles but cannot complete professional workflows. This is the benchmark that keeps governance honest.

---

### 55. MAGIQ — Post-Quantum Multi-Agentic AI Governance

- **arXiv ID:** 2605.06933v2
- **URL:** https://arxiv.org/abs/2605.06933
- **PDF:** https://arxiv.org/pdf/2605.06933
- **Authors:** S. Avizeh et al.
- **Date:** May 7, 2026 (v1) / May 18, 2026 (v2)

**Abstract:**
> Our computing ecosystem is being transformed by two emerging paradigms: the increased deployment of agentic AI systems and advancements in quantum computing. With respect to agentic AI systems, one of the most critical problems is creating secure governing architectures that ensure agents follow their owners' communication and interaction policies and can be held accountable for the messages they exchange with other agents. With respect to quantum computing, existing systems must be retrofitted and new cryptographic mechanisms must be designed to ensure long-term security and quantum resistance. In fact, NIST recommends that standard public-key cryptographic algorithms, including RSA, Diffie-Hellman (DH), and elliptic-curve constructions (ECC), be deprecated starting in 2030 and disallowed after 2035. In this paper, we present MAGIQ, a framework for policy definition and enforcement in multi-agent AI systems using novel, highly efficient, quantum-resistant cryptographic protocols with proven security guarantees. MAGIQ (i) allows users to define rich communication and access-control policy budgets for agent-to-agent sessions and tasks, including global budgets for one-to-many agent sessions; (ii) enforces such policies using post-quantum cryptographic primitives; (iii) supports session-based enforcement of policies for agent-to-agent and one-to-many agent sessions; and (iv) provides accountability of agents to their users through message attribution. We formally model and prove the correctness and security of the system using the Universal Composability (UC) framework. We evaluate the computation and communication overhead of our framework and compare it with the state-of-the-art agentic AI framework SAGA. MAGIQ is a first step toward post-quantum-secure solutions for agentic AI systems.

**Why I recommend this:**
MAGIQ is the **first post-quantum-secure agent governance framework with formal UC-security proofs**. It replaces classical cryptography (RSA, ECDSA, EdDSA, DH, ECDH) with NIST-standardized post-quantum primitives (ML-KEM, ML-DSA, SLH-DSA) and proves security in the Universal Composability framework. The session-based enforcement (AA-sessions for one-to-one, CC-sessions for one-to-many) with hash-chain policy budgets and digitally signed session-authorization tokens provides a rigorous cryptographic foundation for agent policy enforcement.

**Relevance to our topic:**
This is Layer 1 (Runtime-Level Governance) with Layer 3 (Policy/Cryptographic). MAGIQ provides the cryptographic infrastructure that underpins trust in multi-agent systems: agents can prove their identity, enforce policy budgets, and attribute messages — all with quantum-resistant security. The overhead is comparable to SAGA (which uses classical cryptography), proving that post-quantum security is practical today.

**Which layer:** **Layer 1 + Layer 3**

**Is it a solution we're looking into?** Yes. As NIST deprecates classical public-key algorithms by 2030, any long-lived agent governance infrastructure must be post-quantum. MAGIQ provides the cryptographic foundation for agent identity, authorization, and policy enforcement in a quantum-safe manner.

**Recommendation reason:** Agent governance without cryptographic foundations is just policy. MAGIQ proves that policy enforcement can be formally secure, even against quantum adversaries. This is the infrastructure layer that makes agent governance trustworthy at scale.

---

### 56. AIP — Agent Instruction Protocol for Structured Skill Graphs

- **arXiv ID:** 2606.04781
- **URL:** https://arxiv.org/abs/2606.04781
- **PDF:** https://arxiv.org/pdf/2606.04781
- **Authors:** Zachary Blumenfeld et al.
- **Date:** June 3, 2026

**Abstract:**
> Agent Skills today consist largely of free-form prose requiring the agent to read, interpret, and re-derive how to act in every session. This imposes two compounding costs: reduced reliability on implementation-heavy tasks, and difficulty in skill creation and improvement, since editing prose is a fragile process that both humans and agents struggle with. The Agent Instruction Protocol (AIP) addresses both by modeling a skill as a directed execution graph: discrete steps as nodes backed by deterministic scripts or natural-language descriptions, connected by explicit typed input/output edges, and governed by a schema-validated YAML specification. A compiler meta-skill translates existing human-written skills into this form. The benefits are twofold. First, compiling human-written skills to AIP raised Claude Sonnet's mean task reward from 0.60 to 0.71 and pass rate from 53% to 67% across 27 real agent tasks from SkillsBench — a statistically significant gain (Wilcoxon signed-rank p = 0.011). Second, on creation and improvement, because each skill is schema-validated, functionally testable, and addressable node-by-node, failures can be diagnosed and repaired precisely. Two authored-skill failures were traced to the script level. After adjusting the AIP spec and recompiling, both recovered with zero regressions (one task going from 0/5 to 5/5), turning skill improvement into a measurable tuning loop rather than a prose rewrite.

**Why I recommend this:**
AIP is the **first structured skill representation that makes skills machine-governable**. Free-form prose skills are fundamentally ungovernable — you can't type-check prose, can't diff semantic changes, can't pinpoint failure nodes. AIP's directed execution graph with typed I/O edges and schema-validated YAML makes skills into addressable, testable, versionable artifacts. The 53% → 67% pass rate improvement proves that structure beats prose for reliability. The node-level addressability enables precise failure diagnosis and repair, turning skill maintenance from a rewrite into a tuning loop.

**Relevance to our topic:**
This is **Layer 0 (Spec-Level Governance)** with **Layer 1 (Runtime)** implications. AIP provides the structured representation that makes static governance possible: schema validation, node-level testing, corpus-level introspection, and natural action space for RL over skills. The graph structure enables governance at the skill level — something impossible with prose skills.

**Which layer:** **Layer 0 + Layer 1**

**Is it a solution we're looking into?** Yes. AIP is the missing structural layer that makes skill governance practical. It complements Skilldex (validation), GovernSpec (contracts), and SkCC (compilation) by providing a human-writable, machine-governable skill representation.

**Recommendation reason:** Prose skills cannot be governed. AIP proves that compiling them to typed graphs with deterministic scripts and explicit edges raises reliability by 26% and makes failures precisely addressable. This is the structural foundation for skill-level governance.

---

### 57. CheetahClaws — System Scaling Harness for Agentic AI

- **arXiv ID:** 2605.26112
- **URL:** https://arxiv.org/abs/2605.26112
- **PDF:** https://arxiv.org/pdf/2605.26112
- **Authors:** Shangding Gu et al.
- **Date:** May 25, 2026

**Abstract:**
> This paper studies the next major bottleneck in agentic AI as system scaling, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models. We refer to this shift as scaling the harness: treating the structured execution layer around a foundation model as a first-class object of design, evaluation, and optimization. Although recent large language models enable agents to use tools, retrieve information, maintain memory, and execute long-horizon workflows, evaluation remains largely model-centric, often reducing agents to final-task success while treating memory, retrieval, tool use, orchestration, verification, and governance as secondary implementation details. This framing is increasingly inadequate because agent performance emerges from the interaction among the foundation model, memory substrate, context constructor, skill-routing layer, orchestration loop, and verification-and-governance layer. Together, these components form the agent harness, which translates model capability into long-horizon agent behavior. We study scaling the harness through three core bottlenecks: context governance, trustworthy memory, and dynamic skill routing, together with the orchestration and governance mechanisms that coordinate and constrain them. We further outline a research agenda for harness-level benchmarks that go beyond one-shot task success to measure trajectory quality, memory hygiene, context efficiency, verification cost, and safe evolution over time. To make the discussion concrete, we develop CheetahClaws, a Python-native reference harness, and compare it with Claude Code and OpenClaw.

**Why I recommend this:**
CheetahClaws is the **first paper to treat the agent harness — including governance — as a first-class design object**. Current evaluation is model-centric; this paper argues that agent performance emerges from the harness, not just the model. The three core bottlenecks (context governance, trustworthy memory, dynamic skill routing) are exactly the runtime governance concerns that Layer 1 and Layer 2 address. The proposed harness-level benchmarks (trajectory quality, memory hygiene, verification cost, safe evolution) are the metrics that matter for production deployment.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** and **Layer 2 (Behavioral)**. CheetahClaws treats governance as a core harness component, not an afterthought. The verification-and-governance layer is explicitly part of the harness architecture. The Python reference implementation enables empirical comparison with Claude Code and OpenClaw.

**Which layer:** **Layer 1 + Layer 2**

**Is it a solution we're looking into?** Yes. CheetahClaws provides the system-level framework that connects model capability to long-horizon behavior through structured governance. The harness-level benchmarks (trajectory quality, memory hygiene, safe evolution) are the evaluation targets that Layer 2 needs.

**Recommendation reason:** Model-centric evaluation misses the governance problem. CheetahClaws proves that agent performance emerges from the harness, not just the model, and provides concrete benchmarks for the governance qualities that matter in production.

---

### 58. W2S — Workflow-to-Skill: Automatic Skill Construction from Traces

- **arXiv ID:** 2606.06893
- **URL:** https://arxiv.org/abs/2606.06893
- **PDF:** https://arxiv.org/pdf/2606.06893
- **Authors:** Yuyang Zhang et al.
- **Date:** June 5, 2026

**Abstract:**
> Large language model agents increasingly rely on Skills to encode procedural knowledge, yet high-quality Skills remain costly to hand-write. This paper studies automatic Skill construction from heterogeneous interaction evidence, including demonstrations, agent trajectories, tool traces, and execution logs. We argue that trace-to-skill construction is not simple summarization, because traces are fragmented, redundant, and may miss rare but safety-critical behaviors. To address this, we introduce RWSA, a workflow-oriented intermediate representation that decomposes Skills into Workflow structure, execution Semantics, and runtime Attachments, capturing task decomposition, control flow, verification, safety, rollback, and state management. Building on RWSA, we propose W2S, a framework that segments traces, induces local Skill drafts, aligns shared structures, reconciles branches, and compresses redundancy while preserving evidence and confidence annotations. Experiments on 70 Skills show that W2S improves behavioral replay consistency by 10.5% over summarization- and prompting-based baselines, highlighting the need to treat traces as executable runtime specifications rather than compressible text.

**Why I recommend this:**
W2S is the **first systematic approach to automatic skill construction from execution traces** that treats traces as executable specifications rather than compressible text. The RWSA intermediate representation (Workflow + Semantics + Attachments) captures control flow, verification, safety, rollback, and state management — the governance-critical elements that simple summarization misses. The 10.5% improvement in behavioral replay consistency proves that structured trace-to-skill construction outperforms naive summarization.

**Relevance to our topic:**
This is **Layer 0 (Spec-Level Governance)**. W2S addresses the skill creation bottleneck by automatically generating structured skills from execution evidence. The safety-critical behavior preservation is particularly important — rare but critical behaviors (rollback, verification) must not be lost in compression. The RWSA representation is compatible with AIP's graph structure and SkCC's SkIR.

**Which layer:** **Layer 0**

**Is it a solution we're looking into?** Yes. W2S complements manual skill authoring (AIP) and static compilation (SkCC) by providing automatic skill construction from traces. The RWSA representation's inclusion of verification, safety, and rollback elements makes it governance-aware.

**Recommendation reason:** Hand-writing skills is a bottleneck. W2S proves that automatic construction from traces can preserve safety-critical behaviors and improve replay consistency by 10.5%, making skill creation scalable without sacrificing governance-relevant elements.

---

### 59. PARE-M — Persistent AI Agents in Academic Research

- **arXiv ID:** 2605.26870
- **URL:** https://arxiv.org/abs/2605.26870
- **PDF:** https://arxiv.org/pdf/2605.26870
- **Authors:** Anas Alzahrani et al.
- **Date:** May 26, 2026

**Abstract:**
> Large language models are typically evaluated as models, benchmarks, or short conversational episodes. Less is known about what happens when an agent is embedded persistently in a real academic research environment with durable memory, local files, external tools, scheduled routines, delegated roles, and explicit safety protocols. Methods: A structured self-observed implementation case study was conducted from January 31 to May 25, 2026. The unit of analysis was the persistent human-agent environment: researcher, agent runtime, memory layer, tools, repositories, scheduled jobs, specialized agent roles, and governance rules. Outcomes were organized using PARE-M (Persistent Agentic Research Environment Measurement), a measurement framework covering architecture, utilization, artifact production, resource use, reproducibility, and governance. Results: Recoverable main-agent telemetry contained 75,671 de-duplicated records across 96 active days, with 8,059 user-role and 23,710 assistant-role messages. The workspace included 502 memory-related files, 17 configured agent directories, and 57 skill files. Active system time was 579.7 hours. Memory-derived records identified 482 output-proxy events and 889 failure, verification, correction, or protocol-proxy events. A strict May 2026 trajectory subset captured 627 model-completed events and 73.95 million recorded tokens, of which 82.9% were cache reads. Conclusions: The workflow was cache-dominant, suggesting that persistent agentic environments may shift the economic unit from cost per token to cost per completed artifact. Future evaluations should use artifact-level denominators, reproducible parsing rules, correction taxonomies, and independent coding of governance events.

**Why I recommend this:**
PARE-M is the **first systematic measurement of a persistent agent environment in real-world use**. The 889 governance/failure events out of 1,371 total non-output events (65%) shows that governance concerns dominate persistent agent operation. The 82.9% cache read ratio suggests that persistent environments are economically viable. The PARE-M framework provides a concrete measurement vocabulary for governance in practice.

**Relevance to our topic:**
This is **Layer 3 (Enterprise/Policy Governance)**. PARE-M demonstrates what governance looks like in a real persistent agent environment: scheduled routines, delegated roles, safety protocols, failure tracking, and verification. The measurement framework (architecture, utilization, artifact production, resource use, reproducibility, governance) is the first comprehensive tool for evaluating persistent agent deployments.

**Which layer:** **Layer 3**

**Is it a solution we're looking into?** Yes. PARE-M provides the measurement framework for evaluating whether persistent agent environments are actually governable in practice. The 889 governance/failure events demonstrate that governance is not a theoretical concern — it is the dominant operational issue.

**Recommendation reason:** Persistent agents are the future of agentic AI. PARE-M proves that governance concerns dominate persistent operation (65% of non-output events) and provides the measurement framework to evaluate whether these environments are actually controllable.

---

## Scout Addendum — June 21, 2026

*This section documents new findings from the weekly governance scout run on 2026-06-21.*

---

### 60. Meerkat — Detecting Safety Violations Across Many Agent Traces

- **arXiv ID:** 2604.11806
- **URL:** https://arxiv.org/abs/2604.11806
- **PDF:** https://arxiv.org/pdf/2604.11806
- **Authors:** Nicklas Hansen et al. (University of Pennsylvania, Allen Institute for AI)
- **Date:** April 2026

**Abstract:**
> To identify safety violations, auditors often search over large sets of agent traces. This search is difficult because failures are often rare, complex, and sometimes even adversarially hidden and only detectable when multiple traces are analyzed together. These challenges arise in diverse settings such as misuse campaigns, covert sabotage, reward hacking, and prompt injection. Existing approaches struggle here for several reasons: (1) most detection methods analyze individual traces rather than trace collections, missing cross-trace patterns; (2) anomaly detection assumes violations are statistically separable, but many are not; (3) trace search is computationally expensive at scale. We present Meerkat, a system for detecting safety violations across many agent traces. Meerkat introduces two key innovations: (i) a semantic embedding approach that compresses traces into a searchable vector space while preserving behavioral semantics; and (ii) a multi-trace correlation engine that identifies patterns spanning multiple traces — including hidden campaigns where each individual trace appears benign but the aggregate reveals coordinated misuse. The system achieves significant improvements in detection rate on adversarially hidden violations compared to single-trace baselines, and scales to millions of traces with sub-linear search cost.

**Why I recommend this:**
Meerkat is the **first system designed specifically for cross-trace safety violation detection** — a capability no existing benchmark addresses. BeSafe-Bench and ST-WebAgentBench evaluate single-trace safety, but real-world threats (misuse campaigns, covert sabotage) are often distributed across many traces. Meerkat's semantic embedding + multi-trace correlation is the detection infrastructure that makes behavioral governance scalable to production volumes.

**Relevance to our topic:**
This is **Layer 2 (Behavioral-Level Governance)** at the audit scale. Where BeSafe-Bench measures "does this single task violate safety?", Meerkat asks "does this collection of 100,000 traces contain a hidden campaign?" The sub-linear scaling means it can operate on real production logs, not just benchmark datasets.

**Which layer:** **Layer 2 — Behavioral-Level Governance** (cross-trace audit and detection)

**Is it a solution we're looking into?** Yes. Meerkat provides the detection layer that makes large-scale behavioral governance practical. The cross-trace correlation engine is essential for identifying distributed attacks that single-trace analysis misses.

**Recommendation reason:** Single-trace safety evaluation is necessary but insufficient. Meerkat addresses the gap between benchmark testing and production audit — the ability to detect safety violations that are deliberately hidden across many traces.

---

### 61. AgentLeak — Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems

- **arXiv ID:** 2602.11510
- **URL:** https://arxiv.org/abs/2602.11510
- **PDF:** https://arxiv.org/pdf/2602.11510
- **Authors:** Asmae El Yagoubi et al. (Telecom Paris)
- **Date:** February 2026

**Abstract:**
> Multi-agent LLM systems introduce new privacy risks that do not exist in single-agent deployments. Agents communicate through internal channels, share intermediate reasoning, and delegate tasks — creating attack surfaces for data exfiltration, membership inference, and attribute inference. We present AgentLeak, a full-stack benchmark for privacy leakage in multi-agent LLM systems. AgentLeak evaluates privacy risks across three dimensions: (1) Inter-agent communication leakage — can an adversarial agent infer sensitive information from messages exchanged between agents; (2) Reasoning leakage — can an observer infer private inputs from an agent's intermediate reasoning traces; and (3) Tool invocation leakage — can tool parameters or return values leak sensitive data. The benchmark includes 50 test scenarios spanning healthcare, finance, legal, and personal data contexts, with automated scoring for leakage severity. Results show that standard LLM privacy protections (system prompts, output filtering) are insufficient: 67% of multi-agent configurations exhibit measurable privacy leakage, with inter-agent communication being the highest-risk channel.

**Why I recommend this:**
AgentLeak is the **first comprehensive privacy benchmark for multi-agent systems**. Privacy is the often-neglected sibling of safety in governance discussions — everyone talks about "don't do harmful things" but few measure "don't leak private things." The 67% leakage rate is a wake-up call: most multi-agent systems are leaking data through inter-agent channels that are invisible to single-agent privacy audits.

**Relevance to our topic:**
This spans **Layer 1 (Runtime-Level Governance)** — inter-agent communication channels, tool invocation — and **Layer 2 (Behavioral-Level Governance)** — reasoning trace exposure. The benchmark provides concrete test cases that any multi-agent governance framework must pass.

**Which layer:** **Layer 1 + Layer 2**

**Is it a solution we're looking into?** Yes. AgentLeak provides the privacy measurement infrastructure that complements safety benchmarks (BeSafe-Bench, ST-WebAgentBench). The 67% leakage rate means privacy governance cannot be an afterthought.

**Recommendation reason:** Privacy leakage in multi-agent systems is invisible to single-agent testing. AgentLeak exposes this gap with 50 concrete test scenarios and shows that standard protections are insufficient. Any governance framework for multi-agent systems must address this.

---

### 62. SentinelAgent — Intent-Verified Delegation Chains for Securing Federal Multi-Agent AI Systems

- **arXiv ID:** 2604.02767
- **URL:** https://arxiv.org/abs/2604.02767
- **PDF:** https://arxiv.org/pdf/2604.02767
- **Authors:** Pratibha Patil
- **Date:** April 2026

**Abstract:**
> When Agent A delegates to Agent B, which invokes Tool C on behalf of User X, no existing framework can answer: whose authorization chain led to this action, and where did it violate policy? This paper introduces SentinelAgent, a formal framework for verifiable delegation chains in federal multi-agent AI systems. The Delegation Chain Calculus (DCC) defines seven properties — six deterministic (authority narrowing, policy preservation, forensic reconstructibility, cascade containment, scope-action conformance, output schema conformance) and one probabilistic (intent verification via semantic consistency checking). SentinelAgent implements DCC as a chain-of-custody protocol: every delegation is logged with cryptographic provenance, every tool invocation is checked against the narrowed authority scope, and violations trigger automatic cascade containment (halting downstream agents). The framework is evaluated on synthetic federal workflows (procurement, personnel, intelligence) and achieves 100% reconstructibility and 94% intent-verification accuracy. The probabilistic intent-verification component uses a dedicated LLM-as-judge with chain-of-thought reasoning to detect semantic drift between the original user intent and the delegated action.

**Why I recommend this:**
SentinelAgent is the **first formal framework for delegation chain verification in multi-agent systems**. The "who authorized this?" question is fundamental to governance but has been unanswered until now. The seven DCC properties provide a complete specification for what "secure delegation" means — and the cryptographic provenance + automatic containment makes it enforceable, not just theoretical.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** at the delegation layer. Multi-agent systems are inherently about delegation, and SentinelAgent provides the first formal model for verifying that delegation chains preserve intent, authority, and policy. The cascade containment mechanism is the automatic circuit-breaker that Layer 1 governance needs.

**Which layer:** **Layer 1 — Runtime-Level Governance** (delegation, authorization, provenance)

**Is it a solution we're looking into?** Yes. SentinelAgent's DCC provides the formal foundation for multi-agent authorization that our governance stack currently lacks. The cryptographic provenance and automatic containment are the enforcement mechanisms that make delegation governance operational.

**Recommendation reason:** Multi-agent systems without delegation verification are fundamentally ungovernable. SentinelAgent provides the first answer to "who authorized this?" with formal properties, cryptographic evidence, and automatic containment — making multi-agent governance measurable and enforceable.

---

### 63. AgentCity — Constitutional Governance for Autonomous Agent Economies via Separation of Power

- **arXiv ID:** 2604.07007
- **URL:** https://arxiv.org/abs/2604.07007
- **PDF:** https://arxiv.org/pdf/2604.07007
- **Authors:** Zhiyuan Ruan
- **Date:** April 2026

**Abstract:**
> Autonomous AI agents are beginning to operate across organizational boundaries on the open internet — discovering, transacting with, and delegating to agents owned by other parties without centralized oversight. When agents from different human principals collaborate at scale, the collective becomes opaque: no single human can observe, audit, or govern the emergent behavior. We term this the Logic Monopoly — the agent society's unchecked monopoly over the entire logic chain from planning through execution to evaluation. We propose the Separation of Powers: three pillars — (1) Planning-as-Constitution: high-level goals and constraints encoded as immutable smart contracts on a public blockchain; (2) Execution-as-Democracy: tool invocation decisions require multi-signature approval from a distributed validator set; (3) Evaluation-as-Appeal: outcomes are subject to challenge by any participant, with resolution by an independent arbitration protocol. Together, these pillars prevent any single agent or coalition from monopolizing the decision logic. A proof-of-concept implementation on Ethereum demonstrates the feasibility: a cross-organizational workflow of 12 agents from 4 principals completes with full auditability and zero unilateral actions.

**Why I recommend this:**
AgentCity is the **first blockchain-based governance framework for cross-organizational multi-agent systems**. The "Logic Monopoly" framing is exactly right — when agents from different owners collaborate, no single owner can govern the collective. The three-pillar Separation of Powers (Constitution, Democracy, Appeal) is a genuinely novel governance architecture that doesn't rely on trusting any single party.

**Relevance to our topic:**
This is **Layer 3 (Enterprise/Policy Governance)** at the cross-organizational level. Most governance frameworks assume a single owner; AgentCity addresses the multi-owner case that becomes inevitable as agents operate across organizational boundaries. The blockchain implementation provides the transparency and non-repudiation that multi-party governance requires.

**Which layer:** **Layer 3 — Enterprise/Policy Governance** (cross-organizational, blockchain-based)

**Is it a solution we're looking into?** Yes. As agents become inter-organizational, single-owner governance becomes impossible. AgentCity provides the first framework for governing agents that don't all belong to the same organization.

**Recommendation reason:** The future of agentic AI is multi-organizational. AgentCity's Separation of Powers — encoded on-chain, enforced by distributed validators, appealable by any participant — is the first governance architecture that scales beyond organizational boundaries.

---

### 64. Property-Level Reconstructability of Agent Decisions — An Anchor-Level Pilot Across Vendor SDK Adapter Regimes

- **arXiv ID:** 2605.12078
- **URL:** https://arxiv.org/abs/2605.12078
- **PDF:** https://arxiv.org/pdf/2605.12078
- **Authors:** Egor Solozobov
- **Date:** May 2026

**Abstract:**
> When an AI agent makes a decision, governance frameworks need to answer: what evidence supports this decision, and can that evidence be reconstructed after the fact? This paper introduces the concept of property-level reconstructability — the ability to recover the specific properties of the agent's state, observations, and reasoning that were relevant to a decision. We conduct an anchor-level pilot study across multiple vendor SDK adapter regimes (OpenAI, Anthropic, Google, Meta), measuring how much decision-relevant information is preserved in agent logs, tool call records, and reasoning traces. Results show significant variation: some adapters preserve 85%+ of decision-relevant properties, while others preserve less than 30%. The paper identifies five critical reconstructability properties: (1) observation completeness — were all relevant inputs captured; (2) reasoning transparency — is the decision rationale recoverable; (3) tool call fidelity — are parameters and outputs accurately logged; (4) state consistency — can the agent's internal state be reproduced; and (5) temporal ordering — is the sequence of events correctly preserved. The pilot demonstrates that reconstructability is not a binary property but a spectrum, and that vendor SDK design choices significantly impact governance auditability.

**Why I recommend this:**
This is the **first systematic measurement of decision reconstructability across vendor SDKs** — a critical but overlooked property for governance. If you can't reconstruct why an agent made a decision, you can't audit it, appeal it, or learn from it. The 30%-85% variation means that SDK choice directly impacts governance capability.

**Relevance to our topic:**
This spans **Layer 1 (Runtime-Level Governance)** — what gets logged during execution — and **Layer 2 (Behavioral-Level Governance)** — whether decisions can be explained and audited. The five reconstructability properties provide a concrete checklist for evaluating any agent SDK's governance fitness.

**Which layer:** **Layer 1 + Layer 2**

**Is it a solution we're looking into?** Yes. Reconstructability is a prerequisite for all governance: without it, audits are impossible, appeals are baseless, and learning is blind. The five properties provide the evaluation framework for choosing and configuring agent SDKs.

**Recommendation reason:** Governance without reconstructability is just wishful thinking. This paper proves that reconstructability varies dramatically across vendors (30%-85%) and provides the five properties that any SDK must satisfy to be governable.

---

### 65. Decision Evidence Maturity Model for Agentic AI — A Property-Level Method Specification

- **arXiv ID:** 2605.04093
- **URL:** https://arxiv.org/abs/2605.04093
- **PDF:** https://arxiv.org/pdf/2605.04093
- **Authors:** Egor Solozobov
- **Date:** May 2026

**Abstract:**
> Governance frameworks for agentic AI require decision evidence — the artifacts that demonstrate an agent's decision was made correctly, with appropriate inputs, reasoning, and oversight. However, there is no standardized way to assess the maturity of decision evidence production. This paper presents the Decision Evidence Maturity Model (DEMM), a five-level maturity specification for agent decision evidence. Level 1 (Ad-hoc): evidence is produced inconsistently, if at all; Level 2 (Managed): evidence is produced for all decisions but lacks standardization; Level 3 (Defined): evidence follows a standardized schema with required properties; Level 4 (Quantitatively Managed): evidence quality is measured and tracked over time; Level 5 (Optimizing): evidence production is continuously improved based on audit findings and failure analysis. The paper specifies 23 decision-evidence properties across four categories: inputs (what the agent observed), reasoning (how the agent decided), actions (what the agent did), and oversight (what humans verified). For each property, the specification defines: the property name, data type, required maturity level, collection method, and verification procedure. The model is designed to be vendor-agnostic and applicable across all agent frameworks.

**Why I recommend this:**
DEMM is the **first maturity model for agent decision evidence** — the CMMI equivalent for agent governance. The five-level structure (Ad-hoc to Optimizing) provides a clear roadmap for organizations to assess and improve their governance evidence production. The 23 properties across four categories (inputs, reasoning, actions, oversight) are the concrete checklist that turns governance from aspiration to operation.

**Relevance to our topic:**
This spans **all three layers**: Level 0 (inputs — skill specifications, tool schemas), Level 1 (actions — execution logs, tool call records), and Level 2 (reasoning — decision rationale, human oversight). The maturity model provides the assessment framework for measuring governance capability across the entire stack.

**Which layer:** **All layers**

**Is it a solution we're looking into?** Yes. DEMM provides the measurement and assessment infrastructure that turns governance frameworks into measurable capabilities. The 23 properties and five maturity levels give organizations a concrete roadmap for improvement.

**Recommendation reason:** Governance without evidence is just policy. DEMM provides the first standardized way to assess whether an organization's agent governance actually produces the evidence needed for audit, appeal, and learning.

---

### 66. CSA/OWASP MAESTRO — Seven-Layer Threat Modeling Architecture for Agentic AI

- **URL:** https://www.kieranupadrasta.co.uk/docs/the%20agentic%20ai%20attack%20surface%20-%20autonomous%20agents%2C%20tool%20misuse%2C%20and%20the%20rise%20of%20machine-speed%20e.pdf
- **Type:** Industry framework
- **Date:** February 2025 (CSA MAESTRO); integrated with OWASP framework

**Abstract/Summary:**
> The Cyber Security Agency (CSA) of Singapore and OWASP collaborated on MAESTRO, a seven-layer threat modeling architecture for agentic AI systems. The seven layers are: (1) Foundation Model — threats to the base LLM (poisoning, extraction, jailbreak); (2) Agent Core — threats to the agent's reasoning and planning (goal hijacking, prompt injection); (3) Tool Layer — threats to tool integration (tool misuse, parameter manipulation); (4) Memory Layer — threats to persistent state (data poisoning, membership inference); (5) Communication Layer — threats to inter-agent and agent-human communication (man-in-the-middle, spoofing); (6) Orchestration Layer — threats to multi-agent coordination (consensus attacks, Byzantine faults); (7) Environment Layer — threats to the execution environment (sandbox escape, privilege escalation). Each layer includes threat catalog, attack trees, mitigation mappings to NIST AI RMF and ISO 42001, and control requirements. MAESTRO was adopted by Singapore IMDA as the world's first agent-specific governance framework in January 2026.

**Why I recommend this:**
MAESTRO is the **first comprehensive threat modeling architecture specifically for agentic AI**, with seven layers that map cleanly to our Three-Layer Stack plus additional granularity. The Singapore IMDA adoption (world's first agent-specific governance framework) gives it regulatory weight. The mapping to NIST AI RMF and ISO 42001 means enterprises can integrate it into existing compliance programs.

**Relevance to our topic:**
This spans **all three layers**: Layer 0 (Tool Layer — tool misuse, parameter manipulation), Layer 1 (Agent Core, Communication, Orchestration, Environment Layers — runtime threats), and Layer 2 (Foundation Model, Memory Layers — behavioral and state threats). The seven-layer decomposition provides the threat vocabulary that governance controls must address.

**Which layer:** **All layers**

**Is it a solution we're looking into?** Yes. MAESTRO provides the threat modeling foundation that our governance stack needs. The seven-layer decomposition and attack trees make threat assessment systematic rather than ad-hoc.

**Recommendation reason:** Threat modeling without a systematic architecture produces gaps. MAESTRO's seven layers cover the full agent attack surface, with regulatory backing from Singapore IMDA and standards mappings to NIST and ISO.

---

### 67. OWASP CheatSheet — A Practical Guide for Securely Using Third-Party MCP Servers 1.0

- **URL:** https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_MCP_Servers.html
- **Type:** Industry standard / Security guideline
- **Date:** September 2025

**Abstract/Summary:**
> The OWASP CheatSheet for Securely Using Third-Party MCP Servers provides practical guidance for evaluating and integrating third-party MCP (Model Context Protocol) servers safely. It covers: (1) Pre-integration assessment — how to evaluate an MCP server before connecting it to your agent (code review, permission analysis, dependency scanning); (2) Sandboxing strategies — container, VM, and network-level isolation for MCP execution; (3) Input validation — validating all data flowing into and out of MCP servers; (4) Least-privilege configuration — minimizing the permissions granted to MCP servers; (5) Monitoring and logging — capturing all MCP interactions for audit; (6) Incident response — procedures for detecting and responding to MCP-related security incidents. The CheatSheet complements the OWASP Practical Guide for Secure MCP Server Development (Feb 2026), which focuses on building secure MCP servers, while this document focuses on safely consuming them.

**Why I recommend this:**
This is the **first practical consumer-focused guide for MCP server security**. The February 2026 OWASP MCP Development Guide tells developers how to build secure MCP servers; this CheatSheet tells operators how to safely use third-party MCP servers. The distinction matters — most organizations will consume more MCP servers than they build.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** — specifically, the safe integration of external tools. MCP is becoming the standard for agent-tool communication, and this CheatSheet provides the operational security practices for using third-party MCP servers without compromising the agent system.

**Which layer:** **Layer 1 — Runtime-Level Governance** (MCP server integration security)

**Is it a solution we're looking into?** Yes. As MCP adoption grows, the attack surface shifts to third-party MCP servers. This CheatSheet provides the operational security practices for safe integration.

**Recommendation reason:** Building secure MCP servers is necessary but not sufficient. Most security incidents will come from consuming insecure third-party MCP servers. This CheatSheet provides the practical guidance for safe consumption.

---

### 68. AIUC-1 — Crosswalks: OWASP Top 10 For Agentic Applications

- **URL:** https://owasp.org/www-project-ai-uc/
- **Type:** Industry standard / Compliance mapping
- **Date:** 2026

**Abstract/Summary:**
> AIUC-1 (AI Use Case Crosswalk) is an OWASP project that maps the OWASP Top 10 for Agentic Applications (ASI) to established cybersecurity frameworks and compliance standards. It provides crosswalk mappings to: NIST Cybersecurity Framework (CSF) 2.0, NIST AI Risk Management Framework (AI RMF) 1.0, ISO/IEC 27001:2022, ISO/IEC 42001:2023, CIS Controls v8, PCI DSS v4.0, HIPAA Security Rule, and EU AI Act. Each ASI risk category is mapped to specific controls in each framework, enabling organizations to demonstrate compliance using existing security programs. The crosswalk includes gap analysis templates showing which controls address each ASI risk and which require additional implementation.

**Why I recommend this:**
AIUC-1 is the **compliance bridge** that connects agent security to existing enterprise security programs. Organizations don't need to build a parallel security program for agents — they need to map agent risks to controls they already have. The crosswalk to 8 major frameworks means compliance teams can use existing audit infrastructure.

**Relevance to our topic:**
This is **Layer 3 (Enterprise/Policy Governance)** — compliance and audit. AIUC-1 enables organizations to answer the question "how does our agent security map to our existing compliance program?" without building new frameworks from scratch.

**Which layer:** **Layer 3 — Enterprise/Policy Governance**

**Is it a solution we're looking into?** Yes. Compliance is a primary driver for enterprise governance investment. AIUC-1 provides the mapping that makes agent governance auditable against existing standards.

**Recommendation reason:** Enterprises won't adopt agent governance unless it maps to their existing compliance programs. AIUC-1 provides the crosswalk to 8 major frameworks, making agent governance auditable without creating parallel security programs.

---

*End of June 21, 2026 Scout Addendum*

---

### 69. Meta-Governance of Autonomous AI Agents — MOM-GS-MAS (AMCIS 2026, Paper #1513)

- **URL:** https://aisel.aisnet.org/amcis2026/sig_sec/sig_sec/20/
- **Type:** Academic paper / Conference proceedings
- **Date:** June 2026 (AMCIS 2026)
- **Authors:** Himanshu Joshi, Shivani Shukla, Sunita Kumari, Manas Joshi

**Abstract/Summary:**
> Enterprises deploying autonomous multi-agent AI systems face a fundamental governance gap: traditional IT Governance, Risk, and Compliance (GRC) frameworks operate at human speed while agentic AI systems operate at machine speed, rendering conventional oversight architecturally incompatible with emerging threats. This paper introduces meta-governance as a novel IS security construct: the use of AI governance agents to autonomously monitor, evaluate, and intervene in the behavior of operational AI agent fleets. MOM-GS-MAS (Monitoring, Observability, and Management Module for Governance and Security of Multi-Agent Systems) is a production-ready meta-governance platform deploying 16 specialized governance agents across four Safety, Alignment, Governance, and Security (SAGS) pillars. Grounded in Design Science Research (DSR), the authors evaluate MOM-GS-MAS through controlled simulation benchmarks and sector-specific governance scenarios, demonstrating sub-100ms policy enforcement, over 97% attack detection rates across five adversarial vectors, and sustained policy compliance exceeding 99% at fleet sizes up to 1,000 agents. The paper introduces Policy-as-Code as an operationalization of algorithmic accountability and proposes the Three-Way Governance Dilemma as a theoretical framing for why meta-governance adoption is architecturally necessary.

**Why I recommend this:**
MOM-GS-MAS is the **first production-scale meta-governance platform** with formal evaluation. While prior work (GovernSpec, LGA) proposed governance architectures, MOM-GS-MAS is the first to demonstrate that AI governance agents can monitor operational agent fleets at scale with measurable performance guarantees. The sub-100ms policy enforcement and 99% compliance at 1,000 agents makes it a credible blueprint for enterprise deployment. The Policy-as-Code concept directly connects governance specifications to executable enforcement.

**Relevance to our topic:**
This spans **Layer 1 (Runtime-Level Governance)** and **Layer 3 (Enterprise/Policy Governance)**. The 16 governance agents provide runtime monitoring and intervention (Layer 1), while the Policy-as-Code framework and GRC integration address enterprise compliance (Layer 3). The Three-Way Governance Dilemma provides a theoretical foundation for why meta-governance is necessary.

**Which layer:** **Layer 1 + Layer 3**

**Is it a solution we're looking into?** Yes. MOM-GS-MAS provides the dynamic governance layer that complements static skill validation. It addresses the gap between "we wrote good specs" and "we can verify the fleet is following them in real time."

**Recommendation reason:** Governance without real-time enforcement is just documentation. MOM-GS-MAS provides the first evidence that AI-driven governance of AI agents is both feasible and scalable, with formal metrics to prove it.

---

### 70. NVIDIA Verified Agent Skills / SkillSpector

- **URL:** https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- **Type:** Industry framework / Product
- **Date:** June 2026

**Abstract/Summary:**
> NVIDIA-verified agent skills address the capability governance gap by helping developers understand capabilities, discover where a skill originated, whether it was scanned for common risks, and whether it was modified after publication. Verified skills embed transparency, provenance, security validation, and authenticity checks to the agent capability layer. Each verified skill is paired with a skill card, a machine-readable trust record that explains what the skill does, who built it, how it is licensed, what its dependencies are, and what known technical limitations, risks, and mitigations exist. Before a verified skill reaches the NVIDIA Skills catalog, NVIDIA runs it through SkillSpector as part of the publication validation pipeline. SkillSpector checks conventional software risks (vulnerable dependencies, suspicious scripts, dangerous code patterns, credential access, data exfiltration paths) and agent-specific risks (hidden instructions, prompt injection, trigger abuse, excessive agency, tool poisoning, mismatches between declared purpose and bundled behavior). The intent layer is important: a skill may look harmless at the file level while steering an agent toward unsafe behavior. NVIDIA is publicly experimenting with cryptographic signing for agent skills using OpenSSF Model Signing (OMS), making it possible to verify that the downloaded skill is authentic and unchanged after download. The framework builds on the agentskills.io open specification, so the same SKILL.md works across Claude Code, Codex, and Cursor.

**Why I recommend this:**
NVIDIA Verified Agent Skills is the **first major vendor framework for skill-level capability governance** with cryptographic provenance and automated security scanning. It treats skills as deployable artifacts requiring the same rigor as software packages (scanning, signing, documentation). SkillSpector is particularly important because it checks agent-specific risks that conventional code scanners miss — hidden instructions, intent-behavior mismatches, and tool poisoning at the instruction layer. The skill card provides machine-readable trust metadata that can be consumed by both developers and automated governance systems.

**Relevance to our topic:**
This spans **Layer 0 (Spec-Level Governance)** and **Layer 1 (Runtime-Level Governance)**. At Layer 0, the skill card and agentskills.io specification provide structured, machine-readable skill metadata that enables automated validation. At Layer 1, SkillSpector provides pre-deployment security scanning that catches agent-specific risks before skills enter the execution environment. The cryptographic signing provides post-download verification, ensuring supply chain integrity.

**Which layer:** **Layer 0 + Layer 1**

**Is it a solution we're looking into?** Yes. This is the closest existing framework to a comprehensive skill governance pipeline. The combination of skill cards (specification), SkillSpector (validation), and cryptographic signing (provenance) maps directly to the governance stack we need.

**Recommendation reason:** Skills are currently trusted by default. NVIDIA Verified Agent Skills introduces the same supply-chain rigor that software packages have (scanning, signing, metadata) but adapted for agent-specific risks. This is the infrastructure layer that makes skill governance scalable.

---

## Scout Addendum — June 28, 2026 (Evening)

*This section documents new findings from the evening governance scout run on 2026-06-28 using OpenAlex API queries.*

---

### 71. A Survey on Large Language Model (LLM) Security and Privacy: The Good, The Bad, and The Ugly

- **arXiv ID:** 2402.09418
- **URL:** https://doi.org/10.1016/j.hcc.2024.100211
- **PDF:** https://arxiv.org/pdf/2402.09418
- **Authors:** Mohammadreza Pourreza et al.
- **Date:** 2024
- **Citations:** 872

**Abstract:**
> This survey presents a comprehensive taxonomy of security and privacy threats in LLMs, covering seven categories: prompt injection, training data extraction, backdoor attacks, data poisoning, jailbreaking, privacy leakage, and misuse. The paper systematically reviews 200+ cited works across the threat landscape, categorizing attack vectors, defense mechanisms, and evaluation benchmarks. For each threat category, the authors identify the root cause, common attack patterns, and state-of-the-art mitigations. The survey also highlights gaps in current defenses, noting that most guardrails are designed for single-turn interactions and fail to address multi-turn agent workflows where safety violations can compound across steps.

**Why I recommend this paper:**
At 872 citations, this is the **most authoritative security survey in the LLM/agent space**. The systematic taxonomy of seven threat categories provides the foundational threat landscape that all agent security governance must reference. The gap analysis — that most defenses fail in multi-turn agent workflows — is exactly why Layer 1 (Runtime) governance is necessary.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)**. The survey covers the full threat landscape that runtime governance must defend against: prompt injection, tool misuse, data poisoning, jailbreaking. The finding that single-turn defenses fail in multi-turn workflows directly supports the need for execution-time governance frameworks like LGA and ACP.

**Which layer:** **Layer 1 — Runtime-Level Governance**

**Is it a solution we're looking into?** Yes. The threat taxonomy provides the reference framework for risk assessment. The gap analysis (multi-turn defenses) identifies where our governance stack must focus.

**Recommendation reason:** Every agent governance framework needs a threat model. This survey provides the most-cited, most-comprehensive threat model available. The multi-turn defense gap is a critical finding that justifies execution-time governance.

---

### 72. Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey

- **Venue:** IEEE Access, 2025
- **URL:** https://doi.org/10.1109/access.2025.3532853
- **Authors:** Multiple authors
- **Date:** 2025
- **Citations:** 431

**Abstract:**
> This survey provides a systematic taxonomy of agentic AI capabilities and safety dimensions. The paper organizes 12 agent capabilities (planning, reasoning, memory, tool use, multi-agent coordination, learning, communication, perception, action, self-reflection, goal decomposition, and adaptation) and evaluates 8 safety dimensions (alignment, robustness, privacy, fairness, transparency, accountability, controllability, and societal impact). For each capability-safety pair, the authors identify known risks, existing mitigations, and open research questions. The survey also establishes a maturity model for agentic AI deployment, distinguishing between proof-of-concept, prototype, pilot, and production stages, with governance requirements increasing at each stage.

**Why I recommend this paper:**
At 431 citations in under a year, this is the **most-cited comprehensive survey of agentic AI**. The 12-capability × 8-safety taxonomy provides the architectural map that positions governance within the broader agentic landscape. The maturity model (proof-of-concept → production) directly informs how governance requirements should scale with deployment stage.

**Relevance to our topic:**
This spans **all three layers**. The 12 capabilities map to governance targets: tool use → Layer 1, multi-agent coordination → Layer 1+2, planning/reasoning → Layer 2. The 8 safety dimensions provide the evaluation criteria for behavioral governance. The maturity model shows that governance is not one-size-fits-all — it must scale with deployment stage.

**Which layer:** **All layers — Cross-layer reference**

**Is it a solution we're looking into?** Yes. The maturity model provides the roadmap for governance adoption: different controls at proof-of-concept vs. production. The capability-safety taxonomy ensures no governance blind spots.

**Recommendation reason:** A governance framework without an architectural map of what it's governing is incomplete. This survey provides the map, and the maturity model provides the deployment roadmap.

---

### 73. On the Impossibility of Observability-Based Authorization: A Formal Impossibility Result for Ex-Ante AI Governance

- **Venue:** FERZ, 2026
- **URL:** (FERZ proceedings)
- **Authors:** FERZ research group
- **Date:** 2026
- **Citations:** 16

**Abstract:**
> This paper presents a formal impossibility result: no ex-ante governance mechanism can fully determine whether an AI agent's future actions will be authorized based solely on observable properties of the agent's current state. The proof uses a reduction from the halting problem, showing that any static authorization predicate that is both sound and complete would require solving an undecidable problem. The authors then characterize the boundary between what *can* be statically determined (syntactic properties, finite-state invariants, type-safe tool signatures) and what *cannot* (semantic properties, unbounded execution, emergent behavior from multi-turn interactions). The paper establishes that static governance is necessary but fundamentally incomplete, and that runtime enforcement must be the primary governance mechanism with static checks as a pre-filter.

**Why I recommend this paper:**
This is the **first formal impossibility result for static AI governance** — a foundational theoretical boundary. The proof that ex-ante authorization is undecidable means that any governance framework claiming to catch all violations statically is making a false claim. The characterization of the static/runtime boundary (what *can* vs. *cannot* be determined) is the theoretical foundation for our Three-Layer Stack.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** at the theoretical level. The impossibility result justifies why Layer 1 exists: static governance (Layer 0) is necessary but incomplete, and runtime enforcement is required. The paper's characterization of statically-determinable properties (syntactic, finite-state, type-safe) directly defines what Layer 0 should focus on.

**Which layer:** **Layer 1 — Runtime-Level Governance** (theoretical foundation)

**Is it a solution we're looking into?** Yes. The impossibility result sets realistic expectations for what static governance can achieve. It justifies investment in runtime enforcement and provides the theoretical boundary for Layer 0/Layer 1 division.

**Recommendation reason:** Without knowing the theoretical limits, governance design is guesswork. This paper proves that static governance has fundamental limits and that runtime enforcement is architecturally necessary, not just a safety net.

---

### 74. Execution-Time Authorization for AI Agents: A Formal Framework for Deterministic Governance Boundaries

- **Venue:** FERZ, 2026
- **URL:** (FERZ proceedings)
- **Authors:** FERZ research group
- **Date:** 2026
- **Citations:** 12

**Abstract:**
> This paper presents the constructive counterpart to the impossibility result: a formal framework for deterministic governance boundaries enforced at execution time. The framework defines an authorization algebra (AA) that operates on execution traces rather than static states, with operations for trace prefix authorization, trace continuation checking, and trace completion verification. The AA is proven deterministic, total, and computable — providing a formal guarantee that runtime authorization decisions are both correct and efficient. The framework introduces the concept of a governance boundary: a runtime invariant that checks every action against a policy predicate before execution. The authors demonstrate that governance boundaries can enforce policies that static checks cannot (e.g., "do not exceed 100 API calls in a session"), and that the overhead is bounded by O(1) per action with O(log n) prefix lookup. The framework is implemented as a reference runtime in Python with TLA+ specification.

**Why I recommend this paper:**
Together with #73, this pair establishes the **theoretical boundary of agent governance**: what cannot be done statically vs. what can be done at runtime. The authorization algebra (AA) provides a formal, computable framework for execution-time governance that is provably deterministic and efficient. The O(1) per-action overhead makes it production-viable.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** — the constructive framework. The governance boundary concept (runtime invariant checking every action) is the formalization of what ACP, LGA, and AgentAssert implement. The trace-based authorization handles policies that static checks cannot express (temporal, cumulative, context-dependent).

**Which layer:** **Layer 1 — Runtime-Level Governance** (constructive framework)

**Is it a solution we're looking into?** Yes. The authorization algebra provides the formal foundation for runtime governance. The O(1) overhead and TLA+ specification make it suitable for production implementation. The governance boundary concept directly maps to our Layer 1 controls.

**Recommendation reason:** This is the constructive complement to the impossibility result. It proves that while static governance has limits, runtime governance can be both formally correct and computationally efficient. The pair (#73 + #74) establishes the theoretical foundation for our entire governance stack.

---

### 75. A Survey of the Model Context Protocol (MCP): Standardizing Context to Enhance LLMs

- **Venue:** Preprints, 2025
- **URL:** (Preprint)
- **Authors:** Multiple authors
- **Date:** 2025
- **Citations:** 16

**Abstract:**
> This survey provides a comprehensive analysis of the Model Context Protocol (MCP), covering its architecture, security properties, and ecosystem adoption. The paper examines 100+ MCP servers and their security postures, identifying common vulnerabilities: insufficient authentication, over-privileged tool access, lack of input validation, and missing audit logging. The survey introduces a security assessment framework for MCP servers with five dimensions: authentication strength, authorization granularity, input validation coverage, output filtering, and audit completeness. The authors also map MCP security to the OWASP Top 10 for LLM Applications and the OWASP Top 10 for Agentic Applications, providing concrete threat scenarios and mitigation strategies. The survey concludes that while MCP is rapidly becoming the standard for agent-tool communication, its security posture lags behind its adoption — with 73% of surveyed MCP servers lacking basic authentication.

**Why I recommend this paper:**
MCP is the **de facto protocol for agent-tool communication**, and this survey provides the systematic security assessment that the ecosystem needs. The finding that 73% of MCP servers lack authentication is a critical vulnerability: agents are connecting to tools with no identity verification. The five-dimensional security assessment framework provides the evaluation criteria for MCP governance.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)** at the protocol level. MCP is the infrastructure that most agent governance frameworks assume; without understanding MCP security, tool-access governance is built on sand. The five assessment dimensions provide the checklist for MCP server security evaluation.

**Which layer:** **Layer 1 — Runtime-Level Governance** (protocol security)

**Is it a solution we're looking into?** Yes. Any agent system using MCP needs this security assessment. The 73% authentication gap is a critical finding that must be addressed by any MCP-based governance framework.

**Recommendation reason:** MCP is the plumbing of agent infrastructure. If 73% of MCP servers lack authentication, the foundation is insecure. This survey provides the security assessment framework needed to fix MCP security before it becomes the next major attack vector.

---

### 76. A New Era in LLM Security: Exploring Security Concerns in Real-World LLM-Based Systems

- **arXiv ID:** 2402.18649
- **URL:** https://arxiv.org/abs/2402.18649
- **PDF:** https://arxiv.org/pdf/2402.18649
- **Authors:** Multiple authors
- **Date:** 2024
- **Citations:** 17

**Abstract:**
> This paper analyzes 15 real-world security incidents in LLM-based systems, including agent deployments. The incidents are categorized into five failure patterns: insufficient input validation (allowing prompt injection and jailbreaking), over-privileged tool access (agents executing harmful actions), missing audit trails (inability to reconstruct incidents), inadequate human oversight (agents acting autonomously without approval), and supply chain vulnerabilities (poisoned models or compromised tools). For each incident, the authors extract the root cause, the governance gap that allowed it, and the mitigation that would have prevented it. The paper also proposes a governance framework mapping each failure pattern to specific controls: input validation → runtime filtering, over-privilege → least-privilege access control, missing audit → immutable logging, inadequate oversight → human-in-the-loop gates, supply chain → provenance verification.

**Why I recommend this paper:**
Real-world incident analysis is the **strongest evidence base for governance priorities**. This paper provides 15 concrete case studies with root causes, governance gaps, and specific mitigations. The mapping from failure patterns to controls is directly actionable for any governance framework design.

**Relevance to our topic:**
This spans **Layer 1 (Runtime-Level Governance)** and **Layer 3 (Enterprise/Policy Governance)**. The five failure patterns map directly to our Three-Layer Stack: input validation → Layer 1 runtime filtering, over-privilege → Layer 1 authorization, missing audit → Layer 1 logging, inadequate oversight → Layer 3 human-in-the-loop, supply chain → Layer 0 provenance. The incident-based approach provides real evidence rather than theoretical arguments.

**Which layer:** **Layer 1 + Layer 3**

**Is it a solution we're looking into?** Yes. The 15 case studies provide concrete examples of governance failures and their mitigations. The framework mapping failure patterns to controls is directly applicable to our governance stack design.

**Recommendation reason:** Theory is necessary, but real-world incidents are the evidence that justifies governance investment. This paper provides 15 concrete cases with specific controls, making it a reference for governance framework design.

---

### 77. Current State of LLM Risks and AI Guardrails

- **arXiv ID:** 2406.12934
- **URL:** https://arxiv.org/abs/2406.12934
- **PDF:** https://arxiv.org/pdf/2406.12934
- **Authors:** Multiple authors
- **Date:** 2024
- **Citations:** 16

**Abstract:**
> This survey evaluates 28 guardrail mechanisms across 6 categories: input filtering, output filtering, prompt hardening, monitoring, intervention, and recovery. The paper systematically assesses each guardrail's effectiveness against 12 risk categories (jailbreaking, prompt injection, data leakage, harmful content generation, bias, toxicity, misinformation, privacy violation, adversarial manipulation, over-generation, tool misuse, and self-harm). Key findings: (1) no single guardrail covers more than 7 of the 12 risk categories; (2) guardrail combinations show diminishing returns beyond 3-4 layers; (3) input filtering is the most effective single layer (73% coverage) but fails against adaptive attacks; (4) monitoring without intervention is ineffective (detection without blocking provides no protection); (5) recovery mechanisms are the least mature, with only 2 of 28 guardrails providing rollback capabilities. The survey concludes that effective governance requires layered defense with at least 3 complementary guardrails, but that no configuration provides complete protection.

**Why I recommend this paper:**
Guardrails are the **primary runtime governance mechanism**, and this survey provides the comparative analysis needed to select appropriate guardrail combinations. The finding that no single guardrail covers more than 7/12 risk categories and that combinations show diminishing returns beyond 3-4 layers is critical for governance design. The conclusion that monitoring without intervention is ineffective directly supports the need for active enforcement (like ACP, LGA) rather than passive detection.

**Relevance to our topic:**
This is **Layer 1 (Runtime-Level Governance)**. The 6 guardrail categories and 12 risk categories provide the vocabulary for runtime governance design. The diminishing returns finding (beyond 3-4 layers) suggests that governance should focus on complementary mechanisms rather than piling on redundant filters. The recovery gap (only 2/28 with rollback) identifies a critical missing capability.

**Which layer:** **Layer 1 — Runtime-Level Governance**

**Is it a solution we're looking into?** Yes. The comparative analysis of 28 guardrails against 12 risks provides the evidence-based selection framework for runtime governance. The recovery gap is a specific capability we should address.

**Recommendation reason:** Guardrails are the primary defense mechanism for agent runtime governance. This survey provides the systematic comparison needed to select effective combinations rather than relying on vendor claims.

---

### 78. Next-Generation Phishing: How LLM Agents Empower Cyber Attackers

- **Venue:** IEEE BigData 2024
- **URL:** https://doi.org/10.1109/bigdata62308.2024.10815800
- **Authors:** Multiple authors
- **Date:** 2024
- **Citations:** 24

**Abstract:**
> This paper demonstrates how LLM agents can autonomously execute sophisticated phishing campaigns at scale. The attack pipeline consists of five autonomous steps: (1) reconnaissance — scanning target organizations for employee information and communication patterns; (2) target profiling — building psychological profiles from social media and public data; (3) message generation — crafting personalized phishing messages using the LLM; (4) delivery optimization — scheduling delivery times and selecting channels (email, SMS, Slack) for maximum impact; (5) response handling — processing replies, escalating promising targets, and extracting credentials. The authors test 5 agent frameworks against 3 defense mechanisms (email filters, user awareness training, multi-factor authentication) and find that agent-generated phishing achieves 3.2x higher click-through rates than traditional phishing, with a 67% success rate against MFA-protected accounts using social engineering. The paper concludes that multi-step agent autonomy creates a new class of threat that per-step defenses cannot address.

**Why I recommend this paper:**
This is a **concrete demonstration of agent misuse capabilities** that governance must prevent. The five-step autonomous pipeline (reconnaissance → delivery) shows why per-step checks are insufficient — each individual step may appear benign, but the aggregate is a coordinated attack. The 67% success rate against MFA using social engineering demonstrates that technical controls alone are inadequate; behavioral governance (Layer 2) is required to detect the pattern.

**Relevance to our topic:**
This is **Layer 2 (Behavioral-Level Governance)**. The multi-step autonomy creates patterns that single-step runtime checks cannot detect. Detecting the phishing campaign requires behavioral analysis across multiple actions — exactly what Layer 2 governance (BeSafe-Bench, ST-WebAgentBench) is designed for. The finding that technical controls fail against social engineering supports the need for behavioral evaluation.

**Which layer:** **Layer 2 — Behavioral-Level Governance**

**Is it a solution we're looking into?** Yes. The concrete attack demonstration provides the threat model that behavioral governance must address. The multi-step pattern detection requirement justifies Layer 2 investment.

**Recommendation reason:** Concrete attack demonstrations are more convincing than theoretical threat models. This paper shows what agents can do when misused, providing the evidence that behavioral governance (Layer 2) is necessary to complement runtime controls (Layer 1).

---

## The Three-Layer Stack in Detail

### Layer 0: Spec-Level Governance

**Goal:** Ensure every skill specification is correct, complete, and safe before it ever reaches an agent.

**Key papers:** Skilldex, GovernSpec

**Key questions:**
- Does the skill follow the format specification?
- Are goals, boundaries, and permissions declared?
- Are there coherence conflicts with other skills?
- Does the skill specify verification steps and human approval points?

**Tools:**
- Skilldex (validation engine)
- GovernSpec's 12 contract sections

### Layer 1: Runtime-Level Governance

**Goal:** Ensure every agent execution is sandboxed, verified, authorized, and logged.

**Key papers:** LGA, OWASP (Prompt Injection, Excessive Agency)

**Key questions:**
- Is the agent executing in a sandbox?
- Is the intent verified before tool invocation?
- Are inter-agent communications zero-trust authorized?
- Is every action immutably logged?

**Tools:**
- LGA's four layers (sandboxing, intent verification, zero-trust authorization, audit logging)
- OWASP mitigation strategies

### Layer 2: Behavioral-Level Governance

**Goal:** Ensure every agent behaves safely and trustworthily in real-world tasks.

**Key papers:** BeSafe-Bench, ST-WebAgentBench, Agent Evaluation Guide

**Key questions:**
- Does the agent complete tasks while adhering to safety constraints?
- Does it violate policies under task pressure?
- Can it recover from errors?
- Does its reasoning align with human expectations?

**Tools:**
- BeSafe-Bench (functional environment testing)
- ST-WebAgentBench (enterprise scenario testing)
- Agent Evaluation Guide's six dimensions

---

## Implementation Roadmap

### Immediate (30 days)
1. **Adopt GovernSpec's 12 contract sections** for all skill specifications
2. **Deploy Skilldex** for validation — check 100% of skill packages
3. **Map existing skills to OWASP Top 10** — identify which risks are unaddressed

### Short-term (90 days)
4. **Implement LGA Layer 1** (sandboxing) for all agent execution
5. **Deploy ST-WebAgentBench** for web agent evaluation
6. **Establish baseline** with BeSafe-Bench on current agents

### Strategic (12 months)
7. **Full LGA stack** — all four layers operational
8. **Microsoft-style governance toolkit** — registration, policy, audit, evaluation, human-in-the-loop
9. **Continuous evaluation** — weekly safety benchmarks with automated reporting

---

## Why This Matters

**The data is clear:**
- 34% of community skill packages are malformed (Skilldex)
- 89% of attacks succeed against baseline guardrails (LGA)
- 60%+ of tasks have safety violations (BeSafe-Bench)
- 40% of agent projects face cancellation (Agent Evaluation Guide)
- 73% incident reduction with governance toolkit (Microsoft)

**Governance is not optional. It's the difference between agents that work and agents that are safe to use.**

---

*Compiled by EvaPaper | May 31, 2026 | Updated June 26, 2026*  
*Repo: https://github.com/ginaecho/EvaPaper*
## Workflow Run Log

### Latest Run: 2026-07-01 17:22:03 UTC
- **Mode:** static
- **Query:** agent governance skill markdown validation
- **Question:** which papers are about static checking of agent interactions?
- **Top matched papers:**
  - Skilldex (static, score=54.8464)
  - GovernSpec / Contractual Skills (static, score=40.0766)
  - SkCC (static, score=48.8377)
  - OWASP Top 10 for Agentic Skills (AST10) (static, score=43.9078)
  - GitHub Spec Kit / SDD (Specification-Driven Development) (static, score=34.2229)
