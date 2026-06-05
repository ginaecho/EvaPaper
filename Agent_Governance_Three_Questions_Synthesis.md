# Agent Governance Research Summary: Three Critical Questions

> Compiled by EvaPaper | June 6, 2026
> Based on 28 papers across the Three-Layer Governance Stack

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

---

### What **No** Paper Claims

**No paper proves:**
- "Skill markdown completely determines agent behavior" — false, system prompts, context truncation, and model internals also matter
- "Agents always follow skill instructions" — BIV's 80% deviation rate disproves this
- "Natural language instructions are formally binding" — this requires L3 runtime enforcement (see Question 3)

---

### Verdict on Question 1

> **Skills markdown affects behavior at L1-L2 (probabilistic influence). No paper proves deterministic mandate without runtime enforcement (L3). The influence is real, material, and measurable — but not guaranteed.**

If you need **guaranteed** behavior, you need:
- **Static:** Formal specification + type checking (see Question 2)
- **Runtime:** Deterministic enforcement (see Question 3)

---

## Question 2: Formal Static Typing / Checking Before Runtime?

### Short Answer: **Yes, multiple approaches exist — but none are universally deployed.**

---

### Papers With Static Analysis / Pre-Runtime Verification

#### 1. **SkillFortify** (arXiv:2603.00195, Layer 0/1) — **Most Advanced**
- **What it does:** First formal analysis framework for skill supply chain security
- **Static analysis:** Sound static analysis via abstract interpretation
- **Capability-based sandboxing:** Confinement proof before deployment
- **Results:** F1=96.95%, 0% false positives on 540 skills
- **Mechanism:** Abstract interpretation builds a mathematical model of skill behavior; SAT-based resolution checks constraints
- **Open source:** `pip install skillfortify` — https://github.com/varun369/skillfortify
- **Gap:** Analyzes code, not natural language skill descriptions

#### 2. **SkCC / Skill Compilation** (arXiv:2605.03353, Layer 1/2)
- **What it does:** Portable and secure skill compilation with strongly-typed intermediate representation (SkIR)
- **Static typing:** SkIR decouples skill semantics from framework-specific formatting
- **Security:** Static optimizer enforces security constraints before deployment
- **Results:** 94.8% proactive security trigger rate; reduces adaptation complexity from O(m×n) to O(m+n)
- **Gap:** Requires skills to be written in SkIR, not natural language markdown

#### 3. **GovernSpec / Contractual Skills** (arXiv:2605.22634, Layer 0)
- **What it does:** 12 contract sections (P, I, G, R — Preconditions, Invariants, Governance, Recovery)
- **Static checking:** Machine-parseable contracts checked at skill load time
- **Gap:** Contracts are natural language with structured sections, not formal logic; no type system

#### 4. **SSL Representation** (arXiv:2604.24026, Layer 0)
- **What it does:** Decomposes skill text into Scheduling-Structural-Logical representations
- **Static checking:** Structured representation enables automated verification, policy checking
- **Gap:** 87% accuracy vs expert annotations; not a formal type system

#### 5. **AgentVerify** (preprints.org, 2026, Layer 1/2)
- **What it does:** Compositional formal verification via LTL model checking
- **Static checking:** 23 temporal logic templates for memory integrity, tool call protocols, MCP/skill invocations
- **Results:** 86.67% verification accuracy
- **Gap:** Post-hoc analysis, not pre-runtime type checking; requires model checking expertise

#### 6. **Skilldex** (arXiv:2604.16911, Layer 0)
- **What it does:** Validation engine for skill packages
- **Static checking:** Schema validation, format checking, coherence analysis
- **Results:** 34% of community packages malformed
- **Gap:** Schema-level, not behavioral type checking

#### 7. **MIGT / Machine Identity Governance** (arXiv:2604.06148, Layer 1/3)
- **What it does:** Skill-level attestation as runtime admission control
- **Static checking:** Attestation binds skill to verified identity before execution
- **Gap:** Identity verification, not behavioral type checking

---

### What Is **Missing** (The Gap)

| Capability | Exists? | Notes |
|-----------|---------|-------|
| **Formal type system for skill interfaces** | ❌ No | SkCC has SkIR but it's not a type system for natural language skills |
| **Static behavioral type checking** | ⚠️ Partial | SkillFortify does formal analysis of code; not for NL descriptions |
| **Protocol compatibility checking** | ❌ No | No MPST-style session type checking for multi-agent interactions |
| **Pre-runtime deadlock detection** | ❌ No | Not addressed in any paper |
| **Skill-skill interaction verification** | ❌ No | No static analysis of how multiple skills compose |

---

### Verdict on Question 2

> **Static analysis exists (SkillFortify, SkCC) but is limited to code artifacts or structured representations. There is no formal type system for natural language skill descriptions, and no MPST-style static protocol checking for multi-agent interactions. This is a research gap.**

---

## Question 3: Runtime Checking in a Deterministic Way (Not LLM-as-Judge)?

### Short Answer: **Yes — multiple deterministic runtime enforcement mechanisms exist, some formally verified.**

---

### Papers With Deterministic Runtime Enforcement

#### 1. **ACP — Admission Control Protocol** (arXiv:2603.18829, Layer 1) — **Fastest + Formally Verified**
- **Deterministic:** Yes — risk scoring is deterministic, not LLM-based
- **Mechanism:** Temporal admission control with static risk scoring + stateful signals (anomaly accumulation, cooldown) through LedgerQuerier
- **Performance:** 739-832 ns decision latency; 1,720,000 req/s throughput
- **Verification:** TLA+ verified across 4,294,930,695 states, 11 invariants + 4 temporal properties, 0 violations
- **Key result:** Stateless engines approve 100% of individually-valid requests in a 500-request attack chain; ACP limits autonomous execution to 0.4%
- **Open source:** Go reference implementation (23 packages, 138 conformance tests)
- **Paper series:** 1 of 6-paper Agent Governance Series (Marcelo Fernandez)

#### 2. **Agent Behavioral Contracts (ABC)** (arXiv:2602.22302, Layer 1/2) — **Most Comprehensive**
- **Deterministic:** Yes — contracts are formal, not probabilistic
- **Mechanism:** Contract C = (P, I, G, R) — Preconditions, Invariants, Governance policies, Recovery
- **Runtime:** AgentAssert library enforces contracts with <10 ms overhead per action
- **Results:** 88-100% hard constraint compliance; behavioral drift bounded to D* < 0.27
- **Verification:** (p, delta, k)-satisfaction for probabilistic compliance; Drift Bounds Theorem
- **Open source:** AgentAssert runtime library (Qualixar suite)
- **Gap:** Contracts are probabilistically satisfied, not 100% deterministic

#### 3. **Runtime Governance / Policies on Paths** (arXiv:2603.16586, Layer 1) — **Most Expressive**
- **Deterministic:** Yes — policies are temporal predicates, not LLM-evaluated
- **Mechanism:** Path-based policies as functions on execution paths; policy compiler translates requirements to executable path monitors
- **Complexity:** Polynomial-time evaluation
- **Expressiveness:** Can encode separation of duties, data minimization, audit trails
- **Gap:** Proposed framework, not yet evaluated at scale

#### 4. **AgentVerify** (preprints.org, 2026, Layer 1/2)
- **Deterministic:** Hybrid — O(1) runtime monitor + post-hoc Kripke-structure analyser
- **Mechanism:** LTL model checking for memory integrity, tool call protocols, MCP/skill invocations, human-in-the-loop boundaries
- **Results:** 86.67% verification accuracy vs 46.67% runtime baseline
- **Gap:** Hybrid architecture, not purely deterministic runtime

#### 5. **SentinelAgent** (arXiv:2604.02767, Layer 1)
- **Deterministic:** Yes — Delegation Chain Calculus with 7 formal properties
- **Mechanism:** DCC (Delegation Chain Calculus) — authority narrowing, policy preservation, forensic reconstructibility, cascade containment, scope-action conformance, output schema conformance, intent preservation
- **Verification:** TLA+ verified across 2.7 million states
- **Results:** 100% TPR at 0% FPR on DelegationBench v4 (516 scenarios, 10 attack categories)
- **Gap:** Focused on delegation chains, not general skill execution

#### 6. **Trace-Based Assurance Framework** (arXiv:2603.18096, Layer 1/2)
- **Deterministic:** Yes — Message-Action Traces (MAT) with explicit contracts
- **Mechanism:** Machine-checkable verdicts, deterministic replay, structured fault injection
- **Governance:** Runtime component enforcing per-agent capability limits and action mediation (allow/rewrite/block)
- **Gap:** Complex to implement; requires trace instrumentation

#### 7. **LGA / Layered Governance Architecture** (arXiv:2603.07191, Layer 1)
- **Deterministic:** Yes — sandboxing, intent verification, zero-trust authorization, audit logging
- **Mechanism:** Four layers of runtime governance
- **Results:** 89% of attacks succeed against baseline guardrails — showing LGA's enforcement is needed
- **Gap:** Architectural framework, not a specific implementation

#### 8. **MCP-38 / Threat Taxonomy** (arXiv:2603.18063, Layer 1)
- **Deterministic:** N/A — taxonomy paper, not enforcement
- **Contribution:** 38 threat categories mapped to STRIDE, OWASP LLM Top 10, OWASP Agentic Top 10
- **Gap:** No runtime enforcement mechanism

#### 9. **NIST IR 8596** (Dec 2025, Layer 1/2)
- **Deterministic:** Standards document, not implementation
- **Gap:** Framework only, no runtime enforcement

---

#### 10. **ZipperGen / Provable Coordination for LLM Agents via MSCs** (arXiv:2604.17612, Cross-layer Layer 0+1)
- **Deterministic:** Yes — message-passing structure is formally specified; LLM actions remain opaque
- **Mechanism:** Domain-specific language based on Message Sequence Charts (MSCs). Syntax-directed projection generates deadlock-free local agent programs from global coordination specifications. Owned control flow with explicit deciders. Control broadcasts ensure non-owner lifelines observe branch choices.
- **Results:** Deadlock-free by construction. Coordination properties established independently of LLM nondeterminism. Runtime planning extension: LLM generates workflows with same structural guarantees.
- **Open source:** ZipperGen — https://zippergen.io
- **Gap:** Does not verify LLM action content (opaque by design). No runtime behavioral enforcement beyond coordination structure.

---

### Comparison: Deterministic vs LLM-as-Judge Runtime Checking

| Mechanism | Deterministic? | Speed | Formal Verification | Production Ready |
|-----------|---------------|-------|---------------------|------------------|
| **ACP** | ✅ Yes | 739-832 ns | TLA+ (4.2B states) | ✅ Go impl |
| **ABC / AgentAssert** | ✅ Mostly | <10 ms | Drift Bounds Theorem | ✅ Library |
| **Runtime Governance** | ✅ Yes | Polynomial | Framework | ⚠️ Proposed |
| **AgentVerify** | ⚠️ Hybrid | O(1) monitor | LTL model checking | ⚠️ Research |
| **SentinelAgent** | ✅ Yes | — | TLA+ (2.7M states) | ⚠️ Research |
| **Trace-Based Assurance** | ✅ Yes | — | Replay-based | ⚠️ Complex |
| **BeSafe-Bench** | ❌ No | — | — | ✅ Benchmark |
| **ST-WebAgentBench** | ❌ No | — | — | ✅ Benchmark |

---

### What Is **Missing** (The Gap)

| Capability | Exists? | Notes |
|-----------|---------|-------|
| **Deterministic skill-level policy enforcement** | ✅ Yes | ABC, ACP, Runtime Governance |
| **Sub-microsecond enforcement** | ✅ Yes | ACP (739-832 ns) |
| **Formally verified runtime** | ✅ Yes | ACP (TLA+), SentinelAgent (TLA+) |
| **MPST-style session type enforcement** | ❌ No | No multi-party session type checking at runtime |
| **Deterministic skill composition verification** | ❌ No | No runtime checking that composed skills preserve invariants |
| **Behavioral typing with blame** | ❌ No | No blame assignment when agents violate protocols |
| **Real-time rollback on violation** | ⚠️ Partial | ABC has Recovery (R) contracts; not automatic rollback |

---

### Verdict on Question 3

> **Deterministic runtime enforcement exists and is production-ready (ACP, ABC/AgentAssert). These are not LLM-as-judge — they use formal risk scoring, temporal logic, and contract enforcement. The fastest (ACP) is sub-microsecond with TLA+ formal verification. However, MPST-style multi-party session type enforcement and automatic rollback are still research gaps.**

---

## Overall Assessment

### The Three Questions — Synthesis

| Question | Status | Best Existing Work | Gap |
|----------|--------|-------------------|-----|
| **1. Do skills affect behavior?** | ✅ Yes, empirically | BIV, SSL Survey, GovernSpec | No formal guarantee without L3 enforcement |
| **2. Static type checking?** | ⚠️ Partial | SkillFortify, SkCC, GovernSpec | No formal type system for NL skills; no MPST static checking |
| **3. Deterministic runtime?** | ✅ Yes | ACP, ABC/AgentAssert, Runtime Governance | No MPST runtime enforcement; no automatic rollback |

### The MPST Opportunity

Your intuition is correct: **the gap is at the intersection of all three.**

What doesn't exist yet:
- **Static:** MPST session types for multi-agent skill interactions, checked before runtime
- **Runtime:** Deterministic enforcement of MPST protocols with blame assignment and rollback
- **Behavioral guarantee:** Proof that if all agents follow the protocol, global invariants hold

The closest existing work:
- **ACP** — fast, formally verified, temporal admission control (single agent)
- **ABC** — behavioral contracts with probabilistic compliance (single agent)
- **SentinelAgent** — formal delegation chain verification (multi-agent, but not general protocols)
- **Runtime Governance** — temporal predicates on paths (expressive, but not yet multi-agent)

**The research opportunity:** Extend MPST to the agent skill domain — static session type checking for skill composition, plus deterministic runtime enforcement with sub-microsecond overhead and formal verification.

---

*Compiled by EvaPaper | Based on 28 papers across the Three-Layer Governance Stack*
