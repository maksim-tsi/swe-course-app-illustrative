# Grooming Studio — Software Engineering II teaching example

Grooming Studio is the instructor-operated example for the Software Engineering II course at TSI. Across six workshops, we will develop a small appointment-booking application for a dog grooming studio and use its history to examine requirements, architecture decisions, implementation, testing, review, release, and maintenance. Students can inspect the decisions and evidence here, then apply the methods to **their own Part I projects**. This repository is not a student assignment or a required contribution destination.

> **Current state (26 September 2026): W1 candidate under review.** The repository contains requirements, plans, stage briefs, agent guidance, a proposed ADR and a pure in-memory cancellation seam with ordinary unit checks. It does not yet contain a runnable application, accepted ADR, completed workshop result or deployed service. The W1 pull request records observed check results; the instructor's decision remains pending. Planned later-stage checks below are not executed results.

## The application we will build

A dog owner selects a grooming service and a start time, sees available appointments, and requests a booking. The application should give an unambiguous result and a booking reference. Later stages add cancellation and rescheduling. The teaching studio has **three groomers, two interchangeable rooms, and four fixed-duration services**:

| Service | Proposed duration |
|---|---:|
| Bath | 30 minutes |
| Basic Groom | 60 minutes |
| Full Groom | 90 minutes |
| Puppy Introduction | 30 minutes |

All groomers can perform every service in this simplified model. One active booking uses one groomer and one room for its entire interval. A booking must not overlap another active booking for either assigned resource. The initial requirements also call for understandable pending, success, validation, conflict, and unavailable states; a safe response to uncertain outcomes; and reproducible startup. These are [requirements](docs/requirements.md), not claims about the current implementation.

The proposed architecture is a **small modular monolith**: Python and FastAPI for the HTTP API, SQLite for local persistence, and plain HTML/JavaScript for the browser client. A booking service will own domain rules while a repository module will own durable reads and writes. This choice keeps the allocation and cancellation rules visible within the course's time budget. Its trade-offs are described in the [architecture note](docs/architecture.md) and proposed W1 [Architecture Decision Record (ADR)](docs/adr/0001-application-boundary.md). No ADR has been accepted yet.

## Six workshop stages

Each stage has a budget of **at most eight instructor engineering hours**, including implementation, checks, review, and documentation. A class workshop demonstrates a bounded part of that work in about 40 minutes. Each stage should leave a named revision, observed check results, known limits, and an instructor decision before the next stage builds on it.

| Stage | Planned increment | What the demonstration examines |
|---|---|---|
| [W1 — Initiation](docs/stages/W1-initiation.md) | First ADR, cancellation contract, and application skeleton | Scope, architectural rationale, a small agent-assisted change, and human review |
| [W2 — Usable slice](docs/stages/W2-usable-slice.md) | Browser-to-SQLite booking path and reproducible startup | Client states, resource conflicts, unavailable dependencies, safe retry, and clean setup |
| [W3 — Tests and early release](docs/stages/W3-test-and-early-release.md) | Stronger test oracles and an early version | Boundary cases, structural checks, test sensitivity, and feedback |
| [W4 — Feedback and rescheduling](docs/stages/W4-feedback-reschedule.md) | One feedback-driven reschedule operation | State invariants, real-store integration, and compatibility with earlier data |
| [W5 — Operational rehearsal](docs/stages/W5-operational-release.md) | Trust-boundary checks and an isolated release | Allowed and denied actions, rollback, and data restore |
| [W6 — Maintenance and publication](docs/stages/W6-maintenance-publication.md) | Checked maintenance change and handover | Regression, operating instructions, and a course-accessible release subject to an instructor decision |

The [stage index](docs/stages/README.md) maps workshops to lectures and suggests optional demonstration tools. GitHub CLI illustrates issue and PR evidence; it is not an AI agent harness. OpenCode, Codex, Antigravity, or another available assistant may help the instructor propose bounded changes. **No particular AI tool, account, subscription, VM, or provider is required for student homework.** Ordinary project commands and manual review remain valid routes.

## Start reading or following the demonstration

```sh
git clone https://github.com/maksim-tsi/swe-course-app-illustrative.git
cd swe-course-app-illustrative
```

1. Read this README. At W1, the only executable check is `python3 -m unittest discover -s tests -v`; there is no application install or run command yet.
2. Read the [user requirements](docs/requirements.md) and [architecture proposal](docs/architecture.md) to understand the product boundaries.
3. Review the [specification](docs/specification-plan.md), [test](docs/test-plan.md), and [acceptance](docs/acceptance-plan.md) plans. They describe the intended six-stage coverage and distinguish planned checks from observed results.
4. Open the [current stage brief](docs/stages/README.md) and follow the resulting commits and PRs. Check the actual revision and evidence before treating a feature as complete.
5. If you use a coding agent, read [AGENTS.md](AGENTS.md), the portable [role briefs](.agents/roles/README.md), and [skills](.agents/skills/README.md). AI output is a proposal for instructor review, not a substitute for it.

The [documentation index](docs/README.md) explains the purpose of each document. The `app/` and `tests/` directories contain W1's pure cancellation code and checks; later stages will extend them. Optional VM, OpenCode, and model setup can illustrate an instructor environment, but they are not needed to read or assess the repository.

## Evidence, safety, and scope

- Use synthetic owners, pets, and appointments. Do not commit real customer data, credentials, local databases, deployment secrets, or private model transcripts.
- Keep the example small: no payments, notifications, customer accounts, specialist groomer qualifications, multi-branch scheduling, or production-grade availability promise. The planned booking reference and ownership proof do not claim production identity management.
- Record exact revisions, commands actually run, results, limitations, and the instructor's accept/revise/reject decision. A passing test or CI job gives bounded evidence; it cannot prove the absence of defects.
- A public source repository does not make the application a public running service. W5 rehearses recovery in isolation. W6 publication requires a separate instructor operational decision.
- The instructor performs the illustrative work. Student teams extend their own existing projects under the course assignments; this repository is a reference example, not a shared submission repository.

## Contributing to this example

Instructor practice and demonstration changes use `dev-max` as the integration branch; `main` remains stable under the active [Protect Main ruleset](https://github.com/maksim-tsi/swe-course-app-illustrative/rules/24012631). Every agent or contributor makes a bounded change in an **isolated Git worktree** on a descriptive `feature/<task>` branch from current `origin/dev-max`. Do not edit the primary checkout, push directly to `dev-max` or `main`, force-push, or share one worktree between concurrent agents. Commit and push the feature branch, then open a PR **to `dev-max`** for instructor review. [AGENTS.md](AGENTS.md) defines the required PR description; the [PR template](.github/pull_request_template.md) provides its headings. The instructor reviews and merges accepted changes. Students may clone this example for reference while completing assignments in their own repositories.

Preserve earlier stage history and describe the state that was actually observed. A workshop's timebox does not turn an unfinished acceptance criterion into a pass; see the [acceptance plan](docs/acceptance-plan.md) for the evidence expected at each handoff.
