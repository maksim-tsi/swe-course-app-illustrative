# Verification code

W1 adds executable standard-library contract tests for the pure cancellation seam. From the repository root, run `python3 -m unittest discover -s tests -v`. This command checks only in-memory W1 behaviour; executed results and the tested revision belong in the feature PR. Subsequent stages add client, API, state, integration, release and regression checks as mapped in the [test plan](../docs/test-plan.md).
