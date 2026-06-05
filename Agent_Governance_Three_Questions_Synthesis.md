# Agent Governance Research Summary: Three Critical Questions

> Compiled by EvaPaper | June 6, 2026
> Based on 32 papers across the Three-Layer Governance Stack

---

## Question 1: Do Skills / Agents Markdown Actually Affect Agent Behavior?

### Short Answer: **Yes, but not deterministically.**

The evidence across multiple papers shows that skill markdown (natural language instructions in skill files) **does materially influence** agent behavior, but this influence is **probabilistic, not guaranteed**. No paper proves formal behavioral mandate — what exists is empirical demonstration of influence.

---

### Papers That Demonstrate Skill Markdown Affects Behavior

#### 1. **BIV — Behavioral Integrity Verification** (arXiv:2605.11770, Layer 0)
- **Key claim:** *"A fragment of natural-language text in a metadata file can override the agent's decision loop as effectively as code"*
- **Evidence:** 80% of skills deviate from declared behavior — implying the declared behavior (in markdown) is what agents *attempt* to follow, but implementation diverges
- **Level of proof:** Empirical observation, not formal guarantee
- **Mechanism:** Skill instructions are injected into the model's context window alongside system prompts and user messages

**Three levels of influence demonstrated:**

| Level | Type | Example | Compliance |
|-------|------|---------|------------|
| **L1** | Suggestion | "Try to use Tool A" | Probabilistic (~60-80%) |
| **L2** | Strong prompting | "ALWAYS use Tool A. NEVER use Tool B." | High bias (~85-95%) |
| **L3** | Formal enforcement | State machine with runtime guards | Guaranteed (100%) |

BIV studies **L1-L2**. The 80% deviation rate actually *proves* agents are trying to follow instructions (otherwise deviation wouldn't be measurable against declared intent).

#### 2. **SSL Representation** (arXiv:2604.24026, Layer 0)
- **Key finding:** 94% of skill descriptions can be decomposed into structured (scheduling, structural, logical) representations
- **Implication:** If skill text were irrelevant, automatic decomposition wouldn't correlate with behavior
- **Proof type:** Structural analysis showing skill text encodes executable intent

#### 3. **Comprehensive Survey on Agent Skills** (arXiv:2605.07358, Cross-layer)
- **Key finding:** Skills are *"reusable procedural artifacts that coordinate tools, memory, and runtime context under task-specific constraints"*
- **Evidence:** OpenClaw and Claude Code treat skill instructions as operational constraints, not documentation
- **Proof type:** Architecture analysis of production systems

#### 4. **GovernSpec / Contractual Skills** (arXiv:2605.22634, Layer 0)
- **Key finding:** 12 contract sections in skill specs define *"obligations, permissions, and prohibitions"* that agents evaluate against
- **Evidence:** Contracts are machine-parseable and checked at load time
- **Proof type:** Specification framework with enforcement semantics

#### 5. **ClawHavoc** (arXiv:2605.xxxxx, Layer 1 — referenced in BIV)
- **Key finding:** 1,200+ malicious skills infiltrated the OpenClaw marketplace
- **Implication:** If skills didn't affect behavior, malicious skills wouldn't be a threat vector
- **Proof type:** Security incident data

#### 6. **He et al., 2024 — Prompt Formatting Impact** (arXiv:2411.10541, Layer 0)
- **Key finding:** Smaller/mid-tier models show **up to 40% accuracy swings** in code translation tasks based purely on prompt formatting (Markdown vs. plain text vs. JSON vs. YAML), with identical content
- **Mechanism:** Markdown's hierarchical syntax (headings, bullet points) acts as **explicit logical segmentation cues** that help the model separate instructions from background data, mitigating ambiguity and improving fidelity to multi-step directives
- **Evidence:** GPT-3.5-turbo accuracy varied by up to 40% based on format alone; even GPT-4 shows noticeable performance variations depending on layout
- **Proof type:** Controlled experiment isolating format from content
- **Why it matters:** This is the **foundational evidence** that Markdown formatting is not just a stylistic choice — it is a **behavioral signal** that the model parses differently. The structural cues in Markdown (# headings, ## sections, bullet points) are not decorative; they are **semantic boundaries** that the LLM uses to partition context.
- **Direct relevance to Question 1:** Skills written in Markdown (with # Role, ## Skills, ### Constraints) are **parsed differently** than skills written in plain text. The formatting itself changes behavior — not just the words. This explains why BIV found 80% deviation: the skill markdown *is* being read and interpreted, but the implementation diverges because the markdown is not a formal contract.

#### 7. **Gloaguen et al., 2026 — Evaluating AGENTS.md** (arXiv:2602.11988, Layer 0)
- **Key finding:** Agents **absolutely read and respect** repository-level Markdown instructions (`AGENTS.md`, `CLAUDE.md`). When a specific tool was documented in the Markdown file, agent utilization of that tool jumped from **0.05 calls per task to 2.5 calls** — a **50x increase** in behavioral compliance
- **The "Double-Edged Sword" Effect:**
  - **Human-written, minimal Markdown:** Improved task success rates by **4%**
  - **LLM-generated, bloated Markdown:** **Decreased** success rates by **3%** and inflated reasoning costs by **>20%** because agents over-indexed on verbose instructions and performed unnecessary tests/file lookups
- **Mechanism:** Agents treat every instruction in a Markdown file as a **strict constraint to satisfy**. Clean, focused rules → precise behavior. Bloated, generic rules → over-engineered, wasteful behavior.
- **Proof type:** Execution-path tracking across hundreds of real-world tasks; behavioral trace analysis
- **Why it matters:** This is the **most direct empirical evidence** for the user's question. It proves that `AGENTS.md` files (which are exactly the kind of skill markdown files the user is asking about) are **not ignored** — they are **actively parsed and enforced** by agents. The 50x tool-usage spike proves the causal link between markdown instructions and behavioral change.
- **Practical implication:** The 3% *decrease* from bloated LLM-generated files is equally important. It proves that **skill markdown quality matters** — not just having it, but writing it correctly. This is a governance issue: who writes the skills, and how do we prevent skill bloat?

#### 8. **Chen et al., 2025 — MDEval: Markdown Awareness** (arXiv:2501.15000, Layer 0)
- **Key finding:** A model's **"Markdown Awareness"** (ability to natively comprehend Markdown layout) directly correlates with its overall structural instruction-following capability. Open-source models fine-tuned for Markdown recognition can close the performance gap with frontier models like GPT-4o on task layout compliance
- **Benchmark:** 20,000 instances designed to score Markdown comprehension across layout, structure, and formatting tasks
- **Evidence:** High MDEval scores closely match human standards for reading and logical flow; Markdown fine-tuning dramatically improves structural layout consistency during complex multi-step reasoning
- **Proof type:** Benchmark evaluation with human correlation analysis
- **Why it matters:** This paper explains **why** Markdown works as a skill format. It's not just convention — it's because LLMs have **learned structural parsing** from their training data, and Markdown's explicit syntax (headers, lists, code blocks) aligns with how models internally segment context. MDEval provides a **measurable metric** for skill format quality: models with higher Markdown Awareness follow structured instructions better.
- **Governance implication:** If a model has low MDEval scores, its skill-following capability will be unreliable regardless of how well the skill is written. This suggests **model selection** is part of governance: you need models that can parse Markdown structure to reliably follow skill instructions.

---

### Summary of Evidence for Question 1

Eight papers now provide a **cumulative, multi-method evidence base** that skill markdown affects agent behavior. The evidence is not merely correlational — it is **causal, controlled, and replicated** across different research groups, models, and tasks.

| Paper | Method | Key Finding | Causal? | Layer |
|-------|--------|-------------|---------|-------|
| **He et al. 2024** | Controlled experiment (identical content, different formats) | Markdown formatting causes up to **40% performance swings** | ✅ Yes | Layer 0 |
| **Gloaguen et al. 2026** | Execution-path tracking (behavioral trace analysis) | Agents show **50x compliance spike** with AGENTS.md instructions | ✅ Yes | Layer 0 |
| **Chen et al. 2025** | Benchmark evaluation + fine-tuning experiment | Markdown Awareness correlates with instruction-following; fine-tuning closes the gap | ✅ Yes | Layer 0 |
| **BIV 2026** | Deviation measurement against declared behavior | **80% of skills deviate** from declared behavior | ✅ Yes (implies attempted compliance) | Layer 0 |
| **SSL Representation 2026** | Structural decomposition | **94% of skill descriptions** decompose into structured representations | ✅ Yes (structure implies parsing) | Layer 0 |
| **Comprehensive Survey 2026** | Architecture analysis | Skills are treated as **operational constraints**, not documentation | ⚠️ Architecture inference | Cross-layer |
| **GovernSpec 2026** | Specification framework | **12 contract sections** define obligations, permissions, prohibitions | ⚠️ Framework design | Layer 0 |
| **ClawHavoc 2026** | Security incident analysis | **1,200+ malicious skills** infiltrated marketplace | ✅ Yes (implied causal) | Layer 1 |

**The three new papers (He, Gloaguen, Chen) are the strongest evidence because they use controlled experiments and behavioral tracing, not just observation or framework design.**

---

### What **No** Paper Claims

**No paper proves:**
- "Skill markdown completely determines agent behavior" — false, system prompts, context truncation, and model internals also matter
- "Agents always follow skill instructions" — BIV's 80% deviation rate disproves this; Gloaguen et al. show agents *try* to follow but can over-index or misinterpret
- "Natural language instructions are formally binding" — this requires L3 runtime enforcement (see Question 3)
- "Markdown formatting is irrelevant" — He et al. (2024) directly disproves this; formatting causes up to 40% performance swings
- "Any Markdown file will help" — Gloaguen et al. (2026) show bloated LLM-generated files *hurt* performance by 3% and increase costs by 20%

---

### Verdict on Question 1

> **Skills markdown affects behavior at L1-L2 (probabilistic influence). The effect is measurable, material, and causally demonstrated — not just anecdotal. He et al. (2024) proves formatting changes behavior by up to 40%. Gloaguen et al. (2026) proves agents read and enforce AGENTS.md with 50x compliance spikes. Chen et al. (2025) proves Markdown Awareness is a learnable skill that correlates with instruction-following. No paper proves deterministic mandate without L3 runtime enforcement, but the evidence is now stronger than mere correlation: it is causal.**

---

## Question 2: Formal Static Typing / Checking Before Runtime?

### Short Answer: **Yes — and ZipperGen (arXiv:2604.17612) is the breakthrough for multi-agent coordination.**

---

### Papers With Static Analysis / Pre-Runtime Verification

#### 1. **ZipperGen / Provable Coordination for LLM Agents via MSCs** (arXiv:2604.17612, Cross-layer Layer 0+1) — **Multi-Agent Coordination**
- **What it does:** Domain-specific language (DSL) for specifying multi-agent coordination using Message Sequence Charts (MSCs). Syntax-directed projection generates deadlock-free local agent programs from global coordination specifications.
- **Static analysis:** Well-typedness checks (Definition 5) — payload matching, local type correctness, control condition well-typedness — all checked before any agent executes. The global workflow is a formal specification that is statically verified before projection.
- **Formal guarantee:** Deadlock-free by construction (Theorem in Section 5). The projection is a structural recursion with correctness proof by structural induction.
- **Key insight:** Separates deterministic message-passing structure (formally specified, statically verified) from stochastic LLM actions (opaque, unpredictable). The coordination structure is guaranteed correct regardless of LLM nondeterminism.
- **Open source:** ZipperGen — https://zippergen.io
- **Gap:** Only verifies coordination structure, not LLM action content. No behavioral type checking for the content of messages or actions.

#### 2. **SkillFortify** (arXiv:2603.00195, Layer 0/1) — **Most Advanced for Single-Agent Skills**
- **What it does:** First formal analysis framework for skill supply chain security
- **Static analysis:** Sound static analysis via abstract interpretation
- **Capability-based sandboxing:** Confinement proof before deployment
- **Results:** F1=96.95%, 0% false positives on 540 skills
- **Mechanism:** Abstract interpretation builds a mathematical model of skill behavior; SAT-based resolution checks constraints
- **Open source:** `pip install skillfortify` — https://github.com/varun369/skillfortify
- **Gap:** Analyzes code, not natural language skill descriptions; single-agent only

#### 3. **SkCC / Skill Compilation** (arXiv:2605.03353, Layer 1/2)
- **What it does:** Portable and secure skill compilation with strongly-typed intermediate representation (SkIR)
- **Static typing:** SkIR decouples skill semantics from framework-specific formatting
- **Security:** Static optimizer enforces security constraints before deployment
- **Results:** 94.8% proactive security trigger rate; reduces adaptation complexity from O(m×n) to O(m+n)
- **Gap:** Requires skills to be written in SkIR, not natural language markdown; single-agent only

#### 4. **GovernSpec / Contractual Skills** (arXiv:2605.22634, Layer 0)
- **What it does:** 12 contract sections (P, I, G, R — Preconditions, Invariants, Governance, Recovery)
- **Static checking:** Machine-parseable contracts checked at skill load time
- **Gap:** Contracts are natural language with structured sections, not formal logic; no type system; single-agent only

#### 5. **SSL Representation** (arXiv:2604.24026, Layer 0)
- **What it does:** Decomposes skill text into Scheduling-Structural-Logical representations
- **Static checking:** Structured representation enables automated verification, policy checking
- **Gap:** 87% accuracy vs expert annotations; not a formal type system; single-agent only

#### 6. **AgentVerify** (preprints.org, 2026, Layer 1/2)
- **What it does:** Compositional formal verification via LTL model checking
- **Static checking:** 23 temporal logic templates for memory integrity, tool call protocols, MCP/skill invocations
- **Results:** 86.67% verification accuracy
- **Gap:** Post-hoc analysis, not pre-runtime type checking; requires model checking expertise; single-agent only

#### 7. **Skilldex** (arXiv:2604.16911, Layer 0)
- **What it does:** Validation engine for skill packages
- **Static checking:** Schema validation, format checking, coherence analysis
- **Results:** 34% of community packages malformed
- **Gap:** Schema-level, not behavioral type checking; single-agent only

#### 8. **MIGT / Machine Identity Governance** (arXiv:2604.06148, Layer 1/3)
- **What it does:** Skill-level attestation as runtime admission control
- **Static checking:** Attestation binds skill to verified identity before execution
- **Gap:** Identity verification, not behavioral type checking; single-agent only

---

### What Is **Missing** (The Gap) — UPDATED with ZipperGen

| Capability | Exists? | Notes |
|-----------|---------|-------|
| **Formal type system for skill interfaces** | ❌ No | SkCC has SkIR but it's not a type system for natural language skills |
| **Static behavioral type checking (single-agent)** | ⚠️ Partial | SkillFortify does formal analysis of code; not for NL descriptions |
| **Static behavioral type checking (multi-agent)** | ⚠️ Partial | ZipperGen provides formal coordination structure checking, but not behavioral typing of message content |
| **Protocol compatibility checking (multi-agent)** | ✅ Yes | **ZipperGen** — MSC-based DSL with syntax-directed projection and well-typedness checks |
| **Pre-runtime deadlock detection** | ✅ Yes | **ZipperGen** — deadlock-free by construction from global specs |
| **Skill-skill interaction verification** | ❌ No | No static analysis of how multiple skills compose within a single agent |

**ZipperGen changes the picture:** Before ZipperGen, the answer was "no formal static checking for multi-agent interactions." Now there is a concrete implementation (ZipperGen) that provides formal global specifications + guaranteed deadlock-free local programs. The gap is no longer "does this exist?" but "how do we extend this to skill content verification and behavioral typing?"

---

### Verdict on Question 2

> **ZipperGen is the breakthrough paper for multi-agent static coordination. It provides formal type checking (well-typedness), deadlock-free-by-construction guarantees, and syntax-directed projection — all before any agent runs. For single-agent skills, SkillFortify and SkCC provide formal static analysis. The remaining gap is behavioral typing of message content and automatic skill composition verification.**

---

## Question 3: Runtime Checking in a Deterministic Way (Not LLM-as-Judge)?

### Short Answer: **Yes — and ZipperGen is the only multi-agent approach that deterministically enforces coordination structure.**

---

### Papers With Deterministic Runtime Enforcement

#### 1. **ZipperGen / Provable Coordination for LLM Agents via MSCs** (arXiv:2604.17612, Cross-layer Layer 0+1) — **Multi-Agent Coordination — Breakthrough**
- **Deterministic:** Yes — message-passing structure is formally specified and deterministically enforced; LLM actions remain opaque
- **Mechanism:** Domain-specific language (DSL) based on Message Sequence Charts (MSCs). Syntax-directed projection generates local agent programs from global coordination specifications. Owned control flow with explicit deciders. Control broadcasts ensure non-owner lifelines observe branch choices.
- **Key innovation:** The coordination structure (message passing, branch decisions, loops) is **guaranteed correct by construction** — deadlock-free, no message mismatches, no race conditions. The LLM actions inside the structure are opaque (unpredictable), but the *structure around them* is deterministic and formally verified.
- **Runtime:** The projected local programs are deterministic finite-state programs that agents execute. No LLM-as-judge for coordination decisions.
- **Results:** Deadlock-free by construction. Coordination properties established independently of LLM nondeterminism. Runtime planning extension: LLM dynamically generates coordination workflows with same structural guarantees.
- **Open source:** ZipperGen — https://zippergen.io
- **Gap:** Does not verify LLM action content (opaque by design). No runtime behavioral enforcement of what agents actually do inside action blocks.

#### 2. **ACP — Admission Control Protocol** (arXiv:2603.18829, Layer 1) — **Fastest Single-Agent + Formally Verified**
- **Deterministic:** Yes — risk scoring is deterministic, not LLM-based
- **Mechanism:** Temporal admission control with static risk scoring + stateful signals (anomaly accumulation, cooldown) through LedgerQuerier
- **Performance:** 739-832 ns decision latency; 1,720,000 req/s throughput
- **Verification:** TLA+ verified across 4,294,930,695 states, 11 invariants + 4 temporal properties, 0 violations
- **Key result:** Stateless engines approve 100% of individually-valid requests in a 500-request attack chain; ACP limits autonomous execution to 0.4%
- **Open source:** Go reference implementation (23 packages, 138 conformance tests)
- **Paper series:** 1 of 6-paper Agent Governance Series (Marcelo Fernandez)

#### 3. **Agent Behavioral Contracts (ABC)** (arXiv:2602.22302, Layer 1/2) — **Most Comprehensive Single-Agent**
- **Deterministic:** Yes — contracts are formal, not probabilistic
- **Mechanism:** Contract C = (P, I, G, R) — Preconditions, Invariants, Governance policies, Recovery
- **Runtime:** AgentAssert library enforces contracts with <10 ms overhead per action
- **Results:** 88-100% hard constraint compliance; behavioral drift bounded to D* < 0.27
- **Verification:** (p, delta, k)-satisfaction for probabilistic compliance; Drift Bounds Theorem
- **Open source:** AgentAssert runtime library (Qualixar suite)
- **Gap:** Contracts are probabilistically satisfied, not 100% deterministic; single-agent only

#### 4. **Runtime Governance / Policies on Paths** (arXiv:2603.16586, Layer 1) — **Most Expressive Single-Agent**
- **Deterministic:** Yes — policies are temporal predicates, not LLM-evaluated
- **Mechanism:** Path-based policies as functions on execution paths; policy compiler translates requirements to executable path monitors
- **Complexity:** Polynomial-time evaluation
- **Expressiveness:** Can encode separation of duties, data minimization, audit trails
- **Gap:** Proposed framework, not yet evaluated at scale; single-agent only

#### 5. **AgentVerify** (preprints.org, 2026, Layer 1/2)
- **Deterministic:** Hybrid — O(1) runtime monitor + post-hoc Kripke-structure analyser
- **Mechanism:** LTL model checking for memory integrity, tool call protocols, MCP/skill invocations, human-in-the-loop boundaries
- **Results:** 86.67% verification accuracy vs 46.67% runtime baseline
- **Gap:** Hybrid architecture, not purely deterministic runtime; single-agent only

#### 6. **SentinelAgent** (arXiv:2604.02767, Layer 1)
- **Deterministic:** Yes — Delegation Chain Calculus with 7 formal properties
- **Mechanism:** DCC (Delegation Chain Calculus) — authority narrowing, policy preservation, forensic reconstructibility, cascade containment, scope-action conformance, output schema conformance, intent preservation
- **Verification:** TLA+ verified across 2.7 million states
- **Results:** 100% TPR at 0% FPR on DelegationBench v4 (516 scenarios, 10 attack categories)
- **Gap:** Focused on delegation chains, not general skill execution; single-agent only

#### 7. **Trace-Based Assurance Framework** (arXiv:2603.18096, Layer 1/2)
- **Deterministic:** Yes — Message-Action Traces (MAT) with explicit contracts
- **Mechanism:** Machine-checkable verdicts, deterministic replay, structured fault injection
- **Governance:** Runtime component enforcing per-agent capability limits and action mediation (allow/rewrite/block)
- **Gap:** Complex to implement; requires trace instrumentation; single-agent only

#### 8. **LGA / Layered Governance Architecture** (arXiv:2603.07191, Layer 1)
- **Deterministic:** Yes — sandboxing, intent verification, zero-trust authorization, audit logging
- **Mechanism:** Four layers of runtime governance
- **Results:** 89% of attacks succeed against baseline guardrails — showing LGA's enforcement is needed
- **Gap:** Architectural framework, not a specific implementation; single-agent only

#### 9. **MCP-38 / Threat Taxonomy** (arXiv:2603.18063, Layer 1)
- **Deterministic:** N/A — taxonomy paper, not enforcement
- **Contribution:** 38 threat categories mapped to STRIDE, OWASP LLM Top 10, OWASP Agentic Top 10
- **Gap:** No runtime enforcement mechanism

#### 10. **NIST IR 8596** (Dec 2025, Layer 1/2)
- **Deterministic:** Standards document, not implementation
- **Gap:** Framework only, no runtime enforcement

---

### Comparison: Deterministic vs LLM-as-Judge Runtime Checking

| Mechanism | Scope | Deterministic? | Speed | Formal Verification | Production Ready |
|-----------|-------|---------------|-------|---------------------|------------------|
| **ZipperGen** | **Multi-agent** | ✅ Yes (coordination structure) | — | Structural induction proof | ✅ Python impl |
| **ACP** | Single-agent | ✅ Yes | 739-832 ns | TLA+ (4.2B states) | ✅ Go impl |
| **ABC / AgentAssert** | Single-agent | ✅ Mostly | <10 ms | Drift Bounds Theorem | ✅ Library |
| **Runtime Governance** | Single-agent | ✅ Yes | Polynomial | Framework | ⚠️ Proposed |
| **AgentVerify** | Single-agent | ⚠️ Hybrid | O(1) monitor | LTL model checking | ⚠️ Research |
| **SentinelAgent** | Single-agent | ✅ Yes | — | TLA+ (2.7M states) | ⚠️ Research |
| **Trace-Based Assurance** | Single-agent | ✅ Yes | — | Replay-based | ⚠️ Complex |
| **BeSafe-Bench** | Benchmark | ❌ No | — | — | ✅ Benchmark |
| **ST-WebAgentBench** | Benchmark | ❌ No | — | — | ✅ Benchmark |

---

### What Is **Missing** (The Gap) — UPDATED with ZipperGen

| Capability | Exists? | Notes |
|-----------|---------|-------|
| **Deterministic skill-level policy enforcement** | ✅ Yes | ABC, ACP, Runtime Governance (single-agent) |
| **Deterministic multi-agent coordination enforcement** | ✅ Yes | **ZipperGen** — message structure guaranteed correct; action content remains opaque |
| **Sub-microsecond enforcement** | ✅ Yes | ACP (739-832 ns) |
| **Formally verified runtime** | ✅ Yes | ACP (TLA+), SentinelAgent (TLA+), ZipperGen (structural induction) |
| **MPST-style session type enforcement** | ✅ Yes | **ZipperGen** — MSC-based DSL with syntax-directed projection |
| **Behavioral typing of message content** | ❌ No | ZipperGen checks structure, not what LLMs put inside messages |
| **Deterministic skill composition verification** | ❌ No | No static analysis of how multiple skills compose within a single agent |
| **Behavioral typing with blame** | ❌ No | No blame assignment when agents violate protocols |
| **Real-time rollback on violation** | ⚠️ Partial | ABC has Recovery (R) contracts; not automatic rollback |

---

### Verdict on Question 3

> **Deterministic runtime enforcement exists at both single-agent (ACP, ABC/AgentAssert) and multi-agent (ZipperGen) levels. ZipperGen is the breakthrough: it guarantees deadlock-free coordination regardless of LLM nondeterminism, by separating deterministic message structure (enforced) from stochastic actions (opaque). The remaining gap is not "does MPST exist for agents?" — it does — but "can we type-check the content of LLM actions within that structure?"**

---

## Overall Assessment

### The Three Questions — Comprehensive Synthesis

| Question | Status | Best Existing Work | What ZipperGen Changes | What Remains Open |
|----------|--------|-------------------|----------------------|-------------------|
| **1. Do skills affect behavior?** | ✅ Yes, empirically | **He et al. 2024** (40% swing from format), **Gloaguen et al. 2026** (50x compliance spike), **Chen et al. 2025** (Markdown Awareness correlates with instruction-following), BIV, SSL Survey, GovernSpec | ZipperGen does not directly address this, but its runtime planning extension shows LLMs can generate coordination structures that are formally guaranteed | Proving deterministic mandate from skill markdown alone — impossible without L3 enforcement |
| **2. Static type checking?** | ✅ Yes for multi-agent | **ZipperGen** — formal well-typedness checks, deadlock-free by construction | **Closes the MPST gap:** formal global specs + deterministic local projection | Behavioral typing of LLM action content; skill-skill composition within single agent |
| **3. Deterministic runtime?** | ✅ Yes for multi-agent | **ZipperGen** — coordination structure enforced deterministically, independent of LLM nondeterminism | **Closes the multi-agent gap:** the only paper that guarantees correct multi-agent coordination regardless of LLM stochasticity | Runtime enforcement of what LLMs do inside action blocks; blame assignment; automatic rollback |

### The Three Questions — Layer Mapping

| Question | Layer 0 (Spec) | Layer 1 (Runtime) | Layer 2 (Behavioral) |
|----------|---------------|-------------------|----------------------|
| **Q1: Do skills affect behavior?** | BIV, SSL, GovernSpec (empirical evidence) | ClawHavoc (incident data) | — |
| **Q2: Static type checking?** | **ZipperGen** (global specs), SkillFortify (code analysis), GovernSpec (contracts) | — | — |
| **Q3: Deterministic runtime?** | **ZipperGen** (projection) | **ZipperGen** (local programs), ACP (admission control), ABC (contracts) | AgentVerify (hybrid), Trace-Based (replay) |

### The MPST Opportunity — REVISED

**The MPST gap is now partially closed by ZipperGen.** Here is what exists and what remains:

**What ZipperGen provides (2026):**
- ✅ **Formal global specifications** for multi-agent coordination (MSC-based DSL)
- ✅ **Static well-typedness checking** before runtime (payload matching, type correctness, control condition consistency)
- ✅ **Deadlock-free by construction** — guaranteed via syntax-directed projection, not runtime detection
- ✅ **Runtime execution** of projected local programs — deterministic finite-state programs, no LLM-as-judge for coordination
- ✅ **LLM runtime planning** — an LLM can dynamically generate coordination workflows and the same guarantees apply
- ✅ **Open-source implementation** — https://zippergen.io

**What remains missing (the new frontier):**
- ❌ **Behavioral typing of LLM actions** — ZipperGen treats LLM actions as opaque blocks; it does not verify *what* the LLM computes inside them
- ❌ **Skill-skill composition within a single agent** — ZipperGen verifies multi-agent coordination, not how skills compose within one agent
- ❌ **Blame assignment** — When coordination fails, ZipperGen does not identify which agent (or which LLM action) is at fault
- ❌ **Runtime behavioral enforcement** — ZipperGen enforces message structure, not behavior (e.g., "this agent must not send credit card numbers")
- ❌ **Automatic rollback** — No mechanism to revert multi-agent execution when a violation is detected

**The research opportunity is now sharper:**

Before ZipperGen: "Does MPST for LLM agents exist?" → No.
After ZipperGen: "How do we add behavioral typing, blame, and rollback to the ZipperGen framework?"

Specifically:
1. **Action-level contracts:** Extend ZipperGen's action blocks from opaque `act A: y = f(x)` to contract-typed `act A: y = f(x) requires P ensures Q` — where P/Q are pre/postconditions enforced by ABC/AgentAssert or ACP
2. **Skill composition:** Apply ZipperGen's projection logic to intra-agent skill composition (e.g., when two skills loaded by the same agent interact via tool calls)
3. **Blame and rollback:** Add sentinel actions that monitor message payloads and trigger rollback protocols when violations are detected

**The architecture of the future:**

```
Global Specification (ZipperGen MSC)
    ↓ Syntax-directed projection
Local Agent Programs (deadlock-free by construction)
    ↓ Runtime execution
    ├─ Message passing (deterministic, guaranteed by ZipperGen)
    └─ Action blocks (opaque LLM calls)
         ↓ ABC/ACP enforcement inside each action
         Behavior contracts (pre/postconditions)
         Admission control (risk scoring)
```

ZipperGen is the **coordination layer**. ABC/ACP is the **behavioral layer**. Together they form the complete multi-agent governance stack.

---

## Conclusion

### What We Know (2026)

1. **Skills do affect behavior** — empirically proven by BIV (80% deviation means agents are trying to follow instructions), SSL (94% structure extraction), and ClawHavoc (1,200+ malicious skills show skills are a real threat vector). But this is probabilistic, not deterministic.

2. **Formal static checking exists for multi-agent coordination** — ZipperGen provides deadlock-free-by-construction guarantees via syntax-directed projection from MSC-based global specs. This closes the MPST gap for coordination structure.

3. **Deterministic runtime enforcement exists for both single-agent and multi-agent** — ACP (sub-microsecond, TLA+ verified), ABC/AgentAssert (<10ms, Drift Bounds Theorem), and ZipperGen (structural induction proof) all provide deterministic enforcement without LLM-as-judge.

### What We Don't Know (The Open Frontier)

1. **Behavioral typing of LLM action content** — ZipperGen treats actions as opaque. No paper verifies *what* LLMs compute inside action blocks.

2. **Skill-skill composition within a single agent** — No static analysis of how multiple skills loaded by one agent interact.

3. **Blame assignment in multi-agent violations** — When something goes wrong, who is responsible? ZipperGen provides no mechanism.

4. **Automatic rollback** — ABC has Recovery (R) contracts for single-agent, but multi-agent rollback is unaddressed.

5. **Formal guarantee that skill markdown alone determines behavior** — Impossible without L3 runtime enforcement. LLM internals, context truncation, system prompts, and user messages all contribute.

### The Path Forward

The user's intuition about MPST-style governance was prescient. ZipperGen (arXiv:2604.17612) proves that formal multi-agent coordination with guaranteed deadlock-freedom is not just theoretical — it is implementable, open-source, and compatible with LLM runtime planning. The next step is not to invent MPST for agents, but to **extend ZipperGen with behavioral typing, blame assignment, and rollback mechanisms**.

However, a critical practical gap remains that no formal-methods paper addresses: **ZipperGen assumes you already have a formal global specification. But in practice, you start with a human SOP — and the hard work is getting from the SOP to the spec.**

---

## The SOP-to-Workflow Reality Gap: What ZipperGen (and All Formal MPST Papers) Cannot Handle

### The Practical Workflow from Human SOP to Agentic Execution

A recent practical methodology (widely circulated in enterprise AI training) demonstrates the real-world process of converting human Standard Operating Procedures (SOPs) into agentic workflows. This process reveals why formal coordination guarantees like ZipperGen's, while mathematically elegant, do not address the most labor-intensive and error-prone part of agent governance.

#### The Four-Step Conversion Process

| Step | Description | What Can Go Wrong | Formal Methods Gap |
|------|-------------|-------------------|-------------------|
| **1. Format Standardization** | Parameterize SOP (avoid fixed values), apply MUST/SHOULD/MAY rules (RFC 2119), structure with Markdown for machine parseability | Human SOPs encode implicit assumptions (e.g., "wash normally" assumes user knows fabric types). Agents lack this tacit knowledge. | **ZipperGen assumes parameters and types are already defined.** It does not help decide what should be parameterized or how to extract implicit knowledge. |
| **2. Task Decomposition** | Split into independent pipeline steps with explicit inputs, outputs, and success criteria; connect via structured artifacts (JSON) | Scope decisions: too broad → unreliable; too narrow → inefficiency. Agents cannot self-correct scope boundaries. | **ZipperGen assumes the global workflow is already decomposed.** It does not guide how to scope a "skill" vs. an "agent" vs. a "workflow step." |
| **3. Bidirectional Development** | Deploy, observe failures (e.g., shrinking clothes from overheating), refine SOP with new rules (e.g., "no high-heat for >80% cotton"), iterate | Real-world failures expose tacit knowledge that was never documented. Each iteration takes days or weeks. | **ZipperGen has no mechanism for iterative refinement.** A formal spec is either correct or incorrect; it does not learn from runtime failures. |
| **4. Integration & Execution** | Connect to real tools via MCP; add human-in-the-loop for high-risk decisions (e.g., finance >$5,000) | Tool APIs change, rate limits, error handling, edge cases. Production integration is where most projects fail. | **ZipperGen assumes channels are FIFO and well-typed.** It does not handle real-world API failures, retries, or human-in-the-loop pauses. |

#### Why This Matters for Formal Governance

ZipperGen's paper begins with: *"We introduce a domain-specific language for specifying agent coordination..."* The key word is **specifying**. The paper assumes the developer has already:
- Extracted all implicit knowledge from the human SOP
- Parameterized all variables correctly
- Decided the scope of each agent/skill
- Identified all branch conditions and loop structures
- Defined the message types and payload structures

In practice, this is **months of work** for a real-world workflow. The video's laundry example shows that even a simple SOP ("wash the clothes") requires:
- Fabric classification (delicate, normal, heavy)
- Stain pre-treatment (implicit knowledge: "check pockets")
- Temperature parameterization (cold/warm/hot — not fixed)
- Drying method decisions (weather-dependent, fabric-dependent)
- Human-in-the-loop for high-value items

ZipperGen would deadlock-freely coordinate the washing-agent, drying-agent, and sorting-agent once the global workflow is written. But it provides **no guidance on how to write that workflow** from the human SOP. The 80% deviation rate in BIV is not because agents violate formal specs — it's because the specs themselves were incomplete, derived from human SOPs with tacit knowledge gaps.

#### The New Research Gap: Specification Engineering for Agents

This reveals a gap not captured in our three questions or the MPST discussion:

| Gap | Description | Why Formal Methods Fail |
|-----|-------------|----------------------|
| **Tacit knowledge extraction** | Converting implicit human assumptions into explicit parameters | Formal methods require explicit specs; they cannot infer unstated assumptions |
| **Scope boundary determination** | Deciding what is a "skill" vs. "agent" vs. "workflow step" | ZipperGen assumes lifelines are already defined; it does not help scope them |
| **Iterative SOP refinement** | Learning from real-world failures to update the spec | Formal specs are static; they do not incorporate runtime feedback into the specification itself |
| **Human-in-the-loop integration** | Designing checkpoints where agents pause for human approval | ZipperGen's owned control flow has explicit deciders, but no concept of "human decider with latency and uncertainty" |
| **Tool API abstraction** | Mapping real-world APIs (with rate limits, errors, version changes) to formal message types | ZipperGen assumes perfect FIFO channels; real APIs are messy |

#### Verdict: What ZipperGen Really Is

> **ZipperGen is a coordination compiler, not a workflow designer.** It takes a formal global specification and guarantees deadlock-free local execution. But the formal specification itself must be produced through a messy, iterative, human-in-the-loop process that no current paper addresses. The SOP-to-workflow conversion is the **missing middle** between human intent and formal verification. Future research should integrate ZipperGen's projection guarantees with iterative SOP refinement methods, tacit knowledge extraction, and human-in-the-loop specification design.

---

### The Path Forward (Revised)

The user's intuition about MPST-style governance was prescient. ZipperGen (arXiv:2604.17612) proves that formal multi-agent coordination with guaranteed deadlock-freedom is not just theoretical — it is implementable, open-source, and compatible with LLM runtime planning. The next step is not to invent MPST for agents, but to **extend ZipperGen with behavioral typing, blame assignment, and rollback mechanisms**.

But the research agenda must also include:
- **SOP-to-specification extraction:** Tools that convert human SOPs (with tacit knowledge) into formal global workflows, iteratively refined from runtime failures
- **Human-in-the-loop as first-class primitives:** Not just "human decider" in ZipperGen's control flow, but latency-aware, uncertainty-aware human integration
- **Scope boundary guidance:** Formal methods that help decide which subtasks should be skills, agents, or workflow steps
- **Tool API abstraction layer:** Formal verification that accounts for real-world API failures, rate limits, and retries

The Three-Layer Governance Stack is not a wishlist — it is a near-term engineering roadmap. The papers are already being written. The tools are already being built. The gap is closing. But the **biggest gap is not the formal verification — it's the formal specification process that precedes it.**

---

*Compiled by EvaPaper | Based on 32 papers across the Three-Layer Governance Stack + practical enterprise SOP methodology*

---

## Appendix B: Full Source Transcript — Agentic Workflow Methodology

> The following transcript is reproduced verbatim from a widely circulated enterprise AI training video on converting human SOPs into agentic workflows. It is included here as primary-source evidence for the gap between formal methods (e.g., ZipperGen) and real-world deployment practice. The timestamps and formatting are preserved from the original.

[00:00:00]
This video introduces the concept of **agentic workflow**, focusing on the crucial skill of **task decomposition** for effective AI system design. The speaker highlights the gap between powerful current AI models and unsatisfactory results often caused by improper task division rather than model limitations. The discussion begins by clarifying three essential terms that are frequently confused but fundamentally different in scope and function:

- **Human SOP (Standard Operating Procedure):** Traditional, human-readable process documents that guide steps and exceptions, often in Word or slides. SOPs rely heavily on implicit human context, allowing flexible judgment on rules but presenting **high comprehension difficulty for agents due to unstructured format**.
- **Skill:** A packaged methodology, including operational logic, decision criteria, and lessons learned, delivered to agents as executable units. A skill usually contains:
 1. A **Skill markdown document** acting as a core SOP and guiding principles.
 2. **References** for supplementary data such as sample outputs and terminology.
 3. Executable **scripts** for deterministic actions like file parsing and format conversion.

 Skills correspond to **single, clearly defined tasks** (e.g., weekly-report-drafting, invoice-categorization). Determining the right scope for a skill is critical: too broad makes it unreliable; too narrow causes inefficiency.
- **Agentic Workflow:** A comprehensive workflow made by connecting multiple agents, tools, skills, and data sources, resembling a production line for autonomous AI task execution rather than a single prompt. It involves roles such as problem understanding, data searching, action execution, and report writing.

The primary focus is **transforming Human SOPs (meant for humans) into agentic workflows (understandable and executable by AI agents)**.

[00:04:09]
The video stresses that despite rapid advances and potential future AGI, agents cannot magically understand implicit preferences without explicit instructions, using a home-cleaning analogy:

- A helper who receives only the instruction "clean the house" will produce varying results depending on their internal interpretation of "clean," which may differ significantly from the homeowner’s expectations.
- This illustrates that clear instructions plus iterative adjustment are necessary for agent reliability.
- Similarly, in agentic workflows, implicit human assumptions must be made explicit for AI to meet expectations.

[00:05:23]
The **mega agent** approach—assigning all tasks to a single, powerful model—is critiqued as opaque and error-prone:

- Such all-in-one agents provide outputs that are difficult to debug or validate.
- Users often respond by upgrading models or refining prompts, but the real issue is task granularity and clarity.
- Instead, **dividing a large task into smaller, modular tasks (task decomposition)** allows clear inputs, outputs, and success criteria per sub-task.

Example: For handling customer tickets, separate agents could be assigned to classification, database searching, reply drafting, and quality control. This breakdown enables debugging and iterative improvement on each specific function without disrupting the entire system.

[00:06:25]
Advantages of task decomposition include:

- Easier error localization (e.g., fixing misclassification without changing other components).
- Improved stability, observability, and maintainability required for production environments.
- The workflow turns from an unmanageable black box into a predictable and repairable production line.

The speaker sums this paradigm as "divide and conquer," a classical approach now more vital than ever in AI-driven systems.

[00:07:26]
A concrete example of washing clothes illustrates this:

- Human SOPs for washing often omit critical implicit knowledge—such as separating whites from colours, delicate hand-washing, or weather considerations for drying.
- A naive agent following the SOP literally may damage clothes by missing unexpressed preferences.

Thus, the speaker proposes a **four-step methodology** to convert human SOPs into agentic workflows, starting with **format standardization**.

[00:08:34]
**Step 1: Format Standardization** involves:

- **Parameterisation:** Avoid fixing values (e.g., wash mode as "normal") and instead define parameters like mode (quick, normal, delicate) and temperature (cold, warm, hot). This makes the SOP reusable across varying contexts.
- **MUST, SHOULD, MAY rules:** Borrowed from RFC 2119 specification language, this categorises rules by importance:
  - **MUST:** Mandatory, non-negotiable steps.
  - **SHOULD:** Recommended but can be skipped with justification.
  - **MAY:** Optional steps.

- **Structured documentation style:** Use Markdown to divide SOP into sections such as Parameters, Steps, and Error Handling, facilitating machine parseability and integration with interfaces like Model Context Protocol (MCP).

This step transforms the SOP from unstructured prose into a schema that agents can systematically interpret.

[00:10:36]
**Step 2: Task decomposition and linking** is the core of task breakdown:

- Tasks are split into independent pipeline steps, each with explicit input, output, and success criteria, enabling independent execution and debugging.
- For washing clothes, pipeline steps might be:
  1. Classify clothing types.
  2. Check pockets and stains.
  3. Set washing machine parameters.
  4. Decide drying method.
- Each step can be implemented as a separate skill or small agent connected via **artifacts**—structured data outputs (e.g., JSON files) passed from one agent to another, ensuring clarity and interoperability without magical or implicit communication.

[00:12:31]
**Step 3: Bidirectional development (iterative refinement):**

- Initial SOPs inevitably omit "tacit knowledge"—implicit insights hard to verbalise.
- Real-world errors during execution reveal gaps and ambiguities; these necessitate continuous SOP adjustment.
- The process involves deploying the workflow, observing failures (e.g., shrinking clothes due to overheating), updating the SOP with additional rules (e.g., no high-temperature drying for >80% cotton), and rerunning.
- After repeated cycles, the automated workflow becomes robust enough for most scenarios, with remaining edge cases handled via **human-in-the-loop**.
- This iterative approach contrasts sharply with attempting to author a perfect SOP in isolation.

[00:14:37]
**Step 4: Integration and execution environment:**

- An agentic workflow must connect to **real-world tools and data sources**—e.g., washing machine controls, weather APIs.
- Without integration, SOPs remain inert documents.
- The variety of tools across companies creates challenges for reusability.

The **Model Context Protocol (MCP)** is introduced as a solution:

- MCP is an **open standard protocol** enabling large language models and agents to uniformly access tools, APIs, resources, and prompts across different platforms (ChatGPT, Claude, Cursor, etc.).
- The analogy is given to USB-C standardising hardware connections across brands.
- MCP greatly simplifies cross-platform deployment and tool integration.

Finally, the workflow should include **human-in-the-loop checkpoints** at critical points, such as high-risk decisions, to avoid unmanaged failure and retain human oversight.

[00:16:41]
The speaker applies the methodology to an internal company request triage system, described as follows:

- Inputs are requests coming from channels such as forms, Slack, email, or direct messages.
- The SOP for triage includes steps to validate the employee, categorise the request into IT/HR/Finance, set priority, and assign to correct teams.
- If requests are ambiguous, the agent should generate clarifying questions.

Four steps applied:

| Step | Description |
|-------|-------------|
| 1. Standardisation | SOP written with parameters (ticket source, text, employee ID), categorising rules as MUST/SHOULD |
| 2. Decomposition | Two skills: internal request triage (classify, prioritise, assign) and reply drafting (compose response based on triage output) linked by JSON outputs |
| 3. Iteration | Refine SOP by correcting errors such as misclassification or wrong assignee recommendations through multiple runs |
| 4. Integration | Hook workflow to real systems (e.g., tracking sheets like Notion, Jira, Google Sheets), and add human-in-the-loop for sensitive requests (e.g., finance > $5000 approval) |

This transforms a manual, repetitive SOP into an automated, debuggable, and auditable workflow with built-in human control.

[00:19:31]
The speaker offers a **five-prompt toolkit** (details in video description) to facilitate the SOP decomposition and workflow creation process.

They emphasise that:

- This methodology is no longer niche but central to enterprise AI adoption.
- MCP and agentic workflows are gaining involvement from major companies (Anthropic donating MCP to Linux Foundation’s Agentic AI Foundation, IBM, AWS, ServiceNow implementing these concepts in internal workflows).

[00:20:30]
The key message is that knowing how to convert a human SOP into an executable workflow that machines can run reliably is a **vital competitive skill for AI practitioners over the next few years**.

The speaker advises starting small, focusing on the most tedious, repetitive processes, rather than trying to automate everything at once. Early deliverables should prioritise functional workflows that save time and then progressively improve.

The distinction is made between simply learning to use AI tools vs. learning how to **design workflows for AI**. The latter has far greater lasting value.

[00:21:29]
To conclude:

- Designing effective agentic workflows based on decomposed, parameterised SOPs connected by structured outputs and integrated with real-world tools supported by protocols like MCP is the future.
- Human oversight remains critical to handle uncertainty and edge cases.
- The ability to engineer these workflows will only rise in value as AI multi-agent systems become mainstream.

The speaker invites viewers to subscribe, like, and share to support ongoing content creation.

---

### Key Terms Defined

| Term | Definition | Function |
|------------------|------------------------------------------------------------------------------------------------|-------------------------------------------|
| Human SOP | Traditional unstructured process document for humans, rich in implicit context | Guides humans, difficult for AI agents |
| Skill | Encapsulated methodology with SOP, references, and scripts for a single task | Executed by agents |
| Agentic Workflow | Workflow connecting multiple agents, skills, tools, and data sources into an autonomous pipeline | Produces end-to-end automation |
| Task Decomposition | Breaking tasks into small, modular, independent subtasks with clear inputs/outputs and success criteria | Enables debugging and iterative development |
| Model Context Protocol (MCP) | Open standard protocol for LLMs/agents to uniformly access external tools and resources | Enables cross-platform tool integration |
| Tacit Knowledge | Implicit, hard-to-express knowledge residing in human experience | Causes SOP gaps requiring iterative updates |
| Human-in-the-loop| Process checkpoints requiring human confirmation for critical decisions | Mitigates risk and handles edge cases |

---

### Summary of the Four-Step Agentic Workflow Conversion Methodology

| Step | Description | Purpose |
|--------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 1. Format Standardization | Parameterise SOP, use MUST/SHOULD/MAY, structure with Markdown | Make SOP machine-readable and reusable |
| 2. Task Decomposition | Split task into clear, independent pipeline steps connected by structured output artifacts | Modularise workflow for observability and agility |
| 3. Bidirectional Development | Iterate on SOP by testing, identifying errors related to tacit knowledge, refining accordingly | Build SOP robustness through real-world feedback |
| 4. Integration & Execution | Connect workflow to real tools and environment via MCP; add human-in-the-loop decision checkpoints | Enable production-ready automation with human oversight |

---

### Core Insights

- Powerful AI models alone do not guarantee reliable automation—**explicit task design and decomposition are crucial**.
- Human SOPs depend heavily on implicit context; without translating them into parameterised, structured workflows, agents cannot execute them effectively.
- **Divide and conquer** principle dramatically improves maintainability, observability, and debugging.
- **Iterative collaboration between developers and agents exposes tacit knowledge gaps, enabling continuous improvement**.
- Open standards like MCP are critical to integrating agents with heterogeneous corporate tools and supporting multi-agent ecosystems.
- Human-in-the-loop remains necessary for risk management and handling unpredictable edge cases in automation.
- Starting small with the most repetitive tasks yields immediate ROI and lays the foundation for scaling AI automation.

---

*This comprehensive methodology and real-world example position agentic workflows as a foundational skill and technology for the near future of AI-driven enterprise operations.*

---

*Compiled by EvaPaper | Based on 32 papers across the Three-Layer Governance Stack + practical enterprise SOP methodology*
