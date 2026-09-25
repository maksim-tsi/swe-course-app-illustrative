# Repository guidance for coding agents

This is an instructor-operated teaching example. Read `README.md`, `docs/requirements.md`, the current `docs/stages/W*.md`, `docs/architecture.md`, `docs/specification-plan.md`, `docs/test-plan.md`, and `docs/acceptance-plan.md` before changing a stage. The user request and current stage define scope; future-stage tasks are context, not permission to implement them now.

## Product invariants

- One active booking uses exactly one groomer and one room for its whole service interval. Neither resource can overlap another active booking. Three groomers, two rooms, four fixed-duration services; all groomers may perform all services in this teaching model.
- Validate inputs and availability before changing stored state. Rejected or repeated cancellation must not free capacity twice. Rescheduling must not lose the original booking on failure.
- Use synthetic customer and pet identifiers. Do not commit secrets, real customer data, model transcripts containing private data, local databases, or deployment credentials.
- Treat the selected stack as a small modular monolith: Python/FastAPI, SQLite, plain HTML/JavaScript. W1 records the architectural decision in `docs/adr/`; a later change requires an explicit decision and verified migration.

## Git isolation and review workflow

The active `Protect Main` ruleset requires a PR for changes to `main`. Before any edit, verify the repository and current status, fetch `origin/main`, and start a descriptive `feature/<task>` branch from that ref in a **new isolated Git worktree**. Every agent session, including reviewers, works in its own worktree. Do not let multiple agents edit one worktree or use the primary `main` checkout as a scratchpad. Preserve unrelated changes and history; never reset or force-push to make a branch fit.

When an agent changes files, commit only the bounded task, push its feature branch, and open a PR with base `main`. A read-only reviewer reports findings on the existing PR and does not create an empty PR. Leave the PR open for instructor review; an AI reviewer is advisory and may not merge or treat its own approval as human acceptance. If another agent needs the change, hand off the commit/branch/PR rather than uncommitted files in a shared tree. Rebase or merge an updated `main` only after inspecting conflicts and without discarding work.

### PR title and description standard

Use a concise outcome title, prefixed by the stage when relevant, such as `W2: Add conflict-safe booking` or `Docs: Clarify W1 contract`. Describe the **actual change**, not the agent session. Every PR description includes:

1. **Purpose and scope:** the problem, current stage/requirement IDs or linked issue/ADR, and the bounded result. State what the PR changes; mention exclusions only when they explain a review boundary.
2. **Changes:** the important files or behaviours and the design choice that a reviewer must understand.
3. **Verification:** exact commands and observed outcomes, including failing or unrun checks with reasons. Distinguish expected behaviour from executed evidence and name the tested revision when results were captured.
4. **Review and risk:** the specific question for the instructor, known limits, data/migration or deployment effect, and rollback/restore implications when applicable. Use `None identified` only after checking, not as a substitute for review.

Use the [repository PR template](.github/pull_request_template.md); remove irrelevant prompts rather than inventing results. Link evidence already in the repository or issue/PR; do not paste secrets, real customer data, full model transcripts or large duplicate logs. A passing check is bounded evidence, not a claim of defect freedom.

## Work and evidence

- Limit a stage to its task and 8 instructor engineering hours. Do not implement later stages early to satisfy a prompt. Update the relevant requirement/specification/test/acceptance trace when behaviour changes.
- State commands actually run and observed outcomes. Planned tests, passing CI, AI agreement, and agent review do not prove defect freedom or replace instructor judgment.
- Before proposing acceptance, inspect the diff, run the checks available at that stage, record limitations, and identify the exact revision. An AI reviewer is advisory; the instructor makes the human decision.
- Never autonomously publish the application, expose a write endpoint to the internet, alter repository visibility, or put secrets in Git. W5/W6 operational actions require the instructor's explicit execution decision.

Reusable workflows live in `.agents/skills/`; role briefs live in `.agents/roles/`. Tool-specific agent adapters may point to those briefs. `gh` is a GitHub CLI, not an AI agent harness. Prefer ordinary project commands for required checks, with a manual fallback when an AI tool is unavailable.
