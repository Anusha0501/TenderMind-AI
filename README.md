# TenderMind-AI

TenderMind-AI is an autonomous government tender monitoring and qualification platform built as a step-by-step learning project for Agentic AI, LLM Engineering, FastAPI, Playwright, LangGraph, and production SaaS architecture.

## Current Status

Phase 1 is complete: product and architecture planning.

No application code has been generated yet. This is intentional because the project is being built step by step with clear explanations before implementation.

## Phase 1 Documents

- [Product Requirements Document](docs/product/prd.md)
- [System Architecture](docs/architecture/system-architecture.md)
- [Agent Workflow](docs/architecture/agent-workflow.md)
- [Database Schema](docs/database/schema.md)
- [API Design](docs/api/api-design.md)
- [Folder Structure](docs/folder-structure.md)

## Planned Stack

### Frontend

- Next.js 15
- TypeScript
- Tailwind CSS
- shadcn/ui
- Recharts
- Framer Motion

### Backend

- FastAPI
- Pydantic
- SQLModel
- PostgreSQL on Supabase Free

### AI

- LangGraph
- LangChain
- Gemini 2.5 Flash Free Tier

### Automation and Scraping

- Celery
- Redis
- Playwright

### Monitoring and Deployment

- LangSmith Free
- Loguru
- Vercel
- Railway

## Learning Goal

By completing this project, a beginner should be able to explain:

- how AI agents are orchestrated with LangGraph,
- why human-in-the-loop workflows matter,
- how Playwright scraping differs from HTML-only scraping,
- how FastAPI services are structured,
- how production AI systems are logged, monitored, tested, and deployed.
