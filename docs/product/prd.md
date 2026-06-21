# TenderMind-AI Product Requirements Document

## 1. Product Vision

TenderMind-AI is an autonomous government tender monitoring and qualification platform. It helps small and mid-sized businesses discover relevant public procurement opportunities, understand requirements, assess eligibility, and prepare bid-readiness reports while keeping humans in control before any submission action.

The product is intentionally designed as a **human-in-the-loop AI system**. The AI can monitor, extract, summarize, score, and recommend, but a user must review and approve important decisions.

## 2. Problem Statement

Government tender portals contain valuable business opportunities, but they are difficult to monitor manually because:

- Opportunities are spread across multiple portals.
- Tender documents can be long, inconsistent, and legalistic.
- Eligibility criteria are easy to miss.
- Companies waste time reading tenders they cannot realistically win.
- Bid teams need structured summaries, not raw PDFs and portal pages.

## 3. Target Users

### Primary Users

- Business development teams at SMEs.
- Tender / proposal managers.
- Founders who sell to government departments.
- Consultants who monitor tenders for multiple clients.

### Secondary Users

- Compliance officers.
- Sales operations teams.
- Leadership teams reviewing bid pipelines.

## 4. Goals

TenderMind-AI should:

1. Monitor GeM and CPPP tender portals.
2. Extract new tender metadata and documents.
3. Score opportunities against company preferences.
4. Extract eligibility and technical requirements from tender documents.
5. Compare requirements with a company profile.
6. Generate bid-readiness reports.
7. Notify users about relevant opportunities.
8. Require human approval before any submission-related action.

## 5. Non-Goals for Phase 1

Phase 1 does **not** implement scraping, agents, UI, authentication, deployment, or submission automation. It creates the product and engineering blueprint that later phases will implement step by step.

Submission automation is intentionally out of scope for the initial product because government procurement workflows are high-risk and require human judgment.

## 6. Core User Journey

1. User configures company profile, industry categories, locations, certifications, turnover, and opportunity preferences.
2. System periodically checks tender portals.
3. New tenders are stored and deduplicated.
4. Opportunity filter assigns a relevance score.
5. High-scoring tenders are sent to the eligibility agent workflow.
6. Agent extracts requirements from tender pages and documents.
7. System compares requirements against the company profile.
8. User reviews a bid-readiness report.
9. User approves, rejects, or requests manual review.

## 7. Functional Requirements

### Tender Monitoring

- Monitor GeM and CPPP portals.
- Store tender title, portal source, tender reference number, buyer, location, dates, value, category, links, and document references.
- Detect duplicates across repeated scraping runs.

### Opportunity Filtering

- Score tenders using industry match, project size, location fit, and deadline timing.
- Store score breakdowns for explainability.
- Allow users to tune scoring preferences later.

### Eligibility Analysis

- Parse tender documents and portal text.
- Extract turnover, certification, experience, financial, legal, and technical criteria.
- Compare criteria against company profile.
- Mark each criterion as pass, fail, unknown, or needs human review.

### Human Review

- Create review tasks when confidence is low or requirements are ambiguous.
- Prevent automatic submission.
- Preserve review notes and decisions for auditability.

### Reporting

- Generate bid-readiness reports with:
  - executive summary,
  - opportunity score,
  - eligibility checklist,
  - missing documents,
  - risks,
  - recommended next steps.

### Notifications

- Notify users about high-scoring tenders and completed eligibility reports.
- Start with email or dashboard notifications; later phases can add Slack or WhatsApp.

## 8. Non-Functional Requirements

### Reliability

Scraping and AI workflows must be retryable and idempotent because portal pages, network calls, and LLM APIs can fail.

### Explainability

Every score and eligibility decision should include reasons. This is critical because users must trust the recommendation before spending time or money on a bid.

### Security

Company profiles may include sensitive business information. Store secrets in environment variables and avoid logging credentials or private tender documents.

### Observability

Use structured logs and tracing to understand failures across scraping, background jobs, and agent runs.

### Cost Control

Use free-tier-friendly architecture. Avoid unnecessary LLM calls by filtering low-relevance tenders before document analysis.

## 9. Success Metrics

- Number of tenders discovered per day.
- Percentage of duplicate tenders avoided.
- Time saved per tender review.
- Percentage of agent extractions accepted by humans.
- Number of relevant opportunities surfaced.
- False positive and false negative rates for eligibility checks.

## 10. Key Product Decisions

### Decision: Filter Before Running the AI Agent

Running LLM analysis on every tender would be expensive and slow. A deterministic scoring engine first narrows the set of opportunities. The AI agent then analyzes only promising tenders.

### Decision: Human Approval Before Submission

Tender submission is legally and commercially sensitive. The system assists with readiness, but humans remain accountable for final actions.

### Decision: Start with GeM and CPPP

These portals are high-value starting points for Indian government procurement. The architecture still supports adding more portals later through a scraper adapter pattern.

## 11. Alternative Approaches and Tradeoffs

### Fully Manual Monitoring

- Pros: simple, no automation risk.
- Cons: slow, inconsistent, hard to scale.

### Fully Autonomous Bidding

- Pros: maximum automation.
- Cons: high legal, financial, and trust risk; not suitable for a beginner production system.

### LLM-Only Filtering

- Pros: flexible reasoning.
- Cons: higher cost, lower repeatability, harder to debug.

### Rules-First Then Agentic Analysis

- Pros: cheaper, explainable, production-friendly.
- Cons: requires thoughtful scoring design and data modeling.

TenderMind-AI chooses the rules-first then agentic-analysis approach.
