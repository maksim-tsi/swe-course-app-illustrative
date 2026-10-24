# W1 verification evidence

**Status:** independent W1 verification record. The instructor decision remains pending; this note is not acceptance.

**Requirement:** UR-04. **Stage:** [W1 — Initiate the grooming-studio example](W1-initiation.md).

## Revision

- Integration baseline: `origin/dev-max` at `259dce7` (merge of PR #4).
- Existing W1 implementation: `24d00b7` (`app/grooming/`, `tests/`, proposed ADR-001).
- Verified revision: `796aa1cf671b165ff72ca4de5a39a09ae6df98ae` on `feature/w1-verification`.
- Later commits on the verification branch add documentation only; `app/grooming/` and `tests/test_cancellation.py` are unchanged after the verified revision.

## Environment and commands

Environment: Linux, Python 3.12.3, standard-library `unittest`; no third-party test dependency.

```text
$ python3 -m unittest discover -s tests -v
Ran 13 tests in 0.001s
OK
$ echo $?
0

$ python3 -m compileall -q app
$ echo $?
0

$ git diff --check
$ echo $?
0
```

The checked revision had a clean working tree before the evidence note was added.

## W1 result matrix

| Result | Condition | Booking state |
|---|---|---|
| `Cancelled` | Owner, active booking, `now_minute < start_minute` | New value; only `status` changes to `cancelled` |
| `AlreadyCancelled` | Owner, booking already cancelled, including at/after start | Original unchanged |
| `InvalidInput` | Malformed booking field or time, including malformed actor type | Original unchanged; checked before authorization and state |
| `Unauthenticated` | Missing or blank actor, including on a cancelled booking | Original unchanged |
| `Forbidden` | Different string actor, including at/after start or on a cancelled booking | Original unchanged |
| `TooLate` | Owner, active booking, `now_minute >= start_minute` | Original unchanged |

Covered boundaries include `start_minute - 1` (successful cancellation) and `start_minute` (`TooLate`), repeated cancellation at/after start, `duration_minutes` `0` and negative, both sides of the groomer and room ranges, non-integer times, non-string actors, and validation/authorization precedence.

## Test-oracle change

The original W1 tests compared a returned rejected booking to itself and built the successful expectation with `replace(...)` after the call. That did not independently prove that every field was preserved. The verification branch now:

- captures a full `dataclasses.asdict` snapshot before each call;
- requires every rejection to return the identical original object with the full snapshot unchanged;
- requires successful cancellation to return a distinct object whose only changed field is `status`, while the input remains unchanged.

## Review findings addressed

- ADR-001 now states the input-validation rule, non-blank identifiers, non-boolean integers, result precedence and the W1 timeline limit explicitly.
- Negative `start_minute`/`now_minute` values remain an explicit W1 limitation; W2 must define timeline bounds.
- No implementation defect was found in the independent backend probes. No application code changed on this branch.
- The added tests cover validation before authorization, authorization before lateness, and authentication before cancelled state.

## Limits

- This evidence covers only the pure in-memory W1 cancellation seam.
- It does not establish SQLite durability, transaction behaviour, HTTP correctness, browser behaviour, concurrency safety, real identity or ownership proof, resource-release accounting, deployment or recovery.
- Opening hours, the 30-minute start grid, service durations and date/time-zone conversion remain W2 work.
- A passing 13-test suite and compile check bound the claim; they do not prove defect freedom.

## References

- [Issue #3](https://github.com/maksim-tsi/swe-course-app-illustrative/issues/3)
- [W1 pull request #4](https://github.com/maksim-tsi/swe-course-app-illustrative/pull/4)
- [Proposed ADR-001](../adr/0001-application-boundary.md)
- [W1 stage brief](W1-initiation.md)
