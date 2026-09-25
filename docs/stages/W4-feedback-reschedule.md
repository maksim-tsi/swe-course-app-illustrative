# W4 — Implement a stateful feedback change

**Lectures:** L10–L12. **Engineering budget:** at most 8 instructor hours. **Input:** W3 early release and documented feedback. **Suggested harness illustration:** Antigravity using the shared `AGENTS.md` and skills where supported.

## Instructor task

1. Turn one feedback item into a precise reschedule contract: an owned active booking may move to another available start without losing its original reservation if validation or allocation fails.
2. Model states and invariants: one active booking occupies one groomer and room; no interval overlap per resource; a failed move leaves the original state intact; retry has a defined result.
3. Implement the narrow change and run a bounded sequence/property check, then a real SQLite integration check against a disposable database. Reopen an old synthetic W2/W3 fixture and document compatibility or required migration.
4. Inspect the diff and actual results; record a counterexample if one appears, or the checked no-counterexample bound. Decide accept/revise/reject.

## Done when

One change requested after feedback works within observed checks; old data and real storage behaviour are considered. No new scheduling features or schema redesign are required without evidence. See [W5](W5-operational-release.md).
