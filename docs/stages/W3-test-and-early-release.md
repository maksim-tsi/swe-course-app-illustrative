# W3 — Challenge tests and make an early release decision

**Lectures:** L7–L9. **Engineering budget:** at most 8 instructor hours. **Input:** W2 usable revision. **Suggested harness illustration:** Codex; required verification stays in ordinary tests/commands.

## Instructor task

1. Derive equivalence and boundary cases from the actual requirements and contracts: invalid start, opening edge, 30/60/90-minute service boundary, full two-room occupancy, cancellation repetition and unauthorized attempt. Specify expected outcomes before asking an agent for test additions.
2. Inspect relevant branches and run a controlled mutation or equivalent sensitivity experiment in disposable code. Record whether the check detects it; no surviving mutation is required.
3. Keep useful regression checks, run the suite and review the diff. Mark one stable early version (tag or release marker) only after recording the actual checked SHA and limits.
4. Capture one synthetic user/proxy feedback item that can motivate W4, without changing requirements retrospectively to make existing tests pass.

## Done when

The test plan links requirements to actual commands/results, the early version is identifiable, and feedback has a bounded next change. Coverage or passing CI is not a claim of defect freedom. See [W4](W4-feedback-reschedule.md).
