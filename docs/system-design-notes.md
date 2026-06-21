# System Design Notes

TenderMind-AI uses a modular monolith for the API plus background worker boundaries. The design favors explicit state, auditable AI decisions, and deterministic filtering before LLM usage. This keeps free-tier costs controlled and makes the system easier to explain in interviews.

## Production Safety Principles

- Filter first, call LLM second.
- Store evidence for every extracted requirement.
- Keep human approval before submission.
- Make scraping and agent jobs idempotent.
- Trace agent runs for debugging and evaluation.
