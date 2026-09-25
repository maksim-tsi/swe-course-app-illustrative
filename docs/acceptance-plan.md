# Six-stage acceptance plan

**Status:** criteria for instructor decisions; no stage has been accepted yet. Each workshop is an instructor-run demonstration. AI role output is advisory, and student discussion is formative. A human instructor records accept, revise, or reject against observed evidence.

| Stage | Minimum decision evidence | Handoff |
|---|---|---|
| W1 | Repository cloned/read; ADR created and reviewed against one alternative; narrow cancellation contract, skeleton and actual success/rejection/repetition checks; diff and revision inspected | Contract and baseline ready for persistent vertical slice |
| W2 | One real browser-to-state path; visible success/error/retry; no double allocation/release in checked cases; clean start using non-secret config; bounded accessibility observation | Usable checkpoint for systematic testing |
| W3 | Requirement-derived functional/structural/sensitivity evidence with honest limits; early version identity and one feedback item | Concrete change request for W4 |
| W4 | One feedback-driven reschedule; bounded invariant/sequence checks; real-store and old-fixture compatibility observations | Integration-tested candidate for operations |
| W5 | Allowed/denied action evidence; versioned isolated release; independently demonstrated application rollback and fresh-store data restore | Reviewed release and recovery packet |
| W6 | New maintenance patch with regression; handover instructions and retained history/data; old test target retired safely; accessible published revision smoke-checked | Course example lifecycle closed with one improvement note |

For every stage, record the actual SHA, commands/results, known limits, instructor disposition, and any unfinished criterion. A failed or blocked live demo is recorded truthfully and can lead to revise; the 40-minute class need not manufacture a pass. Publication is a separate operational action and is not authorized by this plan alone.
