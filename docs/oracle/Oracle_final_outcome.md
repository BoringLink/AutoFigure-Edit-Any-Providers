Oracle Final Outcome Plan (AutoFigure Multi-Provider)

- Objective: Deliver a finalized Oracle-guided architecture outcome, with a patch-ready artifact bundle and a live Oracle session to obtain official feedback for the ZAI/OpenAI/OpenRouter integration.

- What will be published in the patch
  - Oracle_final_signoff.md
  - Oracle_final_full_review.md
  - Oracle_final_summary.md
  - Oracle_live_agenda.md
  - Oracle_live_review_agenda.md
  - Oracle_live_review_template.md
  - Oracle_live_session_runbook.md
  - Oracle_session_invite.md
  - e2e-test-plan.md
  - tests/e2e/run-e2e.js
  - payload-schema-canonical.md
  - provider-adapters.md
  - Oracle_live_feedback_template.md
  - Oracle_final_review_instructions.md
  - Oracle_live_session_runbook.md (existing)
  - Oracle_live_feedback_template.md (backup/structure)

- Live session plan
  - Use Oracle_live_agenda.md + Oracle_live_review_template.md as briefing
  - Queue the session at earliest available window
  - Capture decisions and update Oracle_final_signoff.md and Oracle_final_summary.md accordingly

- Post-session actions
  - Update governance for ongoing multi-provider support
  - Reflect Oracle feedback in the artifacts and testing scope
  - If necessary, consolidate artifacts into a governance-ready bundle

- Patch/PR approach
  - Publish as a single patch including all Oracle artifacts for governance traceability
  - After patch merge, queue the live Oracle session and align briefing with the latest content

- Notes
  - The environment may intermittently block live Oracle session startups; the artifacts and runbook are prepared to ship and will be used as the briefing basis once the session can be launched.
