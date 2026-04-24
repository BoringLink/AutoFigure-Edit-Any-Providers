Oracle Final Architecture Sign-Off - AutoFigure Multi-Provider Integration

Overview
- This document captures the definitive architecture decisions, acceptance criteria, risk posture, and rollout plan for the AutoFigure multi-provider integration (ZhipuAI, OpenAI, and future providers).
- The sign-off confirms alignment between the frontend, backend adapters, payload canonicalization, per-session config, and testing strategy, with a clear path to production deployment.

1) Architecture snapshot (final)
- Canonical payload: provider, base_url, api_key, model, input_content/input/content/prompt (normalized to input_content)
- Provider adapters: a unified adapter layer with per-provider concrete implementations for ZAI and OpenAI; an OpenAI-compatible shim to bridge differences for future providers
- Per-session config: each session stores provider, base_url, api_key, model; session isolation enforced
- Security posture: per-session secrets, redacted logging, plan for vault-backed secrets in production
- Data flow: frontend -> backend canonical payload -> per-session config storage -> provider adapters -> response generation
- Endpoints involved: session/create, session/{id}/start, session/{id}/continue, generate-image (via adapter)

2) Acceptance criteria (final)
- All canonical payload shapes pass in CI (including edge cases)
- Deterministic per-session config isolation validated
- End-to-end flow validated via CI/mock harness for at least one ZAI and one OpenAI session
- Architecture sign-off from Security, Product, and Operations representatives
- Documentation updated to reflect final decisions

3) Risks & mitigations
- Provider drift: maintain small shim/adapter layer; add tests per provider
- Secret management: per-session isolation; plan for vault integration in Q2
- End-to-end testing with live providers: rely on deterministic CI mocks; schedule live provider verification in staging
- Rollout complexity: feature flags and staged rollout with rollback gates

4) Rollout plan (high level)
- Phase 1: Confirm Oracle sign-off; lock canonical payload; finalize adapters
- Phase 2: Enable CI/mock end-to-end; run 2-week sprint completes
- Phase 3: Production staging with guarded rollout and metrics
- Phase 4: Full production after monitoring window

5) Open questions & owners
- Q1: Default provider policy (owner: Product) 
- Q2: Dynamic provider registry vs static enum (owner: Architecture)
- Q3: Error taxonomy across providers (owner: Backend)
- Q4: Vault/secrets integration plan (owner: Security)
- Q5: End-to-end harness acceptance criteria (owner: QA/CI)

6) Approval & sign-off
- Sign-off by: Architecture Owner, Security Lead, Product Manager, and DevOps Lead
- Sign-off date: TBD (to be scheduled by Oracle review)

7) Deliverables linked to this sign-off
- This Oracle_final_signoff.md document finalized and stored in docs/
- Updated Oracle_review_schedule.md with final review date and attendees
- Updated docs/sprint_plan.md with final milestones linked to sign-off

Notes
- This document is the canonical reference for production sign-off. Any future changes should go through the Oracle review process and be reflected in this document.
