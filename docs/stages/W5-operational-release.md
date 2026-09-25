# W5 — Review an operational release and recovery

**Lectures:** L13–L15. **Engineering budget:** at most 8 instructor hours. **Input:** W4 integration-tested candidate. **Tool illustration:** reuse an agent for a read-only runbook critique and `gh` for release evidence; the instructor performs all operational steps.

## Instructor task

1. State the trust boundary for changing or cancelling a synthetic booking. Demonstrate an allowed owner action and a denied or malformed request. Do not portray a teaching ownership token as commercial-grade authentication.
2. Identify the candidate revision, configuration, dependency versions, basic health observation and one bounded acceptance path. Produce a versioned release artifact and an isolated test deployment using synthetic data.
3. Write a short runbook and then execute two separate checks in isolation: roll the application code back to a compatible version; restore synthetic records into a fresh store. Verify version identity, expected records and feature behaviour, not only file existence.
4. Record observed results, failed checks and limits. Keep secrets and local database files out of Git. The plan does not authorize an internet-facing write service.

## Done when

There is a reviewable release/recovery packet with actual evidence and a specific instructor readiness decision. The result is an isolated teaching drill, not production resilience certification. See [W6](W6-maintenance-publication.md).
