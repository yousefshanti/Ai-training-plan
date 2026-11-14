# Flowless AI Training

My work through the [Flowless AI Training Roadmap](roadmap/): Python foundations, data analysis and data science, generative AI, and a final end-to-end project. Each module has its own folder and a GitHub issue that tracks its practical tasks.

## Progress

**8 of 14 modules complete (57%)**

`███████████░░░░░░░░░` 57%

**Currently working on:** Phase 3 – Module 4: Prompt Engineering

| Phase | Module | Status | Folder | Issue |
|---|---|:---:|---|---|
| 1 – Foundations | Python, Jupyter search task, GitHub fundamentals | ✅ | [phase-1](phase-1/) | [#1](https://github.com/yousefshanti/Ai-training-plan/issues/1) · [#2](https://github.com/yousefshanti/Ai-training-plan/issues/2) · [#3](https://github.com/yousefshanti/Ai-training-plan/issues/3) |
| 2 – Data Analysis & Data Science | Module 1: Data Fundamentals | ✅ | [module-1-data-fundamentals](phase-2/module-1-data-fundamentals/) | [#4](https://github.com/yousefshanti/Ai-training-plan/issues/4) |
| 2 – Data Analysis & Data Science | Module 2: Data Visualization & EDA | ✅ | [module-2-data-visualization-eda](phase-2/module-2-data-visualization-eda/) | [#5](https://github.com/yousefshanti/Ai-training-plan/issues/5) |
| 2 – Data Analysis & Data Science | Module 3: Time Series Data Analysis | ✅ | [module-3-time-series](phase-2/module-3-time-series/) | [#6](https://github.com/yousefshanti/Ai-training-plan/issues/6) |
| 2 – Data Analysis & Data Science | Module 4: Geospatial Data Analysis | ✅ | [module-4-geospatial](phase-2/module-4-geospatial/) | [#7](https://github.com/yousefshanti/Ai-training-plan/issues/7) |
| 3 – Generative AI | Module 1: Generative AI & Agent Fundamentals | ✅ | [module-1-genai-agent-fundamentals](phase-3/module-1-genai-agent-fundamentals/) | [#8](https://github.com/yousefshanti/Ai-training-plan/issues/8) |
| 3 – Generative AI | Module 2: AI Product Engineering | ✅ | [module-2-ai-product-engineering](phase-3/module-2-ai-product-engineering/) | [#9](https://github.com/yousefshanti/Ai-training-plan/issues/9) |
| 3 – Generative AI | Module 3: Retrieval-Augmented Generation (RAG) — PDF → chunks → MiniLM embeddings → FAISS → Groq LLM. Tuning result: all 18 settings tied at hit rate 1.0 on the 1-page PDF; default pick all-MiniLM-L6-v2, 100-word chunks, k=2. [Run output](phase-3/module-3-rag/rag_pipeline_output.md) | ✅ | [module-3-rag](phase-3/module-3-rag/) | [#10](https://github.com/yousefshanti/Ai-training-plan/issues/10) |
| 3 – Generative AI | Module 4: Prompt Engineering & Context Engineering | 🚧 | — | [#11](https://github.com/yousefshanti/Ai-training-plan/issues/11) |
| 3 – Generative AI | Module 5: LangChain & Building Agents | ⬜ | — | [#12](https://github.com/yousefshanti/Ai-training-plan/issues/12) |
| 3 – Generative AI | Module 6: Model Context Protocol (MCP) | ⬜ | — | [#13](https://github.com/yousefshanti/Ai-training-plan/issues/13) |
| 3 – Generative AI | Module 7: Multi-Agent Systems | ⬜ | — | [#14](https://github.com/yousefshanti/Ai-training-plan/issues/14) |
| 3 – Generative AI | Module 8: AI Evaluation & Benchmarking | ⬜ | — | [#15](https://github.com/yousefshanti/Ai-training-plan/issues/15) |
| Final Project | End-to-End Data Science Pipeline (Streamlit) | ⬜ | — | [#16](https://github.com/yousefshanti/Ai-training-plan/issues/16) |

✅ done · 🚧 in progress · ⬜ to do

## Milestones

| Tag | Meaning |
|---|---|
| `phase-1-complete` | Phase 1 finished |
| `phase-2-complete` | Phase 2 finished |
| `rag-project-done` | RAG pipeline (Phase 3 Module 3) finished |

## Setup

```bash
pip install -r requirements.txt
```

The RAG pipeline needs a Groq API key in `phase-3/module-3-rag/.env` (`GROQ_API_KEY=...`). The file is git-ignored.
