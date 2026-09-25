# W2 — Deliver a usable booking slice

**Lectures:** L4–L6. **Engineering budget:** at most 8 instructor hours. **Input:** W1 contract and accepted baseline. **Tool illustration:** use `gh` for one issue/PR/review trail while an available agent proposes a bounded client or handler change; `gh` is not itself an agent harness.

## Instructor task

1. Add the four fixed-duration services, three groomers and two interchangeable rooms. Use a 30-minute start grid and the W1 ADR's interval convention. A successful booking occupies one groomer and one room for the entire service interval. Choose the lowest numbered free pair deterministically; recheck at the write boundary.
2. Add a small FastAPI path with SQLite storage and a plain HTML/JavaScript page to list services/available starts, submit a booking, show its reference and cancel it. Use synthetic identifiers and a bounded ownership proof; do not claim production identity management.
3. Show pending, success, validation/conflict and unavailable-dependency outcomes; retry only after checking stored state, without duplicate booking or release. Check one keyboard/non-colour status behaviour relevant to the page.
4. Record dependency versions, non-secret configuration and clean start/test commands. Add a basic ordinary CI check if feasible within the stage budget. Inspect the diff, demonstrate a real browser-to-state path, and record failures/limits.

## Done when

A user action reaches persisted state, three-groomer/two-room allocation and four service durations are represented, a blocked or repeated operation does not corrupt state in observed checks, and another clean environment can follow the startup instructions. The client need not be production accessible or mobile certified. Hand off a usable revision to [W3](W3-test-and-early-release.md).
