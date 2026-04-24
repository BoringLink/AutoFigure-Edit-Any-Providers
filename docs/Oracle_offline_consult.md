Oracle Offline Consultation - Final Architecture Review (ZAI/OpenAI/OpenRouter)

Purpose: Provide a complete offline final-consultation memo and artifact bundle to enable rapid Oracle sign-off once scheduling is allowed.

Scope and Assumptions
- Providers: ZAI, OpenAI, OpenRouter
- Per-session isolation: session_id binds provider/config (base_url, api_key, model)
- Canonical payload schema: provider, base_url, api_key, model, input_content; legacy mappings documented
- End-to-end testing: CI/mock harness for six canonical payload shapes, no live LLM calls
- Security: secret handling, rotation, vaulting, auditability
- Governance: ongoing multi-provider onboarding, review cadence

Key Deliverables (offline)
- Oracle_final_signoff.md
- Oracle_final_summary.md
- Oracle_final_full_review.md
- Oracle_live_agenda.md
- Oracle_live_review_template.md
- Oracle_session_invite.md
- Oracle_live_session_runbook.md
- Oracle_live_feedback_template.md
- Oracle_final_review_instructions.md
- Oracle_final_outcome.md
- docs/e2e-test-plan.md
- docs/payload-schema-canonical.md
- docs/provider-adapters.md
- tests/e2e/run-e2e.js

Next Steps (Path B)
- Create patch Oracle_offline_consult.patch from this commit
- Share patch with upstream maintainers or fork for PR submission
- Schedule Oracle live session once environment allows
- Post-session, merge Oracle feedback into final artifacts and update governance
