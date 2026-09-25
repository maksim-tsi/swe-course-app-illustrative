# Why these skills exist

Skills capture **repeatable methods**, while the root `AGENTS.md` carries always-on repository rules and `roles/` identifies a specialist's task. This keeps prompts short and portable between OpenCode, Codex and Antigravity. A skill is loaded when relevant; it is not a new product requirement, a substitute for actual checks, or permission to run an operational action.

We selected three workflows that recur across stages and change agent decisions:

- [`contract-check`](contract-check/SKILL.md): derive behaviour and state checks from a named requirement before accepting a code change (W1 onward).
- [`test-design`](test-design/SKILL.md): build a small risk-based test set and interpret sensitivity without a discovery quota (W2–W4, reused later).
- [`release-recovery`](release-recovery/SKILL.md): separate application rollback, data restoration and publication evidence (W5–W6). It stops before external deployment without explicit instructor action.

Each folder contains a concise `SKILL.md` with required `name` and `description` frontmatter. The descriptions state when to load it; details live in the body. No model-specific provider configuration, credentials, automatic paid API call, or duplicate product specification is embedded. Maintain one canonical requirement/test/acceptance plan and update a skill only when the *method* changes. Review tool discovery against current vendor documentation before teaching; repository placement alone does not guarantee identical behaviour in all harnesses.
