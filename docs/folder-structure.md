# Folder Structure

## What We Are Building

This document defines the planned repository layout before implementation begins. The structure is designed for a beginner-friendly but production-oriented monorepo.

## Planned Structure

```text
TenderMind-AI/
├── apps/
│   ├── api/                    # FastAPI backend
│   │   ├── app/
│   │   │   ├── api/            # Route handlers and API dependencies
│   │   │   ├── agents/         # LangGraph workflows
│   │   │   ├── core/           # Settings, logging, security, app config
│   │   │   ├── db/             # Database session and migrations
│   │   │   ├── models/         # SQLModel database models
│   │   │   ├── schemas/        # Pydantic request/response schemas
│   │   │   ├── scrapers/       # Playwright scraper adapters
│   │   │   ├── services/       # Business logic
│   │   │   ├── tasks/          # Celery jobs
│   │   │   └── tests/          # Backend tests
│   │   ├── pyproject.toml
│   │   └── alembic.ini
│   └── web/                    # Next.js frontend
│       ├── app/                # App Router pages and layouts
│       ├── components/         # Reusable UI components
│       ├── features/           # Feature-specific UI modules
│       ├── lib/                # API clients and utilities
│       ├── public/             # Static assets
│       └── package.json
├── docs/
│   ├── api/                    # API design documents
│   ├── architecture/           # System and agent diagrams
│   ├── database/               # Schema design
│   └── product/                # PRD and product notes
├── infra/                      # Deployment and infrastructure notes
├── .github/
│   ├── ISSUE_TEMPLATE/         # GitHub issue templates
│   └── pull_request_template.md
├── README.md
└── CONTRIBUTING.md
```

## Why This Structure Exists

### apps/api

The backend is isolated from the frontend so Python dependencies, tests, and deployment configuration stay clean.

### apps/web

The frontend is isolated so TypeScript, Tailwind, shadcn/ui, Recharts, and Framer Motion can evolve without mixing with backend code.

### docs

The project is educational. Documentation is treated as a first-class artifact so each design decision can be explained and defended in interviews.

### infra

Deployment configuration should not be scattered across application code. Railway, Vercel, Supabase, and Upstash notes can live here.

### .github

Professional projects include PR templates, issue templates, and contribution guidelines.

## Alternative Structures

### Single Backend Repository

- Pros: simple if there is no frontend.
- Cons: not enough for a SaaS dashboard product.

### Separate Frontend and Backend Repositories

- Pros: independent deployment and permissions.
- Cons: harder for a beginner to coordinate changes and documentation.

### Monorepo

- Pros: one place for full-stack work, shared documentation, easier learning path.
- Cons: needs discipline to keep boundaries clean.

TenderMind-AI uses a monorepo because it is best for learning and full-stack product development.

## Best Practices

- Keep route handlers thin and place business logic in services.
- Keep scraper code portal-specific and reusable.
- Keep LangGraph state definitions close to agent workflows.
- Avoid importing frontend code into backend code or vice versa.
- Write tests near the code they verify.
- Document every major architectural choice.
