Oracle Live Review Feedback Template

- Session details
  - Date:
  - Session ID:
  - Attendees:
  - Review scope:

- Key decisions and acceptance criteria
  - Summary of accepted architecture choices
  - Any caveats or pending items

- Architecture assessment (frontend/backend)
  - Frontend: SettingsModal, ImageGenSettings alignment with canonical payload
  - Backend: session/config, endpoints, LLMClient adapters status
  - Alignment with per-provider adapters and canonical payload routing

- Canonical payload mapping
  - Canonical fields validated against provider adapters
  - Backward compatibility notes and deprecation plan for legacy fields

- Per-session isolation verification
  - Approach to secret/state scoping per session
  - Audit logs, access control, and retention policy

- Security review
  - Secret handling, rotation, vaulting
  - Logging masking and audit requirements

- End-to-end testing outcome
  - CI/mock harness status, six payload shapes coverage
  - Any failed tests and remediation plan

- Milestones and ownership updates
  - Any schedule changes, owner reassignment, or deliverable updates

- Risks and mitigations
  - List of top risks and mitigation strategies

- Outputs and follow-up actions
  - Updated Oracle_final_signoff.md and related artifacts
  - Next steps and owners
