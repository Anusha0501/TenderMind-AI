# TenderMind-AI API

## Run Locally

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Demo Flow

1. `POST /api/v1/jobs/scrape` seeds normalized demo tenders through scraper adapters.
2. `GET /api/v1/tenders` lists discovered tenders.
3. `POST /api/v1/tenders/{id}/score` calculates explainable opportunity fit.
4. `POST /api/v1/tenders/{id}/analyze` creates an eligibility report.
