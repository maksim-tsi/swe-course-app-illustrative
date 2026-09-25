# Grooming Studio — illustrative course application

This repository is the instructor-operated example for Software Engineering II. It will evolve across six 40-minute workshops. Students study the decisions and evidence here, then apply the methods to their own Part I projects. This repository is **not** a student assignment or a required AI-tool account.

**Baseline status:** planning package only. There is no runnable application, passing test suite, ADR, deployed service, or completed workshop result yet. The instructor will create the first ADR and application skeleton during W1. Do not describe planned checks as executed results.

## Product in one paragraph

A dog owner chooses one of four grooming services and a start time at a small studio. The application shows availability, makes a booking, and later supports cancellation and rescheduling. A booking occupies one of three groomers and one of two rooms for the entire service duration. Synthetic names and appointments keep the example safe to publish and reset. The proposed stack is Python, FastAPI, SQLite, and plain HTML/JavaScript; [the architecture note](docs/architecture.md) explains the bounded choice. The W1 ADR records the actual decision.

## Start here

1. Read the [user requirements](docs/requirements.md) and [architecture note](docs/architecture.md).
2. Read the [specification plan](docs/specification-plan.md), [test plan](docs/test-plan.md), and [acceptance plan](docs/acceptance-plan.md). These plans span all six stages; later evidence is still TODO.
3. Read the [six instructor demonstration tasks](docs/stages/README.md), starting with [W1](docs/stages/W1-initiation.md).
4. Read [AGENTS.md](AGENTS.md) before using any coding agent. [Agent roles](.agents/README.md) and [skills](.agents/skills/README.md) explain the portable parts of the AI workflow.

No install or run command is available at this baseline. `app/` and `tests/` contain README files that identify what W1 will create. The instructor may optionally create a VM, install OpenCode, and connect a model for W1. The essential route is to clone this repository, inspect the plans, make the W1 decision and bounded change, and verify what actually happened. Tool setup is not assessed and cannot consume the engineering scope of later stages.

## Delivery boundaries

- Six stages, each at most **8 instructor engineering hours**, including implementation, checks, review, and documentation. A workshop demonstrates a bounded slice of that work within roughly 40 minutes.
- The instructor operates the example. AI specialist profiles are assistants, not human team members or independent human reviewers. Students may discuss the evidence in class.
- H1–H6 in the course programme remain work in students' own repositories. No homework requires OpenCode, Codex, Antigravity, GitHub CLI, or comparison between them.
- Use synthetic data only. No payments, notifications, real customer accounts, personal pet records, multi-branch scheduling, or production-grade availability promise.
- A public source repository does not itself publish a running service. W5 rehearses an isolated release; W6 plans a course-accessible publication subject to a separate operational decision.

## Contribution and pull requests

The repository's active [Protect Main ruleset](https://github.com/maksim-tsi/swe-course-app-illustrative/rules/24012631) requires a pull request into `main`. Do not push changes directly to `main`, force-push it, or bypass the rule. Every agent working on this repository uses its **own isolated Git worktree** and a descriptive `feature/<task>` branch created from the current `origin/main`. Concurrent agents must not edit the same worktree; exchange changes through committed branches and PRs. Keep the primary `main` checkout clean.

Before editing, fetch `main`, inspect the working tree, and create a worktree for the bounded task. After editing, run the checks available at that stage, inspect the diff, commit and push the feature branch, then open a PR targeting `main`. Leave the PR open for instructor review and merge. Read [AGENTS.md](AGENTS.md) for the required PR description; GitHub offers the same structure in the [PR template](.github/pull_request_template.md). AI role output is advisory and does not count as human approval.

For example, from a clean primary clone, an agent can start W1 in a sibling worktree:

```sh
git fetch origin main
git worktree add -b feature/w1-cancellation ../swe-course-app-w1-cancellation origin/main
cd ../swe-course-app-w1-cancellation
git status --short --branch
```

Use a fresh branch name and directory for each independent task. Inspect the branch and base before a PR; do not reuse this example name if it already exists.

## Status and history

This initial commit is the **pre-W1 reading baseline**. Each workshop should leave a small traceable increment, actual check results, an instructor decision, and a stable Git revision or release marker when appropriate. Preserve history; do not rewrite an earlier stage to make the narrative look cleaner. See the [acceptance plan](docs/acceptance-plan.md).
