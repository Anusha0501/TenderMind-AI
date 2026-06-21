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

## Demo-Ready MVP

This repository now includes a production-structured demo MVP:

- `apps/api`: FastAPI backend with SQLModel persistence, scraper adapters, opportunity scoring, eligibility report generation, health checks, and tests.
- `apps/web`: Next.js 15 dashboard shell with dark SaaS UI pages for dashboard, tenders, reports, analytics, and settings.
- `infra`: deployment checklist for Railway, Vercel, Supabase, and Upstash.
- `.github`: PR and feature issue templates.

## Local Backend Demo

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Then call:

```bash
curl -X POST http://localhost:8000/api/v1/jobs/scrape
curl http://localhost:8000/api/v1/tenders
curl -X POST http://localhost:8000/api/v1/tenders/1/score
curl -X POST http://localhost:8000/api/v1/tenders/1/analyze
```

## Local Frontend Demo

```bash
cd apps/web
npm install
npm run dev
```

Open `http://localhost:3000`.

## Roadmap

1. Replace demo scraper adapters with guarded Playwright portal implementations.
2. Add Celery and Redis for scheduled scraping and long-running AI jobs.
3. Add Supabase authentication and row-level security.
4. Integrate Gemini 2.5 Flash through LangGraph nodes.
5. Add Recharts analytics and real-time job updates.
6. Add E2E tests and production monitoring dashboards.
