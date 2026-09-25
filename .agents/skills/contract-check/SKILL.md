---
name: contract-check
description: Use when implementing or reviewing a grooming booking, cancellation, or reschedule contract and its state effects in the current workshop stage.
---

# Contract check

1. Read the current stage task, relevant requirement IDs, and current contract in `docs/specification-plan.md` or its later stage-specific extension. If a result or ownership rule is undefined, record the question instead of inventing acceptance.
2. List success, rejection and repeated-operation examples **before** judging implementation. For each, state the returned result and expected complete state after the call, including groomer/room occupancy.
3. Inspect the changed boundary and run the ordinary available checks against those examples. At W1 the seam is in memory; do not infer W2 persistence or concurrency from it. In W2 and later, check the real storage path separately.
4. Return requirement IDs, actual commands/results, smallest relevant diff, unresolved risk, and an accept/revise/reject recommendation for the instructor. The instructor makes the decision.

Never weaken expected results to match a generated implementation or call a planned test passed.
