# Specification plan

**Status:** plan for progressive specification, not a completed design or implementation. Requirements IDs in [user requirements](requirements.md) are authoritative for desired behaviour; an ADR records selected design choices.

| Stage | Specification to resolve before or during the stage | Artifact/evidence to add |
|---|---|---|
| W1 | Booking identity and cancellation contract; resource interval convention; modular-monolith decision and one alternative | ADR-001 (TODO), narrow contract and initial module boundaries |
| W2 | Four service durations, opening grid, allocation order, request/response and error states, persisted booking/cancel path, client states and setup | API and state contract; sample synthetic inputs; configuration example |
| W3 | Acceptance examples, boundary partitions and release criteria | Versioned criteria linked to actual checks and feedback |
| W4 | Atomic reschedule rule, state invariants, old-record compatibility | Reschedule contract and migration/compatibility note |
| W5 | Ownership proof/trust boundary, release identity, backup/restore and rollback assumptions | Threat/acceptance notes and bounded runbook |
| W6 | Maintenance request and backward behaviour, publication target, handover and retirement condition | Change note, updated runbook and published revision |

## Contract questions to settle explicitly

- Is an interval half-open `[start, end)`? How are local studio times represented and converted?
- How is a groomer-room pair selected when several are free, and how is availability rechecked at commit time?
- What result follows an already-cancelled booking, a repeated request, an unknown reference, or an uncertain network response?
- What identifies the owner for change requests, and what is the limited security claim for this synthetic demonstration?
- What exact state is preserved when a reschedule fails? What data version is restorable?

Do not turn a proposed answer here into a claim of implementation. Add concrete API schemas and data examples when W2 creates them.
