Oracle Live Review Feedback Template
- Session details
  - Date:
  - Attendees:
  - Session ID:

- Scope and decisions recap
  - What was reviewed
  - Key acceptance criteria

- Architecture assessment
  - Frontend surfaces reviewed: SettingsModal, ImageGenSettings
  - Backend surfaces reviewed: session/config, endpoints, adapters
  - Alignment with canonical payload and per-provider adapters

- Canonical payload mapping results
  - How canonical payload fields map to each provider adapter
  - Backward-compat aliases handling and deprecation plan

- Per-session isolation verification plan
  - Approach to secret/state scoping per session
  - Audit/logging requirements and retention policy

- Security review notes
  - Secrets handling, rotation, vaulting
  - Access controls and masking in logs

- End-to-end testing verdict
  - CI/mock harness status, six payload shapes coverage
  - Confidence level and any edge cases

- Milestones and ownership updates
  - Any changes to milestones, owners, or deliverables

- Risks, mitigations, and open questions
  - List top risks and proposed mitigations
  - Any unresolved questions for Oracle

- Outputs to update in repository
  - Oracle_final_signoff.md
  - Oracle_final_summary.md
  - payload-schema-canonical.md (if needed)
  - provider-adapters.md (if needed)
