# Proposed architecture for the teaching application

**Status:** proposal to be evaluated in W1 ADR, not an accepted implementation decision.

A **small modular monolith** is the best fit for this bounded example: one FastAPI process serves plain HTML/JavaScript and a narrow HTTP API; a domain module owns booking rules; a repository module owns SQLite access. The 3-groomer/2-room allocation is one transactional decision. Keeping it in one process and one database makes resource conflicts, state changes, and release recovery observable without adding distributed-service coordination to a six-stage, eight-hour-per-stage exercise.

Proposed dependency direction: `web client → HTTP handlers → booking service → SQLite repository`. Handlers parse/return data; the service validates intervals, cancellation, ownership and rescheduling; the repository performs durable reads/writes in transactions. Tests can exercise rules directly and the real storage boundary separately. The W1 cancellation exercise may begin as a pure function before the W2 persistent path exists.

Trade-offs to record in the W1 ADR: simple deployment and deterministic local checks versus limited concurrency and no independent service scaling; SQLite's suitability for a small teaching instance versus the need to verify write serialization and restore; plain JavaScript's low setup cost versus limited UI structure. Do not claim this is a universal architecture for a commercial grooming platform.

See [ADR guidance](adr/README.md). No ADR has been accepted yet.
