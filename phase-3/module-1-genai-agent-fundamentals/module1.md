# Phase 3 – Module 1: Generative AI & Agent Fundamentals

## 1. Generative AI and AI Agents
Generative AI refers to models, mainly Large Language Models (LLMs), that learn patterns from massive data and generate new content such as text, code, or images by predicting the next token. On its own, an LLM only responds; it cannot act. An **AI agent** wraps the LLM with tools, memory, and a goal, so it can plan and execute multi-step tasks with limited human input.

**Example:** a water-network monitoring agent that reads pressure and flow data, detects a possible leak, checks historical records, and drafts a maintenance alert for an engineer.

## 2. Architecture and Decision-Making
An agent combines five components:

- **Perception:** inputs and sensors.
- **Reasoning:** the LLM.
- **Action:** tools and APIs.
- **Memory:** short-term context and long-term storage.
- **Communication:** with users or other agents.

Decisions usually follow a **ReAct** loop (Thought → Action → Observation, repeated), or a plan-first approach such as **ReWOO** or **Plan-and-Execute**. Reliable systems add guardrails and human approval before irreversible actions.

## 3. Frameworks and Design Patterns
Four core patterns appear across the sources:

- **Reflection:** self-critique and revision.
- **Tool Use**, with ReAct often treated as the loop that drives it.
- **Planning.**
- **Multi-Agent Collaboration.**

Multi-agent systems are organized as sequential, parallel, router, hierarchical, or network topologies.

Each framework fits different patterns:

- **LangChain** and its graph extension **LangGraph** are strongest at integrating tools and building cyclic, stateful workflows, so they suit Tool Use, ReAct, and Reflection.
- **LlamaIndex** focuses on connecting LLMs to enterprise data through retrieval (RAG), which makes it a natural choice for retrieval-based tool use.
- **AutoGen** is built around conversational collaboration between agents, so it fits Multi-Agent and Planning workflows.
- **OpenAI Agents SDK** offers handoffs, agents-as-tools, and built-in guardrails, which map directly to Router and Hierarchical designs.

**Key design rule:** start with a single agent, and add complexity only when it measurably improves results.
