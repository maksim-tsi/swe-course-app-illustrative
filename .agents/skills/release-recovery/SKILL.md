---
name: release-recovery
description: Use when preparing or reviewing the illustrative application's W5-W6 release, rollback, restore, handover, or publication evidence.
---

# Release and recovery evidence

Read the current W5/W6 task, `docs/acceptance-plan.md`, and the actual runbook/release revision. Separate five facts: source SHA, built artifact, configured deployment, application rollback, and data restoration. For each proposed claim, name the check that would observe it and the synthetic fixture it needs. A backup file's existence is not a restore result.

For a bounded drill, inspect compatibility first, then record actual version and behaviour after application rollback; restore to a **fresh disposable store** and verify expected records and behaviour separately. Preserve source/artifacts/history. Return a concise readiness or gap assessment for the instructor.

This skill grants no permission to deploy, expose a write endpoint, modify DNS, delete an old service, or handle live customer data. Stop at a reviewable plan until the instructor explicitly chooses the operational action. Do not turn an isolated drill into a production-resilience claim.
