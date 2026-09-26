# ADR-001 — Application boundary and W1 cancellation seam

**Date:** 26 September 2026

**Status:** Proposed — awaiting instructor decision

**Requirement:** UR-04; later allocation constraints support UR-01–UR-03

## Context and quality risk

Grooming Studio needs an understandable booking path and a cancellation rule that never releases capacity twice. The pre-W1 baseline is documentation only. The teaching scope has three groomers, two interchangeable rooms and four fixed-duration services. An early split into separately deployed components would make state changes and failure handling harder to inspect within the workshop budget.

## Proposed decision

Use a small modular monolith: a plain browser client calls narrow FastAPI handlers; domain services own booking rules; a SQLite repository owns durable transactions. Dependencies flow from client to handler to domain service to repository. W1 establishes only a pure, in-memory cancellation seam. W2 will decide the HTTP and storage representation and verify transaction behaviour; this ADR does not claim either exists now.

The W1 seam accepts a synthetic immutable booking with `id`, `owner_id`, integer `start_minute`, positive integer `duration_minutes`, `groomer_id` in 1–3, `room_id` in 1–2 and `status` of `active` or `cancelled`. `now_minute` is an integer on the same teaching timeline, with no date or time-zone conversion. Invalid booking/time values return `InvalidInput` before authorization or state checks. Missing actor returns `Unauthenticated`; another actor returns `Forbidden`. For the owner, an already cancelled booking returns `AlreadyCancelled`, an active booking at or after its start returns `TooLate`, and an active booking before its start returns `Cancelled` with only `status` changed. Every non-success outcome returns the original whole booking value.

For future allocation, represent occupied intervals as half-open `[start, start + duration)`. Adjacent intervals can meet at an endpoint without overlap. Among free groomer-room pairs, choose the first in ascending `(groomer_id, room_id)` order; W2 must recheck availability at the write boundary. One active booking occupies one groomer and one room for its entire interval. No global occupancy counter is part of the W1 seam.

## Considered alternative

Deploy booking and cancellation as separate services with independent storage. This could permit independent scaling, but introduces distributed coordination for a single resource decision, more failure modes and extra setup for the six-stage teaching example. The proposed monolith keeps the boundary visible while avoiding those costs. Keeping the application entirely in one unstructured handler is simpler initially, but would couple domain rules to transport and make direct contract checks harder.

## Consequences and evidence

The small structure supports direct domain checks and a later real SQLite boundary, but it does not itself prove concurrency safety, durable cancellation, production authentication or commercial scale. SQLite write serialization, recovery and deployment claims require later observed checks. W1 contract tests and the feature PR provide executable evidence; the instructor must review this proposal and record accept, revise or reject before treating it as an accepted architecture decision.
