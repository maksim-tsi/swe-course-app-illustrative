# Specification plan

**Status:** plan for progressive specification, not a completed design or implementation. Requirements IDs in [user requirements](requirements.md) are authoritative for desired behaviour; an ADR records selected design choices.

| Stage | Specification to resolve before or during the stage | Artifact/evidence to add |
|---|---|---|
| W1 | Booking identity and cancellation contract; resource interval convention; modular-monolith decision and one alternative | Proposed [ADR-001](adr/0001-application-boundary.md), pure contract in `app/grooming/`, and ordinary unit checks; instructor decision pending |
| W2 | Four service durations, opening grid, allocation order, request/response and error states, persisted booking/cancel path, client states and setup | API and state contract; sample synthetic inputs; configuration example |
| W3 | Acceptance examples, boundary partitions and release criteria | Versioned criteria linked to actual checks and feedback |
| W4 | Atomic reschedule rule, state invariants, old-record compatibility | Reschedule contract and migration/compatibility note |
| W5 | Ownership proof/trust boundary, release identity, backup/restore and rollback assumptions | Threat/acceptance notes and bounded runbook |
| W6 | Maintenance request and backward behaviour, publication target, handover and retirement condition | Change note, updated runbook and published revision |

## Contract questions to settle explicitly

W1 specifies the in-memory cancellation result order, integer-minute timeline and half-open intervals in proposed ADR-001. It proposes an ascending resource-pair order for W2. These decisions do not establish a persisted or networked path.

- W2: How are local studio times represented and converted, and how is availability rechecked at commit time?
- W2: What result follows an unknown reference or an uncertain network response, and how is owner proof represented at the HTTP boundary?
- W4: What exact state is preserved when a reschedule fails, and how is old data read?
- W5: What data version is restorable, and what is the limited security claim for the synthetic ownership proof?

Do not turn a proposed answer here into a claim of implementation. Add concrete API schemas and data examples when W2 creates them.
