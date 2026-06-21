# API Design

## What We Are Building

The API exposes tender monitoring, scoring, eligibility reports, human review, notifications, and settings to the frontend. FastAPI will later generate OpenAPI docs from typed route and schema definitions.

## API Principles

- Use resource-oriented URLs.
- Return typed JSON responses.
- Keep long-running work asynchronous.
- Make mutations explicit.
- Include explainability fields for AI-assisted decisions.
- Never expose secrets or raw credentials.

## Endpoint Overview

### Health

| Method | Path | Purpose |
|---|---|---|
| GET | /health | Check service health |

### Company Profile

| Method | Path | Purpose |
|---|---|---|
| GET | /api/v1/company-profile | Fetch current company profile |
| PUT | /api/v1/company-profile | Create or update company profile |

### Tender Sources

| Method | Path | Purpose |
|---|---|---|
| GET | /api/v1/sources | List supported tender sources |
| PATCH | /api/v1/sources/{source_id} | Enable or disable a source |

### Tenders

| Method | Path | Purpose |
|---|---|---|
| GET | /api/v1/tenders | List tenders with search and filters |
| GET | /api/v1/tenders/{tender_id} | Fetch tender details |
| POST | /api/v1/tenders/{tender_id}/score | Recalculate opportunity score |
| POST | /api/v1/tenders/{tender_id}/analyze | Queue eligibility analysis |

### Eligibility Reports

| Method | Path | Purpose |
|---|---|---|
| GET | /api/v1/reports | List eligibility reports |
| GET | /api/v1/reports/{report_id} | Fetch report details |
| POST | /api/v1/reports/{report_id}/review | Submit human review decision |

### Notifications

| Method | Path | Purpose |
|---|---|---|
| GET | /api/v1/notifications | List notifications |
| POST | /api/v1/notifications/{notification_id}/read | Mark notification as read |

### Jobs

| Method | Path | Purpose |
|---|---|---|
| POST | /api/v1/jobs/scrape | Queue a scraping run |
| GET | /api/v1/jobs/{job_id} | Fetch job status |

## Example Tender List Query

```http
GET /api/v1/tenders?source=GeM&status=open&min_score=70&search=software&page=1&page_size=20
```

## Example Tender Response Shape

```json
{
  "id": "uuid",
  "title": "Supply and implementation of software platform",
  "source": "GeM",
  "buyer_name": "Example Department",
  "location": "Delhi",
  "estimated_value": 2500000,
  "published_at": "2026-06-21T00:00:00Z",
  "closes_at": "2026-07-05T00:00:00Z",
  "status": "open",
  "opportunity_score": {
    "total_score": 82,
    "reasons": [
      "Strong industry match",
      "Project value fits preferred range",
      "Deadline allows enough preparation time"
    ]
  }
}
```

## Example Eligibility Report Shape

```json
{
  "id": "uuid",
  "tender_id": "uuid",
  "status": "needs_review",
  "readiness_score": 74,
  "executive_summary": "The opportunity is relevant, but certification evidence needs review.",
  "requirements": [
    {
      "type": "turnover",
      "description": "Average annual turnover must be at least INR 1 crore.",
      "decision": "pass",
      "confidence": 0.91,
      "evidence": "Tender document states minimum turnover requirement...",
      "source_reference": "eligibility.pdf page 4"
    }
  ],
  "risks": ["Certification requirement needs manual confirmation"],
  "recommended_next_steps": ["Upload ISO certificate evidence"]
}
```

## Why Async Job Endpoints Exist

Scraping and eligibility analysis may take seconds or minutes. The API should return quickly with a job ID while Celery processes the task in the background.

## Alternatives and Tradeoffs

### REST API

- Pros: beginner-friendly, easy to document, works well with FastAPI.
- Cons: multiple requests may be needed for complex screens.

### GraphQL

- Pros: flexible frontend data fetching.
- Cons: more complexity and less necessary for early phases.

### WebSockets for Everything

- Pros: real-time updates.
- Cons: unnecessary complexity for CRUD workflows.

TenderMind-AI starts with REST and can add WebSockets or Server-Sent Events later for real-time job updates.

## Best Practices

- Use pagination for lists.
- Validate all inputs with Pydantic.
- Return stable error formats.
- Use idempotency keys for job-triggering endpoints later.
- Avoid returning raw LLM prompts or secrets.
- Include correlation IDs in logs and responses for debugging.
