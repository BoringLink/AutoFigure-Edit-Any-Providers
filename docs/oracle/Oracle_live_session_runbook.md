Oracle Live Session Runbook (AutoFigure Multi-Provider)

- Objective
  - Execute a formal Oracle final architecture review for the AutoFigure multi-provider integration (ZAI, OpenAI, OpenRouter).

-Pre-session prerequisites
  - Ensure all Oracle artifacts are published: Oracle_final_signoff.md, Oracle_final_full_review.md, Oracle_final_summary.md, Oracle_live_agenda.md, Oracle_live_review_template.md, Oracle_session_invite.md, e2e-test-plan.md, run-e2e.js, payload-schema-canonical.md, provider-adapters.md, and live-feedback templates.
  - Schedule attendees: Backend Lead, Frontend Lead, QA/CI Lead, Security, Product, Oracle consultant.
  - Prepare briefing materials and a canonical agenda (use Oracle_live_agenda.md).

-Session structure (60-90 minutes)
  1) Intro and scope confirmation
  2) Architecture review: frontend/backend surfaces and canonical payload flow (sanity check adapters)
  3) Per-session isolation and security review
  4) End-to-end testing plan validation (CI/mock harness, six payload shapes)
  5) Milestones, owners, and governance alignment
  6) Risks, mitigations, and open questions
  7) Summary of decisions and next steps

-Deliverables during/after session
  - Capture decisions in Oracle_final_signoff.md and Oracle_final_summary.md
  - Update payload docs and adapters as needed
  - Update governance and milestones for multi-provider support

-Post-session actions
  - Publish revised artifacts
  - Schedule follow-ups as needed
