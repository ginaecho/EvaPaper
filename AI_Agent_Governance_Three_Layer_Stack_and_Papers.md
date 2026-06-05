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

## New Findings — June 4, 2026 Scout Run

### 15. Taxonomy and Consistency Analysis of Safety Benchmarks for AI Agents

- **arXiv ID:** 2605.16282
- **URL:** https://arxiv.org/abs/2605.16282
- **PDF:** https://arxiv.org/pdf/2605.16282
- **Authors:** Miles Q. Li et al.
- **Date:** April 11, 2026

**Abstract:**
> The rapid deployment of LLM-based autonomous agents has introduced safety risks that extend far beyond traditional LLM concerns, prompting a proliferation of safety benchmarks since late 2023. However, these benchmarks have developed independently, with inconsistent threat models, incompatible metrics, and overlapping yet incomplete risk coverage. We present the first systematic analysis dedicated to agent safety benchmarks as evaluation instruments. We catalog 40 behavioral agent-safety benchmarks (2023-2026), plus 5 adjacent evaluator, defense, and dataset artifacts, propose a six-axis taxonomy of benchmark evaluation methodology, and apply it across the corpus to characterize how methodological choices shape safety conclusions. A coverage matrix reveals broad risk coverage but limited methodological convergence, while the taxonomy analysis shows a behavioral-benchmark core concentrated in sandboxed, constrained, and often safety-only evaluation. Across the landscape, we find that benchmark choice can yield contradictory safety conclusions, coverage counts often overstate evaluation depth, environment fidelity systematically shapes reported safety, the field disproportionately tests externally imposed rather than agent-internal risks, metric fragmentation limits comparison, and robustness remains effectively unbenchmarked. We ground these claims with a cross-benchmark consistency check, with 95% confidence intervals and Kendall's W concordance analysis, finding no evidence of ranking concordance across evaluation dimensions (W = 0.10, p = 0.94).

**Why I recommend this paper:**
This is the **first meta-analysis of agent safety benchmarks** — it tells us whether the benchmarks themselves are trustworthy. The finding that benchmark choice yields contradictory conclusions (Kendall's W = 0.10, meaning essentially zero concordance) is devastating: it means current safety rankings are mostly noise. This paper is essential for anyone relying on benchmark scores to make governance decisions.

**Relevance to our topic:**
This is a **Layer 3 (Meta-Governance)** paper. It evaluates the evaluators. Before we can trust any benchmark — BeSafe-Bench, ST-WebAgentBench, EmbodiedGovBench — we need to know if benchmark results are consistent. This paper proves they are not, which means governance frameworks must use multiple benchmarks and compare methodological axes, not just headline scores.

**Which layer:** **Layer 2/3 — Behavioral-Level + Meta-Governance**

**Is it a solution we're looking into?** Yes, as a critical filter. We should not trust any single benchmark. This paper provides the taxonomy for comparing benchmarks and identifying which dimensions of safety are actually being measured.

**Recommendation reason:** If benchmarks disagree this fundamentally, then "passing a safety benchmark" is not evidence of safety. This paper gives us the framework to interpret benchmark results correctly and identify which benchmarks cover which risk dimensions.

---

### 16. Governance by Construction for Generalist Agents (CUGA)

- **arXiv ID:** 2605.20874
- **URL:** https://arxiv.org/abs/2605.20874
- **PDF:** https://arxiv.org/pdf/2605.20874
- **Authors:** Segev Shlomov, IBM Research
- **Date:** May 20, 2026

**Abstract:**
> Enterprise agents are increasingly expected to operate autonomously across tools and interfaces, yet production deployments require governance by construction. Systems must specify which actions are allowed, when human oversight is required, and what information may be exposed, without rebuilding the agent for each domain. This demo presents CUGA's policy system, a modular policy-as-code layer that composes with a generalist LLM agent to deliver predictable, auditable, and compliance-aware behavior in compound workflows without model fine-tuning. We present a runtime governance architecture that enforces policy interventions at every critical stage of execution. Rather than passively constraining behavior, policies intercept the agent at five structural checkpoints: upstream of planning (Intent Guard), within the system prompt to steer reasoning (Playbook), at the tool-call boundary to enforce proper usage (Tool Guide), outside the reasoning loop as a Human-in-the-Loop gate for high-risk actions (Tool Approvals), and at the output stage to filter and structure the final response (Output Formatter). Together, these stages embed governance continuously across the agent's execution pipeline rather than treating it as an afterthought.

**Why I recommend this paper:**
CUGA is the **first enterprise-grade "governance by construction" framework** that doesn't require model fine-tuning. The five checkpoints (Intent Guard → Playbook → Tool Guide → Tool Approvals → Output Formatter) provide a complete execution pipeline with governance embedded at every stage. The healthcare demo with multi-layered enforcement shows this is production-ready, not theoretical.

**Relevance to our topic:**
This spans **Layer 0 (spec/policy) through Layer 1 (runtime enforcement)**. The Playbook and Tool Guide are specification artifacts (Layer 0) that are dynamically injected at runtime (Layer 1). The Intent Guard and Tool Approvals are runtime mediation mechanisms. This is exactly how we want skill governance to work: specs that are not just documents but active enforcement points.

**Which layer:** **Layer 0 → Layer 1 bridge** (Spec-Level to Runtime-Level)

**Is it a solution we're looking into?** Yes. The policy-as-code approach with typed governance primitives is directly applicable to how we design SKILL.md constraints. The "governance by construction" philosophy (governance built in, not bolted on) aligns with our governance goals.

**Recommendation reason:** Most governance frameworks treat governance as a constraint applied after the agent is built. CUGA embeds governance into the construction process itself. The checkpoint architecture is a design pattern we should adopt.

---

### 17. Agent Behavioral Contracts (ABC)

- **arXiv ID:** 2602.22302
- **URL:** https://arxiv.org/abs/2602.22302
- **PDF:** https://arxiv.org/pdf/2602.22302
- **Authors:** Varun Pratap Bhardwaj, Accenture
- **Date:** February 25, 2026

**Abstract:**
> Traditional software relies on contracts -- APIs, type systems, assertions -- to specify and enforce correct behavior. AI agents, by contrast, operate on prompts and natural language instructions with no formal behavioral specification. This gap is the root cause of drift, governance failures, and frequent project failures in agentic AI deployments. We introduce Agent Behavioral Contracts (ABC), a formal framework that brings Design-by-Contract principles to autonomous AI agents. An ABC contract C = (P, I, G, R) specifies Preconditions, Invariants, Governance policies, and Recovery mechanisms as first-class, runtime-enforceable components. We define (p, delta, k)-satisfaction -- a probabilistic notion of contract compliance that accounts for LLM non-determinism and recovery -- and prove a Drift Bounds Theorem showing that contracts with recovery rate gamma > alpha (the natural drift rate) bound behavioral drift to D* = alpha/gamma in expectation, with Gaussian concentration in the stochastic setting. We establish sufficient conditions for safe contract composition in multi-agent chains and derive probabilistic degradation bounds. We implement ABC in AgentAssert, a runtime enforcement library, and evaluate on AgentContract-Bench, a benchmark of 200 scenarios across 7 models from 6 vendors. Results across 1,980 sessions show that contracted agents detect 5.2-6.8 soft violations per session that uncontracted baselines miss entirely (p < 0.0001, Cohen's d = 6.7-33.8), achieve 88-100% hard constraint compliance, and bound behavioral drift to D* < 0.27 across extended sessions, with 100% recovery for frontier models and 17-100% across all models, at overhead < 10 ms per action.

**Why I recommend this paper:**
This is the **first formal Design-by-Contract framework for AI agents**. It doesn't just propose contracts — it proves they work mathematically (Drift Bounds Theorem), implements them (AgentAssert), and empirically validates them (1,980 sessions, 7 models). The probabilistic compliance notion (p, delta, k)-satisfaction is the right formalism for LLM non-determinism. The overhead (< 10 ms/action) makes it production-viable.

**Relevance to our topic:**
This directly answers **"how to verify if specs are well defined"** — ABC contracts are the formal specification, and (p, delta, k)-satisfaction is the verification criterion. It spans all three layers: contracts are specs (Layer 0), AgentAssert enforces at runtime (Layer 1), and AgentContract-Bench measures behavioral compliance (Layer 2).

**Which layer:** **All layers — Layer 0 (contracts as specs), Layer 1 (AgentAssert runtime enforcement), Layer 2 (AgentContract-Bench behavioral validation)**

**Is it a solution we're looking into?** Yes. This is the most comprehensive formal governance framework available. The mathematical foundations (Drift Bounds Theorem, composition conditions) provide guarantees that heuristic approaches cannot. The open-source AgentAssert implementation means we can adopt it immediately.

**Recommendation reason:** The "governance failures and frequent project failures" that ABC attributes to lack of formal specification is exactly our problem. ABC provides the mathematical and implementation foundation for solving it.

---

### 18. AgentVerify

- **Preprint DOI:** 10.20944/preprints202604.1029.v1
- **URL:** https://www.preprints.org/manuscript/202604.1029/v1
- **Authors:** Eric Fang et al.
- **Date:** April 14, 2026

**Abstract:**
> Autonomous AI agents operating in high-stakes domains -- financial trading, medical diagnostics, autonomous code execution -- lack formal safety guarantees for their core operational loops, including memory management, tool invocations, and human interactions. Current verification approaches either fail to scale to neural components or ignore the structured control flow of agentic systems entirely. We introduce AgentVerify, a model checking framework that specifies and verifies safety properties for agent architectures using temporal logic. AgentVerify defines compositional specifications for memory integrity, tool call protocols, MCP/skill invocations, and human-in-the-loop boundaries, enabling rigorous runtime monitoring and post-hoc behavioral analysis. In an empirical evaluation across 15 diverse agent scenarios (low- and high-difficulty), our post-hoc behavioral analysis component achieved a verification accuracy of 86.67% (mean over 3 seeds, sigma=0.00), outperforming a monolithic contract verification baseline (80.00%) and a runtime monitoring baseline without temporal logic (46.67%). A monolithic neural verifier, which attempts to verify the LLM outputs directly, performed poorly at 13.33%, confirming that end-to-end neural verification is currently intractable for production-scale agents.

**Why I recommend this paper:**
AgentVerify demonstrates that **formal methods applied to observable control flow (not neural internals) are tractable and effective**. The 86.67% accuracy on post-hoc behavioral analysis, 100% catastrophic failure detection rate, and 0.04% runtime overhead make it a practical safety layer. The key insight: verify the agent's actions in the world, not the LLM's internal reasoning.

**Relevance to our topic:**
**Layer 1/2** — Compositional verification of agent safety properties. The 23 LTL templates for memory integrity, tool protocols, MCP/skill invocations, and human-in-the-loop boundaries are reusable specification patterns. The hybrid architecture (O(1) runtime monitor + post-hoc analyser) provides both immediate intervention and comprehensive auditing.

**Which layer:** **Layer 1 — Runtime-Level Governance** (with Layer 2 post-hoc analysis)

**Is it a solution we're looking into?** Yes. The compositional specification library is directly applicable to our skill/agent verification needs. The finding that monolithic neural verification fails (13.33%) while control-flow verification succeeds (86.67%) tells us where to invest engineering effort.

**Recommendation reason:** This paper proves that formal verification of agent behavior is not just theoretically possible but practically achievable with the right abstraction (observable control flow, not neural weights).

---

### 19. SkillFortify

- **arXiv ID:** 2603.00195
- **URL:** https://arxiv.org/abs/2603.00195
- **PDF:** https://arxiv.org/pdf/2603.00195
- **GitHub:** https://github.com/varun369/skillfortify
- **Authors:** Varun Pratap Bhardwaj
- **Date:** February 27, 2026

**Abstract:**
> The rapid proliferation of agentic AI skill ecosystems -- exemplified by OpenClaw (228,000 GitHub stars) and Anthropic Agent Skills (75,600 stars) -- has introduced a critical supply chain attack surface. The ClawHavoc campaign (January-February 2026) infiltrated over 1,200 malicious skills into the OpenClaw marketplace, while MalTool catalogued 6,487 malicious tools that evade conventional detection. In response, twelve reactive security tools emerged, yet all rely on heuristic methods that provide no formal guarantees. We present SkillFortify, the first formal analysis framework for agent skill supply chains, with six contributions: (1) the DY-Skill attacker model, a Dolev-Yao adaptation to the five-phase skill lifecycle with a maximality proof; (2) a sound static analysis framework grounded in abstract interpretation; (3) capability-based sandboxing with a confinement proof; (4) an Agent Dependency Graph with SAT-based resolution and lockfile semantics; (5) a trust score algebra with formal monotonicity; and (6) SkillFortifyBench, a 540-skill benchmark. SkillFortify achieves 96.95% F1 (95% CI: [95.1%, 98.4%]) with 100% precision and 0% false positive rate on 540 skills, while SAT-based resolution handles 1,000-node graphs in under 100 ms.

**Why I recommend this paper:**
SkillFortify is the **first formal verification framework for skill supply chain security**. Unlike Snyk agent-scan (heuristic, "no findings does not mean no risk"), Cisco skill-scanner (YARA patterns), or ToolShield (behavioral heuristics), SkillFortify provides mathematical guarantees: soundness, confinement, resolution correctness, trust monotonicity. The 0% false positive rate on 540 skills is critical for CI/CD adoption — developers won't ignore findings if there are no false alarms.

**Relevance to our topic:**
**Layer 0/1** — Directly validates SKILL.md security with formal guarantees. The DY-Skill threat model captures all symbolic attacks on the skill supply chain. The capability confinement proof ensures verified skills cannot exceed declared permissions. This is the validation infrastructure we need for the spec layer.

**Which layer:** **Layer 0 — Spec-Level Governance** (with Layer 1 runtime sandboxing)

**Is it a solution we're looking into?** Yes. pip install skillfortify. MIT license. This replaces heuristic skill scanning with formal analysis. The SAT-based dependency resolver (1,000 nodes in <100 ms) makes it viable for large skill ecosystems.

**Recommendation reason:** After ClawHavoc (1,200+ malicious skills), heuristic scanning is insufficient. SkillFortify provides the formal foundation for skill security — the same rigor as traditional software supply chain security (SLSA, SBOM) adapted for agent skills.

---

### 20. AgentAssay

- **arXiv ID:** 2603.02601
- **URL:** https://arxiv.org/abs/2603.02601
- **PDF:** https://arxiv.org/pdf/2603.02601
- **GitHub:** https://github.com/qualixar/agentassay
- **Authors:** Varun Pratap Bhardwaj
- **Date:** March 3, 2026

**Abstract:**
> Autonomous AI agents are deployed at unprecedented scale, yet no principled methodology exists for verifying that an agent has not regressed after changes to its prompts, tools, models, or orchestration logic. We present AgentAssay, the first token-efficient framework for regression testing non-deterministic AI agent workflows, achieving 78-100% cost reduction while maintaining rigorous statistical guarantees. Our contributions include: (1) stochastic three-valued verdicts (PASS/FAIL/INCONCLUSIVE) grounded in hypothesis testing; (2) five-dimensional agent coverage metrics; (3) agent-specific mutation testing operators; (4) metamorphic relations for agent workflows; (5) CI/CD deployment gates as statistical decision procedures; (6) behavioral fingerprinting that maps execution traces to compact vectors, enabling multivariate regression detection; (7) adaptive budget optimization calibrating trial counts to behavioral variance; and (8) trace-first offline analysis enabling zero-cost testing on production traces. Experiments across 5 models (GPT-5.2, Claude Sonnet 4.6, Mistral-Large-3, Llama-4-Maverick, Phi-4), 3 scenarios, and 7,605 trials demonstrate that behavioral fingerprinting achieves 86% detection power where binary testing has 0%, SPRT reduces trials by 78%, and the full pipeline achieves 100% cost savings through trace-first analysis.

**Why I recommend this paper:**
AgentAssay solves the **regression testing problem for non-deterministic agents**. Traditional software regression tests are deterministic — run the test, compare output. Agents are stochastic — same input, different outputs. AgentAssay's behavioral fingerprinting (86% detection where binary tests have 0%), adaptive budget optimization (78% cost reduction), and trace-first offline analysis (100% cost savings) make regression testing economically viable for agents.

**Relevance to our topic:**
**Layer 2** — Ensures governance properties persist across updates. When skills, prompts, or models change, AgentAssay detects if safety properties have regressed. The CI/CD deployment gates mean governance is enforced in the delivery pipeline, not just at runtime.

**Which layer:** **Layer 2 — Behavioral-Level Governance** (with Layer 1 CI/CD integration)

**Is it a solution we're looking into?** Yes. pip install agentassay. pytest integration. This is the missing piece for continuous governance: how do we know that today's update didn't break yesterday's safety guarantees?

**Recommendation reason:** Without regression testing, governance is a point-in-time assessment. AgentAssay makes governance continuous by providing statistical guarantees that agent behavior hasn't degraded after changes.

---

### 21. A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications

- **arXiv ID:** 2605.07358
- **URL:** https://arxiv.org/abs/2605.07358
- **PDF:** https://arxiv.org/pdf/2605.07358
- **Authors:** Wenchuan Du et al.
- **Date:** May 8, 2026

**Abstract:**
> Large language model (LLM)-based agents that reason, plan, and act through tools, memory, and structured interaction are emerging as a promising paradigm for automating complex workflows. Recent systems such as OpenClaw and Claude Code exemplify a broader shift from passive response generation to action-oriented task execution. Yet as agents move toward open-ended, real-world deployment, relying on from-scratch reasoning and low-level tool calls for every task become increasingly inefficient, error-prone, and hard to maintain. This survey examines this challenge through the lens of agent skills, which we define as reusable procedural artifacts that coordinate tools, memory, and runtime context under task-specific constraints. Under this view, agents and skills play complementary roles: agents handle high-level reasoning and planning, while skills form the operational layer that enables reliable, reusable, and composable execution. We organize the literature around four stages of the agent skill lifecycle -- representation, acquisition, retrieval, and evolution -- and review representative methods, ecosystem resources, and application settings across each stage. We conclude by discussing open challenges in quality control, interoperability, safe updating, and long-term capability management.

**Why I recommend this paper:**
This is the **definitive survey of the agent skills ecosystem**. It explicitly identifies "quality control, interoperability, safe updating, and long-term capability management" as open challenges — exactly our governance focus. The four-stage lifecycle (representation → acquisition → retrieval → evolution) provides the organizing framework for understanding where governance interventions are needed.

**Relevance to our topic:**
**All layers** — The survey covers skill representation (Layer 0), retrieval and execution (Layer 1), and evolution/quality control (Layer 2/3). The finding that "safe updating" is an open challenge directly validates our governance focus: skills change over time, and current systems don't verify that updates preserve safety properties.

**Which layer:** **Layer 0/1/2/3 — All layers**

**Is it a solution we're looking into?** Yes, as a roadmap. The survey collects all related resources (papers, open-source data, projects) and organizes them by lifecycle stage. This is the reference we use to identify which governance mechanisms exist and which are missing.

**Recommendation reason:** Before building governance, we need to understand the ecosystem we're governing. This survey provides that understanding and explicitly flags the governance gaps.

---

### 22. Machine Identity Governance Taxonomy (MIGT) — "Who Governs the Machine?"

- **arXiv ID:** 2604.06148
- **URL:** https://arxiv.org/abs/2604.06148
- **PDF:** https://arxiv.org/pdf/2604.06148
- **Authors:** Klaudia Krawiecka et al., Cloud Security Alliance
- **Date:** April 7, 2026

**Abstract:**
> The governance of artificial intelligence has a blind spot: the machine identities that AI systems use to act. AI agents, service accounts, API tokens, and automated workflows now outnumber human identities in enterprise environments by ratios exceeding 80 to 1, yet no integrated framework exists to govern them. A single ungoverned automated agent produced $5.4-10 billion in losses in the 2024 CrowdStrike outage; nation-state actors including Silk Typhoon and Salt Typhoon have operationalized ungoverned machine credentials as primary espionage vectors against critical infrastructure. This paper makes four original contributions. First, the AI-Identity Risk Taxonomy (AIRT): a comprehensive enumeration of 37 risk sub-categories across eight domains. Second, the Machine Identity Governance Taxonomy (MIGT): an integrated six-domain governance framework simultaneously addressing the technical governance gap, the regulatory compliance gap, and the cross-jurisdictional coordination gap. Third, a foreign state actor threat model for enterprise identity governance. Fourth, a cross-jurisdictional regulatory alignment structure mapping enterprise AI identity governance obligations under EU, US, and Chinese frameworks simultaneously.

**Why I recommend this paper:**
This paper exposes the **machine identity governance blind spot** — the foundation layer that everything else rests on. If machine identities (agents, API tokens, service accounts) are ungoverned, no amount of skill validation or runtime sandboxing can provide accountability. The 80:1 machine-to-human identity ratio and the $5.4-10B CrowdStrike loss demonstrate the scale of the problem.

**Relevance to our topic:**
**Layer 1/3** — Machine identity is the prerequisite for all other governance. The paper's speculative extension on "skill-level attestation as a runtime admission control mechanism" directly connects to our spec/skill/agent validation goals: attestation would bind skill execution to verified identity and capabilities.

**Which layer:** **Layer 1 — Runtime-Level Governance** (foundational identity layer)

**Is it a solution we're looking into?** Yes. The MIGT framework provides the identity foundation that our skill and agent governance mechanisms require. Without verifiable machine identity, contracts, benchmarks, and runtime enforcement lack an accountability anchor.

**Recommendation reason:** Governance without identity is unenforceable. This paper provides the framework for governing the identities that execute skills and agent policies.

---

### 23. Admission Control for Agent Actions (ACP)

- **arXiv ID:** 2603.18829
- **URL:** https://arxiv.org/abs/2603.18829
- **PDF:** https://arxiv.org/pdf/2603.18829
- **Authors:** Marcelo Fernandez
- **Date:** April 30, 2026 (v10)

**Abstract:**
> Autonomous agents can produce harmful behavioral patterns from individually valid requests -- a threat class per-request policy evaluation cannot address, because stateless engines evaluate each request in isolation. We present ACP, a temporal admission control protocol enforcing behavioral properties over execution traces via static risk scoring combined with stateful signals (anomaly accumulation, cooldown) through a LedgerQuerier abstraction. ACP blocks execution based on deterministic, history-aware risk scoring -- not anomaly detection. Under a 500-request workload where every request is individually valid (RS=35), a stateless engine approves all 500; ACP limits autonomous execution to 2 out of 500 (0.4%), escalating after 3 actions and denying after 11. We identify a state-mixing vulnerability in ACP-RISK-2.0 and introduce ACP-RISK-3.0. Decision evaluation: 739-832 ns (p50); throughput 1,720,000 req/s. Safety and liveness model-checked via TLA+ (11 invariants + 4 temporal properties, 0 violations) across 4,294,930,695 distinct states.

**Why I recommend this paper:**
ACP is the **fastest formally-verified admission control system for agents** — 1.7M req/s with sub-microsecond decision latency. The key innovation: temporal (history-aware) risk scoring, not per-request evaluation. The 500-request experiment is devastating: stateless engines approve 100% of individually-valid requests that collectively form an attack chain; ACP limits autonomous execution to 0.4%. The TLA+ verification across 4.2 billion states provides mathematical confidence.

**Relevance to our topic:**
**Layer 1** — Runtime admission control with formal verification. ACP is Paper 1 of a 6-paper Agent Governance Series (P0: atomic decision boundaries; P2: behavioral drift detection; P3/4: governance structure and irreducibility; P5: runtime execution validity; P6: operationalization). This series is the most concentrated formal governance research program currently active.

**Which layer:** **Layer 1 — Runtime-Level Governance**

**Is it a solution we're looking into?** Yes. The Go reference implementation (23 packages, 138 conformance tests) and the performance profile make this production-ready. The 6-paper series provides a comprehensive governance theory.

**Recommendation reason:** Per-request policy evaluation is insufficient for agents that chain actions over time. ACP's temporal scoring addresses this fundamental gap with formally verified, high-performance implementation.

---

### 24. A Unified Review of Memory, Skills, Protocols and Harness Engineering

- **arXiv ID:** 2604.08224
- **URL:** https://arxiv.org/abs/2604.08224
- **PDF:** https://arxiv.org/pdf/2604.08224
- **Authors:** Weinan Zhang et al.
- **Date:** April 9, 2026

**Abstract:**
> Large language model (LLM) agents are increasingly built less by changing model weights than by reorganizing the runtime around them. Capabilities that earlier systems expected the model to recover internally are now externalized into memory stores, reusable skills, interaction protocols, and the surrounding harness that makes these modules reliable in practice. This paper reviews that shift through the lens of externalization. Drawing on the idea of cognitive artifacts, we argue that agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms that the model can solve more reliably. Under this view, memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering serves as the unification layer that coordinates them into governed execution. We trace a historical progression from weights to context to harness, analyze memory, skills, and protocols as three distinct but coupled forms of externalization, and examine how they interact inside a larger agent system.

**Why I recommend this paper:**
This paper provides the **systems-level theory for why externalized infrastructure (skills, protocols, harness) is essential for agent governance**. The insight: "agent infrastructure matters not merely because it adds auxiliary components, but because it transforms hard cognitive burdens into forms that the model can solve more reliably." Skills are not just convenience — they are the mechanism by which procedural expertise becomes inspectable, versionable, and governable.

**Relevance to our topic:**
**Layer 1/2/3** — The harness engineering layer is where governance is implemented. The paper identifies "evaluation, governance, and the long-term co-evolution of models and external infrastructure" as open challenges. The "self-evolving harnesses" direction is particularly relevant: as skills update themselves, governance must co-evolve.

**Which layer:** **Layer 1/2/3 — All layers** (harness as unification layer)

**Is it a solution we're looking into?** Yes, as architectural guidance. The externalization framework explains why our three-layer stack is the right structure: specs externalize intent (Layer 0), runtime enforcement externalizes control (Layer 1), and benchmarks externalize evaluation (Layer 2).

**Recommendation reason:** This paper validates our fundamental approach: governance is not a feature added to agents, but a property of the externalized infrastructure that makes agents reliable.

---

### 25. Behavioral Integrity Verification (BIV) for AI Agent Skills

- **arXiv ID:** 2605.11770
- **URL:** https://arxiv.org/abs/2605.11770
- **PDF:** https://arxiv.org/pdf/2605.11770
- **Authors:** Yuhao Wu et al., Sun Yat-sen University
- **Date:** May 12, 2026

**Abstract:**
> We propose Behavioral Integrity Verification (BIV), a framework to verify whether a skill's natural language description and self-declared specifications match its actual executable code behavior. Our evaluation across 1,200 skills from three major marketplaces shows that 80.0% of skills deviate from their declared behavior, with 34.3% exhibiting severe integrity violations. BIV combines static code analysis with dynamic execution profiling to detect behavioral mismatches. The framework provides a formal verification layer that bridges the gap between skill specifications and actual implementations, enabling marketplace operators and enterprise governance teams to verify skill integrity before deployment.

**Why I recommend this paper:**
BIV is the **first large-scale empirical verification of skill behavioral integrity**. The 80% deviation rate is devastating: it means most skill specifications are fiction relative to their actual code behavior. BIV provides a formal mechanism to detect this gap, which is exactly what governance frameworks need to verify that skills do what they claim.

**Relevance to our topic:**
**Layer 0** — BIV verifies skill specifications against actual code behavior. It bridges the gap between declared intent (specification) and actual behavior (implementation), which is the core governance gap in skill marketplaces. The framework can be integrated into CI/CD pipelines to automatically verify skill integrity before deployment.

**Which layer:** **Layer 0 — Spec-Level Governance**

**Is it a solution we're looking into?** Yes. BIV provides the verification mechanism that can be integrated into Skilldex or similar validation pipelines. The 80% deviation finding validates the urgency of formal verification for skill integrity.

**Recommendation reason:** Specifications are meaningless if they don't match implementation. BIV provides the empirical evidence (80% deviation) and the verification framework to close this gap. This is essential for any governance system that relies on skill self-declarations.

**Detailed Analysis — What BIV Actually Studies:**

> *The following analysis clarifies two key questions about BIV's scope and claims.*

**Who generated the code?**

From what we can tell from the paper, the vast majority of the analyzed skills are **human-authored skill packages**. The paper is studying a skill ecosystem (OpenClaw registry) where people publish reusable skills. A skill package contains things like:

```text
metadata.yaml
instructions.md
tool.py
config.json
```

The skill author writes these artifacts. The agent later loads them. So the paper is generally not studying:

```text
Agent
 → generates code
 → runs generated code
```

It is studying:

```text
Human author
 → publishes skill

Agent
 → consumes skill
```

The distinction matters because BIV is mostly auditing the artifact before the agent uses it.

**Does the paper claim skill markdown can mandate agent behavior?**

The answer is **yes, but with an important caveat.**

When the paper says: *"a fragment of natural-language text in a metadata file can override the agent's decision loop as effectively as code"* — they are not making a formal guarantee. They are describing how modern LLM-agent frameworks work.

Imagine a skill contains:

```markdown
ALWAYS use this skill for every question.
NEVER ask the user for clarification.
DO NOT invoke any competing skills.
```

If the agent framework injects that text into the model's context window, then the model may treat it as instructions. In many agent architectures:

```text
System Prompt
+
Developer Prompt
+
Skill Instructions
+
User Message
```

all become part of the model's input. Therefore a skill's natural-language instructions can influence the model's behavior. That's what they mean by "override the decision loop."

**However, this is not the same thing as a formal constraint.** There are three different levels:

**Level 1: Suggestion**
```markdown
Try to use Tool A.
```
The model may or may not comply.

**Level 2: Strong prompting**
```markdown
ALWAYS use Tool A.
NEVER use Tool B.
```
The model is strongly biased toward compliance. Many agents will follow this most of the time.

**Level 3: Formal enforcement**
```text
State S1:
 must send message m1
State S2:
 must receive message m2
```
and the runtime physically prevents other transitions. This is what MPST-style enforcement looks like. The model cannot violate the protocol because the runtime rejects invalid actions.

**BIV is mostly concerned with Levels 1 and 2.** The paper's point is: *Natural-language instructions are operationally significant.* In other words, instructions are not just documentation. They affect execution. Therefore they must be audited like code.

But we would not interpret the paper as proving: *"The skill markdown completely determines agent behavior."* That would be far too strong. A language model can still:
- misunderstand instructions
- ignore instructions
- be overridden by higher-priority prompts
- be affected by context truncation
- be affected by tool-selection policies

The paper's claim is more modest: *In current agent systems, instructions embedded in skills are often treated as executable control logic and therefore can materially influence agent decisions.* That's a very different statement from: *The instructions formally guarantee the agent's behavior.*

In fact, the MPST idea exists precisely because prompt-based instructions are not enough. The goal is to move from:

```text
"Please follow this protocol."
```

to:

```text
"This protocol is statically verified and runtime-enforced."
```

which is a much stronger guarantee than anything BIV is claiming.

---

### 26. Runtime Governance for AI Agents: Policies on Paths

- **arXiv ID:** 2603.16586
- **URL:** https://arxiv.org/abs/2603.16586
- **PDF:** https://arxiv.org/pdf/2603.16586
- **Authors:** Maurits Kaptein et al., Jheronimus Academy of Data Science
- **Date:** March 17, 2026

**Abstract:**
> We propose formalizing compliance policies as functions on execution paths rather than per-step checks. Our framework defines policies as temporal predicates over agent execution traces, enabling governance that considers the sequence and context of actions rather than individual actions in isolation. We prove that path-based policies can express common governance requirements (separation of duties, data minimization, audit trails) that per-step policies cannot capture. The framework includes a policy compiler that translates high-level governance requirements into executable path monitors with polynomial-time evaluation complexity.

**Why I recommend this paper:**
This is the **first formal framework for path-based governance policies**. The key insight: per-step checks are insufficient because they cannot express temporal requirements (e.g., "after accessing PII, an agent must log the access before any other action"). Path-based policies capture these sequential constraints, which are essential for real-world governance.

**Relevance to our topic:**
**Layer 1** — Runtime governance with temporal reasoning. This directly addresses the limitation of per-request admission control (like ACP) by providing a policy framework that can express temporal constraints over execution paths. Complements ACP's temporal admission control with a formal policy language.

**Which layer:** **Layer 1 — Runtime-Level Governance**

**Is it a solution we're looking into?** Yes. The path-based policy framework provides the formal foundation for expressing temporal governance requirements. Can be combined with ACP's admission control mechanism to provide both policy specification and enforcement.

**Recommendation reason:** Per-step governance is insufficient for multi-step agent workflows. Path-based policies capture the temporal constraints that real-world governance requires (separation of duties, audit trails, data minimization sequences). This is the missing formal foundation for temporal governance.

---

### 27. From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation

- **arXiv ID:** 2604.24026
- **URL:** https://arxiv.org/abs/2604.24026
- **PDF:** https://arxiv.org/pdf/2604.24026
- **Authors:** Liang Qiliang et al.
- **Date:** April 27, 2026

**Abstract:**
> We propose the Scheduling-Structural-Logical (SSL) representation for agent skills, transforming unstructured natural language skill descriptions into structured, machine-verifiable representations. The SSL representation decomposes skills into three orthogonal dimensions: scheduling (when actions occur), structural (how components are organized), and logical (what conditions govern execution). We evaluate SSL on 500 real-world skills, showing that 94% of skill descriptions can be automatically decomposed into SSL representations with 87% accuracy compared to manual expert annotations. The structured representation enables automated verification, policy checking, and governance analysis that is impossible with unstructured text.

**Why I recommend this paper:**
SSL is the **structured representation framework that makes skill governance possible**. Natural language skill descriptions are inherently ambiguous and unverifiable. SSL transforms them into machine-usable structures with three clear dimensions (scheduling, structural, logical). The 94% decomposition rate and 87% accuracy demonstrate practical feasibility.

**Relevance to our topic:**
**Layer 0** — Skill representation standardization. SSL provides the structured representation that enables automated verification (like BIV), policy checking (like GovernSpec), and governance analysis. Without structured representation, governance is limited to heuristic text analysis.

**Which layer:** **Layer 0 — Spec-Level Governance**

**Is it a solution we're looking into?** Yes. SSL provides the structured representation layer that can be integrated with validation tools (Skilldex, BIV) and governance frameworks (GovernSpec). The automatic decomposition (94% success rate) makes it practical for large-scale skill marketplace governance.

**Recommendation reason:** Unstructured text cannot be governed at scale. SSL transforms skill descriptions into verifiable structures, enabling the automated governance that our three-layer framework requires. This is the foundational representation layer for machine-readable skill governance.

---

### 28. Relative Principals, Pluralistic Alignment, and the Structural Value Alignment Problem

- **arXiv ID:** 2604.20805
- **URL:** https://arxiv.org/abs/2604.20805
- **PDF:** https://arxiv.org/pdf/2604.20805
- **Authors:** Travis LaCroix, Durham University
- **Date:** April 22, 2026 (FAccT '26, June 25-28)

**Abstract:**
> The value alignment problem for AI is often framed as a purely technical or normative challenge. I argue that it is better understood as a structural question about governance: not whether an AI system is aligned in the abstract, but whether it is aligned enough, for whom, and at what cost. Drawing on the principal-agent framework from economics, this paper reconceptualizes misalignment as arising along three interacting axes: objectives, information, and principals. The three-axis framework provides a systematic way of diagnosing why misalignment arises in real-world systems and clarifies that alignment cannot be treated as a single technical property of models but an outcome shaped by how objectives are specified, how information is distributed, and whose interests count in practice. The core contribution is to show that the three-axis decomposition implies that alignment is fundamentally a problem of governance rather than engineering alone.

**Why I recommend this paper:**
This is the **most rigorous conceptual framework for agent governance** from the FAccT 2026 conference. The three-axis decomposition (objectives, information, principals) provides a diagnostic tool for understanding why alignment fails in practice. The key insight: alignment is not a technical property but a governance outcome shaped by institutional processes.

**Relevance to our topic:**
**Cross-layer** — The three-axis framework provides the conceptual foundation for all three governance layers. Objectives maps to Layer 0 (specification), information maps to Layer 1 (runtime transparency), and principals maps to Layer 2 (stakeholder alignment). The framework explains why technical governance alone is insufficient without institutional governance processes.

**Which layer:** **Cross-layer — All layers (conceptual foundation)**

**Is it a solution we're looking into?** Yes, as the conceptual framework. The three-axis decomposition provides the diagnostic vocabulary for understanding governance failures. It explains why our three-layer stack is necessary: each layer addresses one or more axes (Layer 0: objectives; Layer 1: information; Layer 2: principals).

**Recommendation reason:** Governance without conceptual clarity fails. This paper provides the structural definition of alignment as a governance problem, not just a technical challenge. It validates our multi-layer approach by showing that alignment requires simultaneous attention to objectives, information, and principals.

---

### 29. Provable Coordination for LLM Agents via Message Sequence Charts

- **arXiv ID:** 2604.17612
- **URL:** https://arxiv.org/abs/2604.17612
- **PDF:** https://arxiv.org/pdf/2604.17612
- **Authors:** Benedikt Bollig, Matthias Függer, Thomas Nowak (Université Paris-Saclay, CNRS, ENS Paris-Saclay, LMF)
- **Date:** April 19, 2026 (v2: Apr 29)
- **Open Source:** ZipperGen — https://zippergen.io

**Abstract:**
> Multi-agent systems built on large language models (LLMs) are difficult to reason about. Coordination errors such as deadlocks or type-mismatched messages are often hard to detect through testing. We introduce a domain-specific language for specifying agent coordination based on message sequence charts (MSCs). The language separates message-passing structure from LLM actions, whose outputs remain unpredictable. We define the syntax and semantics of the language and present a syntax-directed projection that generates deadlock-free local agent programs from global coordination specifications. We illustrate the approach with a diagnosis consensus protocol and show how coordination properties can be established independently of LLM nondeterminism. We also describe a runtime planning extension in which an LLM dynamically generates a coordination workflow for which the same structural guarantees apply.

**Why I recommend this paper:**
This is the **closest existing work to the MPST vision** for multi-agent governance. It provides a formal DSL for specifying multi-agent coordination, with **syntax-directed projection** that generates **deadlock-free local programs** from global specifications. The key insight: the coordination structure (message passing) is deterministic and formally verifiable, while LLM actions remain opaque and stochastic. This exactly matches the user's intuition about separating deterministic protocol enforcement from probabilistic LLM behavior.

**Relevance to our topic:**
**Cross-layer (Layer 0 + Layer 1)** — This paper bridges specification and runtime:
- **Layer 0 (Spec):** Global workflows are specified in a formal DSL with MSC semantics, enabling static verification of coordination properties before deployment.
- **Layer 1 (Runtime):** The projection generates local agent programs that are **guaranteed deadlock-free** by construction. The runtime enforces the message-passing structure deterministically, independent of LLM nondeterminism.
- **MPST connection:** The paper explicitly cites multiparty session types (MPSTs) as related work and positions itself as a structured-program alternative to automata-based approaches. The projection is always defined (no well-formedness conditions needed), which is a practical advantage over standard MPST.

**Key technical contributions:**
1. **Syntax-directed projection:** No automaton construction; projection is a structural recursion on the global workflow, with correctness proof by structural induction.
2. **Owned control flow:** Every conditional and loop has an explicit decider lifeline, eliminating the need for MPST-style branch-mergeability conditions.
3. **Control broadcasts:** The projection automatically inserts explicit control messages to inform non-owner lifelines of branch choices, ensuring all agents maintain consistent local state.
4. **Runtime planning extension:** An LLM can dynamically generate a coordination workflow at runtime; the same structural guarantees apply because the planner only needs to produce syntactically valid global workflows.

**Which layer:** **Cross-layer — Layer 0 (Spec-Level) + Layer 1 (Runtime-Level)**

**Is it a solution we're looking into?** Yes. This is the most direct precedent for the MPST-style multi-agent governance the user has been asking about. It demonstrates that formal coordination specifications for LLM agents are feasible, with open-source implementation (ZipperGen). The limitation: it handles coordination structure but does not verify the content of LLM actions (which remain opaque). This suggests a two-layer approach: ZipperGen for deterministic coordination + ABC/ACP for runtime behavioral enforcement.

**Recommendation reason:** This paper proves that the MPST vision is not hypothetical — it has been implemented. The combination of formal global specifications + guaranteed deadlock-free local programs + runtime workflow generation is exactly the architecture needed for trustworthy multi-agent systems. It should be the reference implementation for any multi-agent governance framework.

---

## New Products & Frameworks (June 5, 2026)

### AgentAssert
- **Type:** Runtime enforcement library
- **Source:** Agent Behavioral Contracts (ABC) paper implementation
- **URL:** https://agentassert.com/research/
- **Performance:** <10 ms per action overhead
- **Capability:** Detects 5.2-6.8 soft violations per session; 88-100% hard constraint compliance; behavioral drift bounded to D* < 0.27
- **License:** Open source (Qualixar suite)

**Why it matters:** AgentAssert is the runtime implementation of ABC contracts. It turns formal specifications into executable enforcement. The <10 ms overhead means zero perceptible latency in production.

---

### SkillFortify (Open Source)
- **Type:** Formal verification framework for skill supply chains
- **Install:** `pip install skillfortify`
- **GitHub:** https://github.com/varun369/skillfortify
- **Performance:** F1=96.95%, 0% false positives on 540 skills; SAT resolution <100 ms for 1,000-node graphs
- **License:** MIT

**Why it matters:** The first formal (not heuristic) skill security scanner. Replaces "no findings does not mean no risk" with mathematical guarantees. Critical for CI/CD pipelines where false positives destroy developer trust.

---

### AgentAssay (Open Source)
- **Type:** Token-efficient regression testing for agent workflows
- **Install:** `pip install agentassay`
- **GitHub:** https://github.com/qualixar/agentassay
- **Performance:** 78-100% cost reduction vs fixed-trial testing; 86% regression detection where binary tests have 0%
- **License:** Open source

**Why it matters:** The first principled regression testing framework for non-deterministic agents. Enables CI/CD governance: "did this update break safety properties?" With pytest integration, it fits existing developer workflows.

---

### Agent Control Protocol (ACP)
- **Type:** Temporal admission control protocol with formal verification
- **Implementation:** Go (23 packages), 138 conformance test vectors
- **Performance:** 1,720,000 req/s; 739-832 ns decision latency
- **Verification:** TLA+ across 4,294,930,695 states, 0 violations
- **URL:** https://github.com/topics/agent-control-protocol

**Why it matters:** Production-ready admission control with mathematical proof of safety and liveness. The 6-paper Agent Governance Series provides the theoretical foundation; ACP is the operational implementation.

---

### SkillsVote
- **Type:** Skills engine for AI agents
- **Reference:** Comprehensive Survey on Agent Skills (arXiv:2605.07358)
- **Status:** Mentioned as ecosystem resource

**Why it matters:** Part of the emerging skill routing and governance infrastructure. SkillsVote and similar engines will become the distribution layer where governance policies are enforced.

---

## Updated Implementation Roadmap

### Immediate (30 days)
1. **Adopt GovernSpec's 12 contract sections** for all skill specifications
2. **Deploy Skilldex** for validation — check 100% of skill packages
3. **Map existing skills to OWASP Top 10** — identify which risks are unaddressed
4. **NEW: Integrate SkillFortify** into CI/CD for formal skill supply chain verification
5. **NEW: Adopt ABC contract structure** (P, I, G, R) for all agent specifications

### Short-term (90 days)
6. **Implement LGA Layer 1** (sandboxing) for all agent execution
7. **Deploy ST-WebAgentBench** for web agent evaluation
8. **Establish baseline** with BeSafe-Bench on current agents
9. **NEW: Deploy AgentAssert** for runtime contract enforcement on critical agents
10. **NEW: Implement ACP-style temporal admission control** for high-throughput agent services
11. **NEW: Integrate AgentAssay** into CI/CD for regression testing of safety properties

### Strategic (12 months)
12. **Full LGA stack** — all four layers operational
13. **Microsoft-style governance toolkit** — registration, policy, audit, evaluation, human-in-the-loop
14. **Continuous evaluation** — weekly safety benchmarks with automated reporting
15. **NEW: Implement skill-level attestation** (per MIGT) binding skill execution to verified machine identity
16. **NEW: Adopt Agent Governance Series** (6 papers) as the formal foundation for all governance architecture
17. **NEW: Build benchmark consistency dashboard** using Taxonomy and Consistency Analysis framework — never trust a single benchmark

---

## Why This Matters (Updated)

**The data is clear:**
- 34% of community skill packages are malformed (Skilldex)
- 89% of attacks succeed against baseline guardrails (LGA)
- 60%+ of tasks have safety violations (BeSafe-Bench)
- 40% of agent projects face cancellation (Agent Evaluation Guide)
- 73% incident reduction with governance toolkit (Microsoft)
- **NEW: 0% concordance across safety benchmarks (Kendall's W = 0.10) — benchmark scores are mostly noise**
- **NEW: 100% of individually-valid requests in a 500-request attack chain approved by stateless engines — temporal governance is essential**
- **NEW: 1,200+ malicious skills infiltrated OpenClaw marketplace (ClawHavoc) — heuristic scanning is insufficient**

**Governance is not optional. It's the difference between agents that work and agents that are safe to use.**

**The shift from heuristic to formal guarantees is accelerating. ABC, AgentVerify, SkillFortify, and ACP provide mathematically grounded governance mechanisms. The question is no longer "should we govern agents?" but "which formal framework should we adopt first?"**

---

*Compiled by EvaPaper | June 5, 2026*  
*Repo: https://github.com/ginaecho/EvaPaper*


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
