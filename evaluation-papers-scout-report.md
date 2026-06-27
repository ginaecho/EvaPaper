# LLM/Agent Evaluation Papers - Scout Report

> **Date:** 2026-06-25  
> **Scope:** LLM & Agent evaluation benchmarks, surveys, and frameworks (2023–2026)  
> **Sources:** arXiv, KDD, NeurIPS, ICML, ICLR, ACL, EMNLP, AAAI

---

## 1. Survey / Overview Papers (Start Here)

| Paper | Year | Venue | arXiv / Link | Notes |
|-------|------|-------|-------------|-------|
| **Evaluation and Benchmarking of LLM Agents: A Survey** | 2025 | KDD | arXiv:2507.21504 | Comprehensive taxonomy across evaluation objectives & process. Cited 179+. |
| **A Survey on Evaluation of LLM-based Agents** | 2025 | — | arXiv:2503.16416 | Descriptive survey mapping existing units of comparison. |
| **Taxonomy and Consistency Analysis of Safety Benchmarks for AI Agents** | 2026 | — | arXiv:2605.16282 | Analyzes 40 behavioral safety benchmarks (Apr 2023–Mar 2026). |
| **Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review** | 2026 | — | arXiv:2605.20351 | Systematic review of 13 malicious-code prompt corpora. |
| **A Survey on LLM Agent Security & Privacy** | 2024 | — | — | Covers security, privacy, and safety evaluation. |
| **Tool Learning with LLMs: A Survey** | 2025 | Frontiers of CS | — | Covers tool-use evaluation benchmarks. |

---

## 2. General Agent Evaluation Benchmarks

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **AgentBench** | 2023 | Evaluating LLMs as Agents | arXiv:2308.03688 |
| **WebArena** | 2023 | Realistic web environment for autonomous agents | arXiv:2307.13854 |
| **AgentBoard** | 2024 | Analytical evaluation board for multi-turn LLM agents | NeurIPS 2024 |
| **τ-bench** | 2024 | Tool-agent-user interaction in real-world domains | arXiv:2406.12045 |
| **AssistantBench** | 2024 | Can web agents solve realistic, time-consuming tasks? | arXiv:2407.15711 |
| **TheAgentCompany** | 2024 | — | — |
| **Agent-as-a-Judge** | 2024 | Evaluate agents with agents | arXiv:2410.10934 |
| **AgentAtlas** | 2026 | Beyond outcome leaderboards for LLM agents | arXiv:2605.20530 |
| **OdysseyBench** | 2025 | Long-horizon benchmark for LLM agents | arXiv:2508.09124 |
| **Trip-Bench** | 2026 | Long-horizon interactive agents in real-world scenarios | arXiv:2602.01675 |
| **LifelongAgentBench** | 2025 | Agent lifelong learning evaluation | — |
| **LTMBenchmark** | 2024 | Long-term memory evaluation for agents | — |
| **AutoEnv** | 2025 | Auto-generated heterogeneous worlds for cross-env testing | — |

---

## 3. Tool Use & Planning Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **T-Eval** | 2024 | Tool utilization capability step-by-step | ACL 2024 |
| **ToolEmu** | 2024 | Tool-use simulation & safety | — |
| **MetaTool** | 2024 | Tool learning benchmark | — |
| **COMPASS** | 2025 | Multi-turn tool-mediated planning & preference optimization | arXiv:2510.07043 |
| **C-ToolEval** | 2024 | Chinese benchmark for LLM-powered agent API interactions | ACL Findings |
| **Spa-Bench** | 2024 | Smartphone agent evaluation | NeurIPS 2024 Workshop |
| **Mobile-Env / MobileBench** | 2024 | Mobile GUI interaction evaluation | — |
| **LangSuitE** | 2024 | — | — |
| **Re-ReST** | 2024 | — | — |
| **XMC-Agent** | 2024 | Dynamic navigation over hierarchical index | ACL Findings |

---

## 4. Coding / Software Engineering Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **SWE-bench** | 2024 | Real-world GitHub issue resolution | ICLR 2024 |
| **SWE-bench Pro** | 2025 | More challenging SE agent benchmark | — |
| **SWE-PolyBench** | 2025 | Multi-language repo-level coding agents | arXiv:2504.08703 |
| **ClassEval** | 2023 | Class-level code generation | arXiv:2308.01861 |
| **EvoCodeBench** | 2024 | Evolving code generation with domain-specific eval | NeurIPS D&B |
| **RepoBench** | 2024 | Repository-level code auto-completion | ICLR 2024 |
| **AutoCodeRover** | 2024 | Autonomous program improvement | ISSTA 2024 |
| **DafnyBench** | 2025 | Formal software verification | TMLR 2025 |
| **PatchEval** | 2025 | Evaluating LLMs on patching real-world vulnerabilities | arXiv:2511.11019 |
| **VulnRepairEval** | 2025 | Exploit-based vulnerability repair evaluation | arXiv:2509.03331 |

---

## 5. Safety, Security & Alignment Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **AgentHarm** | 2024/25 | Measuring harmfulness of LLM agents | arXiv:2410.09024 |
| **AgentDojo** | 2024 | Prompt injection & adversarial testing | — |
| **AgentPoison** | 2024 | Backdoor attacks on LLM-based agents | — |
| **SafeAgentBench** | 2024 | Safe task planning for embodied LLM agents | arXiv:2412.13178 |
| **Agent-Safety Bench (ASB)** | 2024 | Formalizing attacks & defenses in LLM agents | arXiv:2410.02644 |
| **R-Judge** | 2024 | Risk judgment for agents | — |
| **CASA** | 2025 | Context-aware safety assessment | — |
| **Cybench** | 2024 | Cybersecurity capabilities & risks of LLMs | arXiv:2408.08926 |
| **CyberGym** | 2025 | Real-world cybersecurity capabilities at scale | arXiv:2506.02548 |
| **CVE-Bench** | 2025 | AI agents exploiting real-world web app vulnerabilities | arXiv:2503.17332 |
| **OpenAgentSafety** | 2025 | Safety evaluation for open-source LLM agents | arXiv:2507.06134 |
| **MCPsecBench** | 2025 | Security benchmark for Model Context Protocols | — |
| **MAGPIE** | 2025 | Multi-agent contextual privacy evaluation | — |
| **AgentLeak** | 2026 | Privacy leakage in multi-agent LLM systems | — |
| **AgentLAB** | 2026 | Long-horizon attacks on LLM agents | — |
| **OR-Bench** | 2024/25 | Over-refusal benchmark for LLMs | ICML 2025 |
| **XSTest** | 2023/24 | Exaggerated safety behaviors | NAACL 2024 |
| **RefusalBench** | 2026 | Generative evaluation of selective refusal | EACL 2026 |
| **VSCBench** | 2025 | Vision-language model safety calibration | ACL 2025 Findings |
| **RealToxicityPrompts** | 2020 | Toxicity detection | — |

---

## 6. Multi-Agent & Collaboration Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **AgentSims** | 2023 | Multi-agent social simulation | — |
| **MATSA** | 2024 | Multi-agent task & social analysis | — |
| **GAMEBENCH** | 2024 | Multi-agent game evaluation | — |
| **BALROG** | 2024 | — | — |
| **MAGPIE** | 2025 | Multi-agent privacy evaluation | — |
| **AgentLAB** | 2026 | Long-horizon attacks on multi-agent systems | — |
| **Agent Drift** | 2026 | Behavioral degradation in multi-agent LLM systems | arXiv:2601.04170 |
| **Pre-Act** | 2025 | Multi-step planning & reasoning improves acting | arXiv:2505.09970 |

---

## 7. Reasoning & RAG Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **MMLU / MMLU-Pro** | 2020+ | Massive multitask language understanding | — |
| **GPQA** | 2024 | Graduate-level Google-proof Q&A | COLM 2024 |
| **Folio** | 2024 | Natural language reasoning with first-order logic | EMNLP 2024 |
| **CriticBench** | 2024 | Critique-correct reasoning | ACL Findings |
| **R2MED** | 2025 | Reasoning-driven medical retrieval | — |
| **GraphRAG-Bench** | 2025 | Graph retrieval-augmented generation | — |
| **MR2-Bench** | 2025 | Multimodal retrieval reasoning | — |
| **BRIGHT** | 2024 | Reasoning-intensive retrieval | — |
| **RAGAS** | 2024 | Automated RAG evaluation | — |
| **ScienceAgentBench** | 2024 | Data-driven scientific discovery | arXiv:2410.05080 |
| **SchHorizon** | 2025 | AI-for-science readiness | KDD 2025 |
| **InnovatorBench** | 2025 | Agents conducting innovative LLM research | — |

---

## 8. Deep Research & Web Agent Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **GAIA** | 2023 | General AI Assistants | — |
| **BrowseComp** | 2025 | Browsing agent benchmark | arXiv:2504.12516 |
| **BrowseComp-Plus** | 2025 | Fair & transparent deep-research evaluation | — |
| **DeepResearch Bench** | 2025 | Comprehensive deep research agent benchmark | — |
| **DeepResearchGym** | 2025 | Reproducible evaluation sandbox for deep research | — |
| **DeepScholar-Bench** | 2025 | Live benchmark for generative research synthesis | — |
| **DeepResearch-9K** | 2026 | Challenging deep-research agent dataset | — |
| **Deep Research Arena** | 2026 | LLM research abilities via seminar tasks | AAAI 2026 |
| **DeepFact** | 2026 | Co-evolving benchmarks & agents for factuality | — |
| **FieldWorkArena** | 2025 | Agentic AI for real field work tasks | — |
| **WideSearch** | 2025 | Agentic broad info-seeking | — |
| **Mind2Web 2** | 2025 | Agentic search with agent-as-a-judge | — |
| **WebLinX** | 2024 | Web agent robustness | — |

---

## 9. Embodied & Robotics Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **ALFWorld** | 2021 | Embodied agent reasoning | — |
| **OSWorld** | 2024 | Multimodal agents for open-ended computer tasks | NeurIPS 2024 |
| **NavSpace** | 2026 | Spatial intelligence in embodied navigation | ICRA 2026 |
| **SafeAgentBench** | 2024 | Safe task planning for embodied agents | — |
| **CRADLE** | 2024 | LLM-based agent in video games (Red Dead Redemption II) | — |
| **Optimus-1** | 2024 | Memory & context retention for embodied agents | — |
| **LoCoMo** | 2024 | Long-context memory evaluation | — |
| **LongEval** | 2023 | Long-context evaluation | — |
| **SocialBench** | 2024 | Social interaction evaluation | — |

---

## 10. Reliability & Consistency

| Paper/Benchmark | Year | Focus | Link |
|----------------|------|-------|------|
| **ReliabilityBench** | 2026 | Multi-dimensional LLM reliability | arXiv:2601.06112 |
| **Towards a Science of AI Agent Reliability** | 2026 | Agent reliability framework | arXiv:2602.16666 |
| **τ-Bench** | 2024 | Consistency (pass^k) | arXiv:2406.12045 |
| **HELM** | 2023 | Holistic evaluation of language models | — |
| **Benchmark Illusion** | 2026 | Disagreement among LLMs & scientific consequences | arXiv:2602.11898 |
| **Lost in the Middle** | 2024 | Long-context usage | TACL 2024 |
| **METR Long-Horizon Study** | 2025 | Measuring AI ability to complete long tasks | arXiv:2503.14499 |

---

## 11. Self-Reflection & Meta-Cognitive Evaluation

| Benchmark | Year | Focus | Link |
|-----------|------|-------|------|
| **LLF-Bench** | 2023 | Standardized self-reflection benchmarks | — |
| **LLM-Evolve** | 2024 | Self-reflection on standard benchmarks | — |
| **Reflection-Bench** | 2024 | Cognitive reflection capabilities | — |
| **Agent Drift** | 2026 | Behavioral degradation over extended interactions | arXiv:2601.04170 |
| **Trace** | 2025 | Test-time exploration & evolving tasks | — |

---

## 12. Notable GitHub Awesome Lists (Curated Resources)

| Resource | Link | Description |
|----------|------|-------------|
| **Awesome LLM Evaluation** | https://alopatenko.github.io/LLMEvaluation/ | Massive compendium of LLM evaluation papers & benchmarks |
| **Awesome Embodied Robotics & Agent** | https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent | VLM + LLM embodied AI research |
| **Awesome Refusal Suppression** | https://github.com/ant-research/Awesome-Refusal-Suppression | Refusal suppression research |
| **Awesome LLM Agent Privacy** | https://github.com/yagobski/awesome-llm-agent-privacy | Privacy, security, compliance in agents |

---

## Key Takeaways

1. **Two "must-read" surveys:** arXiv:2507.21504 (KDD) and arXiv:2503.16416 cover the full landscape.
2. **Safety evaluation is booming:** 40+ behavioral safety benchmarks identified just between 2023–2026.
3. **Long-horizon is the new frontier:** OdysseyBench, Trip-Bench, LifelongAgentBench, METR study.
4. **Agent-as-a-Judge is emerging:** Using agents to evaluate agents (arXiv:2410.10934).
5. **Deep research evaluation is hot:** BrowseComp, DeepResearch Bench, DeepFact (all 2025–2026).
6. **Reliability is under-studied:** Only ReliabilityBench (2026) and τ-Bench tackle consistency formally.

---

*Scout complete. 80+ papers/benchmarks identified across 12 categories.*
