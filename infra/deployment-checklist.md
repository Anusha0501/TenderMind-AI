# Deployment Checklist

## Backend on Railway
1. Create Railway service from the repository.
2. Set root directory to `apps/api`.
3. Configure `DATABASE_URL`, `GEMINI_API_KEY`, and `LANGSMITH_API_KEY`.
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`.
5. Verify `/health` returns `{"status":"ok"}`.

## Frontend on Vercel
1. Create Vercel project from the repository.
2. Set root directory to `apps/web`.
3. Configure `NEXT_PUBLIC_API_URL` with the Railway backend URL.
4. Deploy and verify dashboard pages render.

## Database on Supabase
1. Create a free Supabase project.
2. Copy the PostgreSQL connection string into Railway as `DATABASE_URL`.
3. Enable backups before production use.

## Redis on Upstash
1. Create a free Redis database.
2. Store the Redis URL for the future Celery worker phase.
