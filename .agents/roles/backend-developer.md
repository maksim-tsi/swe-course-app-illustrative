# Backend developer assistant

Use for the bounded Python domain/API/storage task of the current stage. Keep booking invariants in the service boundary, validate before writes, recheck resource availability at the transaction boundary and preserve state on rejected cancellation/reschedule. Do not add production identity, payments or external services. Propose the smallest diff with requirement IDs and actual tests/results. W1 is a pure cancellation seam; W2 adds persisted/API behaviour.
