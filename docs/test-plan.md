# Progressive test plan

**Status:** intended coverage, not executed results. The instructor updates results and limits per stage. This plan covers the full six-meeting teaching arc without requiring every topic to be an automated test. Link each implemented check to a requirement and a Git revision.

| Stage / lectures | Requirements and principal risk | Planned method and observable evidence |
|---|---|---|
| W1 / L1–L3 | UR-04; unclear contract, invalid/repeated cancellation, unchecked agent change | Contract examples and ordinary unit checks on a pure function; diff inspection; ADR rationale; actual command/result and instructor decision |
| W2 / L4–L6 | UR-01–UR-06; overlapping resources, ambiguous client failure, unsafe retry, non-reproducible setup | API/storage integration cases for 3 groomers, 2 rooms, 4 durations and conflicts; client pending/success/error and one keyboard/non-colour observation; dependency outage/retry; fresh startup and basic CI |
| W3 / L7–L9 | UR-07 plus earlier requirements; weak oracle, untested boundaries, false confidence from coverage | Equivalence and boundary cases from requirements; relevant branch review; bounded mutation/check experiment with actual outcome; tagged early release and feedback |
| W4 / L10–L12 | UR-08; invalid state sequence, failed reschedule loses booking, fake passes while storage fails | State transitions/invariants and bounded operation sequence; disposable real SQLite integration; old synthetic fixture compatibility; record found or not-found counterexample honestly |
| W5 / L13–L15 | UR-09; unauthorized change, unverified release, backup that cannot restore | Allowed/denied and malformed-input acceptance cases; version/config/health observation; isolated application rollback and separate fresh-store data restore with record/behaviour verification |
| W6 / L16–L18 | UR-10 and retained behaviour; patch regression, broken handover or retired endpoint | Characterization/regression for old behaviour; published-revision smoke check; replacement and old-test-target checks; retained data/history/runbook; one process-improvement observation |

## Cross-cutting trace

Architecture and Agile/PMO work is evidenced by ADRs, bounded issues, meaningful commits/PRs, review dispositions, feedback, releases and handover, not by a fictitious unit test for each process concept. AI output is reviewed as a proposal; all required checks use ordinary project tools. Test status must distinguish planned, executed-pass, executed-fail, blocked and not-applicable. A passing suite, CI or AI consensus does not prove absence of defects. No mutation, property, exploration or security failure discovery quota applies.

As each stage is implemented, append exact commands, environment/version, fixture ID, outcome, revision and known limit in a stage evidence note or linked PR. Do not pre-fill successful results.
