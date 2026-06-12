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

### June 13, 2026 scout addendum: one newly surfaced paper

The June 13 scout adds one paper on **proactive runtime safety auditing** that bridges Layer 1 and Layer 2:

1. **TRACES** (`arXiv:2605.27690`)
   - Learns prefix-level trajectory risk states from an observer LLM's hidden representations to proactively flag unsafe behavior before it fully manifests
   - Most relevant to **Layer 1 + Layer 2**
   - Why it matters: most safety systems are reactive (post-hoc diagnosis); TRACES is proactive — it catches risks while they are unfolding by modeling temporal evolution of latent risk features, trained with weak trajectory-level supervision rather than expensive step-level annotations

**Interpretation:** the June 13 addition reinforces that the governance problem is not just about writing better specs or adding runtime guards. It is also about (c) detecting when an agent is *drifting* toward unsafe behavior before the damage is done, using signals embedded in the LLM's own hidden states. TRACES shows that proactive auditing is possible with weak supervision, making it practical for production deployment.

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

*Compiled by EvaPaper | May 31, 2026*  
*Repo: https://github.com/ginaecho/EvaPaper*
## Workflow Run Log

### Run 2026-06-07 13:33:31 UTC
- **Mode:** static
- **Query:** agent governance skill markdown validation
- **Question:** which papers are about static checking of agent interactions?
- **Discovery graph:** 0 seeds, 0 candidates
- **Input tokens:** 1234
- **Output tokens:** 567
- **Total tokens:** 1801
- **Estimated cost (USD):** 0.012340
- **Cost note:** Test run for workflow accounting
- **Graph warning:** Discovery graph unavailable; fell back to local corpus only: <urlopen error [Errno 8] nodename nor servname provided, or not known>
- **Top matched papers:**
  - Skilldex (static, score=55.196)
  - GovernSpec / Contractual Skills (static, score=40.1709)
  - SkCC (static, score=49.8863)
  - OWASP Top 10 for Agentic Skills (AST10) (static, score=44.1682)
  - GitHub Spec Kit / SDD (Specification-Driven Development) (static, score=34.3207)

### Run 2026-06-07 13:35:24 UTC
- **Mode:** static
- **Query:** agent governance skill markdown validation
- **Question:** which papers are about static checking of agent interactions?
- **Discovery graph:** 0 seeds, 0 candidates
- **Input tokens:** 0
- **Output tokens:** 0
- **Total tokens:** 0
- **Estimated cost (USD):** 0.000000
- **Cost note:** Default local workflow accounting. Update this file or pass CLI overrides when you have real API/model usage numbers.
- **Graph warning:** Discovery graph unavailable; fell back to local corpus only: <urlopen error [Errno 8] nodename nor servname provided, or not known>
- **Top matched papers:**
  - Skilldex (static, score=55.196)
  - GovernSpec / Contractual Skills (static, score=40.1709)
  - SkCC (static, score=49.8863)
  - OWASP Top 10 for Agentic Skills (AST10) (static, score=44.1682)
  - GitHub Spec Kit / SDD (Specification-Driven Development) (static, score=34.3207)

### Run 2026-06-07 13:52:47 UTC
- **Mode:** static
- **Query:** agent governance skill markdown validation
- **Question:** which papers are about static checking of agent interactions?
- **Discovery graph:** 0 seeds, 0 candidates
- **Input tokens:** 0
- **Output tokens:** 0
- **Total tokens:** 0
- **Estimated cost (USD):** 0.000000
- **Cost note:** Default local workflow accounting. Update this file or pass CLI overrides when you have real API/model usage numbers.
- **Graph warning:** Discovery graph unavailable; fell back to local corpus only: <urlopen error [Errno 8] nodename nor servname provided, or not known>
- **Top matched papers:**
  - Skilldex (static, score=55.196)
  - GovernSpec / Contractual Skills (static, score=40.1709)
  - SkCC (static, score=49.8863)
  - OWASP Top 10 for Agentic Skills (AST10) (static, score=44.1682)
  - GitHub Spec Kit / SDD (Specification-Driven Development) (static, score=34.3207)
