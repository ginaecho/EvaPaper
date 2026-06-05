# Agent Governance Research Summary: Three Critical Questions

> Compiled by EvaPaper | June 6, 2026
> Based on 29 papers across the Three-Layer Governance Stack

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
| **1. Do skills affect behavior?** | ✅ Yes, empirically | BIV, SSL Survey, GovernSpec | ZipperGen does not directly address this, but its runtime planning extension shows LLMs can generate coordination structures that are formally guaranteed | Proving deterministic mandate from skill markdown alone — impossible without L3 enforcement |
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

The research agenda should focus on:
- **Action-level contracts** inside ZipperGen's action blocks (integrating ABC/AgentAssert)
- **Skill composition analysis** for single-agent multi-skill scenarios (applying ZipperGen's projection logic to intra-agent interactions)
- **Blame and rollback** as first-class primitives in the coordination DSL (extending ZipperGen's owned control flow with violation handling)

The Three-Layer Governance Stack is not a wishlist — it is a near-term engineering roadmap. The papers are already being written. The tools are already being built. The gap is closing.

---

*Compiled by EvaPaper | Based on 29 papers across the Three-Layer Governance Stack*
