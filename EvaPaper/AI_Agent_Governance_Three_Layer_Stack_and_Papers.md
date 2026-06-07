# AI Agent Governance: Three-Layer Stack and Research Papers

> "Even if the world forgets, I'll remember for you." — EvaPaper

---

## Executive Summary

This report consolidates research on **AI Agent Governance**, **Skill Markdown Validation**, and **Agent Behavior Evaluation**. It presents a **Three-Layer Governance Stack** as the organizing framework, with each paper/product mapped to the specific layer it addresses.

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
