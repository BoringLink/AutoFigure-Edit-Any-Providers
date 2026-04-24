# Oracle Final Sign-off: AutoFigure multi-provider integration (ZAI/OpenAI/OpenRouter)

Executive summary: This document records the authoritative decisions from the Oracle final architecture review for the AutoFigure multi-provider integration. It covers frontend and backend surface changes, per-session isolation across providers, canonical API payload schema, end-to-end testing strategy, security considerations, milestones, ownership, and governance for ongoing multi-provider support.

1. Scope
- Frontend: SettingsModal.tsx, ImageGenSettings.tsx
- Backend: autofigure_routes.py, session/config defaults, and payload handling
- Providers: ZAI, OpenAI, OpenRouter; per-session isolation; migration path for new providers

2. Architecture decisions
- A centralized provider negotiation layer coordinates provider selection and model choices, with strict per-session scoping.
- Base URLs and API keys are managed per session to ensure isolation and reproducibility of runs.
- Backward compatibility strategy is defined: maintain a canonical payload shape while enabling provider-specific extensions via adapters.

3. Per-session isolation
- Each session binds provider, base_url, api_key, and model to a unique session_id; data from one session cannot be leaked to another.
- Keys rotation, revocation, and audit logging are standardized across sessions.

4. Canonical payload schema
- Required fields: provider, base_url, api_key, model, input_content (or prompt).
- Support for multiple input formats with a canonical mapping layer; legacy fields are migrated with documented rules.
- Validation rules per provider to catch misconfigurations before API calls.

5. End-to-end testing plan (CI/mock harness)
- A CI harness validates six canonical payload shapes across ZAI/OpenAI/OpenRouter without invoking real LLMs.
- Test matrix includes provider/provider-model permutations, session-scoped credentials, and fallback paths.
- Acceptance criteria and rollback procedures are defined.

6. Security considerations
- Secrets are stored and transmitted per-session only; no cross-session leakage.
- Rotation cadence, vaulting options, and audit trails are specified.

7. Milestones, owners, deliverables
- Milestone 1: Patch publication with all Oracle artifacts — Architecture Lead
- Milestone 2: Schedule/live Oracle session — Project Manager
- Milestone 3: Integrate Oracle feedback — Tech Lead + QA
- Milestone 4: Lock down per-session isolation + canonical payload docs — Backend/Frontend leads
- Milestone 5: CI/mock E2E validation — QA/CI Engineers

Deliverables: Oracle_final_signoff.md, Oracle_final_summary.md, Oracle_final_full_review.md, E2E/payload/docs, and runbooks referenced in the patch.

8. Risks and mitigations
- Live session scheduling delays: fallback offline briefing; CI/mock validation continues.
- Provider API drift: versioned payload schema with migration guide.
- Secrets leakage: strict per-session scoping and auditable vaulting.

9. Success criteria
- Clear Oracle sign-off with milestones and governance guidance.
- Verified offline CI/mock end-to-end coverage for canonical payloads.
- Patch published with full artifact traceability.

10. Governance model
- Onboarding of new providers, payload normalization standards, and review cadence.
- Per-session isolation policy and access controls.

Appendix: Patch provenance and identifiers will be included in the patch metadata.
