---
name: test-design
description: Use when deriving or evaluating requirement-based functional, structural, state, or integration tests for a grooming-studio workshop stage.
---

# Test design

Read `docs/requirements.md`, `docs/test-plan.md`, and the current stage. Select a few risks that stage can actually observe. Derive expected outcomes from requirements before reading implementation behaviour. Use representative equivalence and boundary cases, including full two-room occupancy, service interval edges, repeated cancellation, and failed reschedule when in scope. State which layer each check exercises: pure rule, HTTP/client, disposable SQLite, or release/restore.

Run only checks available at the current stage. Report command, fixture, exact result and remaining blind spots. A branch count, mutation result, no-counterexample run or passing CI bounds a claim; it does not establish general correctness. Keep controlled faults in disposable code/data and remove them before release. Suggest the smallest next test that would change the instructor's decision.
