# Repository guidance for coding agents

This is an instructor-operated teaching example. Read `README.md`, `docs/requirements.md`, the current `docs/stages/W*.md`, `docs/architecture.md`, `docs/specification-plan.md`, `docs/test-plan.md`, and `docs/acceptance-plan.md` before changing a stage. The user request and current stage define scope; future-stage tasks are context, not permission to implement them now.

## Product invariants

- One active booking uses exactly one groomer and one room for its whole service interval. Neither resource can overlap another active booking. Three groomers, two rooms, four fixed-duration services; all groomers may perform all services in this teaching model.
- Validate inputs and availability before changing stored state. Rejected or repeated cancellation must not free capacity twice. Rescheduling must not lose the original booking on failure.
- Use synthetic customer and pet identifiers. Do not commit secrets, real customer data, model transcripts containing private data, local databases, or deployment credentials.
- Treat the selected stack as a small modular monolith: Python/FastAPI, SQLite, plain HTML/JavaScript. W1 records the architectural decision in `docs/adr/`; a later change requires an explicit decision and verified migration.

## Work and evidence

- Limit a stage to its task and 8 instructor engineering hours. Do not implement later stages early to satisfy a prompt. Update the relevant requirement/specification/test/acceptance trace when behaviour changes.
- State commands actually run and observed outcomes. Planned tests, passing CI, AI agreement, and agent review do not prove defect freedom or replace instructor judgment.
- Before proposing acceptance, inspect the diff, run the checks available at that stage, record limitations, and identify the exact revision. An AI reviewer is advisory; the instructor makes the human decision.
- Never autonomously publish the application, expose a write endpoint to the internet, alter repository visibility, or put secrets in Git. W5/W6 operational actions require the instructor's explicit execution decision.

Reusable workflows live in `.agents/skills/`; role briefs live in `.agents/roles/`. Tool-specific agent adapters may point to those briefs. `gh` is a GitHub CLI, not an AI agent harness. Prefer ordinary project commands for required checks, with a manual fallback when an AI tool is unavailable.
