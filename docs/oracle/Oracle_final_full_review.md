Oracle Final Full Review: AutoFigure multi-provider integration (ZAI/OpenAI/OpenRouter)

Scope
- Validate end-to-end data flow across frontend (SettingsModal, ImageGenSettings) and backend (autofigure_routes/config).
- Enforce per-session isolation for ZAI, OpenAI, and OpenRouter providers.
- Define a canonical payload schema and migration path from legacy fields.
- Establish CI/mock end-to-end testing coverage for six canonical payload shapes.
- Address security, governance, milestones, and ownership.

Key decisions
- A unified provider negotiation layer with per-session scoping for keys/base URLs/models.
- Canonical payload shape: provider, base_url, api_key, model, input_content; support mapping for prompt usage.
- Migration plan: maintain backward compatibility while phasing to canonical fields.
- CI/mock testing: six canonical payload shapes, per-session isolation checks, and rollback.
- Security: per-session secret handling, vault integration options, auditability.
- Governance: provider onboarding, review cadence, change management, and incident response.

Details
- Frontend changes: UI components expose provider choices with per-provider model lists; placeholders and base URLs adapt to provider when selected.
- Backend changes: session config binds keys/models per session; routes validate canonical payloads and route through provider adapters.
- End-to-end: CI/math harness simulates provider responses without hitting real LLMs; tests cover success and failure paths.
- Security: tokens/secrets stored per-session; rotation policy specified; auditing of access and usage.

Risks & mitigations
- Session leakage risk: mitigated via strict scoping and isolation boundaries; implement per-session vault access controls.
- Provider API drift: mitigate with versioned schema and migration guide.
- Live Oracle session delays: offline briefing available; CI/mock harness ensures progress.

Milestones & owners
- Patch publication: Architecture Lead
- Live Oracle session: Project Manager
- Feedback integration: Tech Lead + QA
- Per-session isolation/docs: Backend/Frontend leads
- CI/mock E2E validation: QA/CI Engineers

Deliverables
- Oracle_final_signoff.md, Oracle_final_summary.md, Oracle_final_full_review.md
- E2E/payload/docs, provider adapters, runbooks, and live-session templates

Conclusion
- This document provides a comprehensive, production-ready blueprint for Oracle finalization. It is ready to accompany the patch and serve as the canonical reference once the live Oracle session can be conducted.
