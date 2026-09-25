# W1 — Initiate the grooming-studio example

**Lectures:** L1–L3. **Engineering budget:** at most 8 instructor hours. **Starting point:** the pre-W1 reading baseline, not a working app. **Suggested agent harness:** OpenCode. VM creation, OpenCode installation and external-model connection are optional desirable demonstrations; the workshop must remain useful if they fail or are skipped.

## Instructor task

1. Clone this existing repository. Read its README, user requirements, specification plan, test plan, acceptance plan, architecture note and this task. Identify what is planned versus implemented.
2. Open a bounded issue for the first increment. Write `docs/adr/0001-application-boundary.md` in class: context, modular-monolith proposal, one alternative, decision, trade-offs and timing/allocation assumptions. Until the instructor decides, keep its status proposed.
3. Create a minimal Python package skeleton under `app/` and narrow, executable cancellation behaviour on a synthetic in-memory booking. Define results for valid cancellation, repeated cancellation, invalid input, non-owner and too-late request; rejected calls leave the entire record unchanged. This pure W1 seam does not claim SQLite durability, HTTP correctness or concurrency safety.
4. Add ordinary tests under `tests/`, inspect the exact diff, execute them independently of agent output, and record the actual result, revision and instructor accept/revise/reject decision. Update the specification and evidence status without filling later stages.

## W1 cancellation contract to implement live

The bounded pure seam is `cancel(booking, actor_id, now_minute) -> (result, booking_after)`. Use a synthetic booking value with `id`, `owner_id`, integer `start_minute`, positive `duration_minutes`, `groomer_id` in 1–3, `room_id` in 1–2, and `status` (`active` or `cancelled`). The time value is an integer minute on the same teaching timeline; no date/time-zone conversion is claimed at W1. No global occupancy counter exists: later availability is derived from active booking intervals.

- Validate the full input before any change; malformed data or time yields `InvalidInput` and the original booking.
- Missing actor yields `Unauthenticated`; a different actor yields `Forbidden`. Neither changes the booking.
- For the owner, an already cancelled booking yields `AlreadyCancelled` and no change, even on repetition.
- An active booking at or after its start yields `TooLate` and no change.
- Otherwise return `Cancelled` with only `status` changed to `cancelled`. All identifiers, time fields and resource assignments remain unchanged.

The caller must be able to compare the complete before/after values. W1 tests cover each result and immutability of rejected/repeated operations. This is a teaching contract; W2 defines the HTTP/storage representation and ownership proof separately.

## Live 40-minute slice

Prioritise clone/read → ADR boundary → one bounded agent proposal → one check and human decision. The optional remote-environment route may use the instructor's VM; do not spend all verification time on provider setup. If the code is unfinished, show the observed gap and a revise decision.

## Done when

The ADR and contract agree with requirements UR-04, a small skeleton and real checks exist, and the instructor can point to the actual SHA and limitations. No booking web UI, SQLite integration, release or deployment is required. [W2](W2-usable-slice.md) takes the contract into a persistent path.
