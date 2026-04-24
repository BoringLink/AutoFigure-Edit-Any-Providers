Oracle final architecture review for multi-provider AutoFigure integration

Overview
- Objective: Validate and finalize the architecture for multi-provider AutoFigure integration (ZhipuAI, OpenAI, and future providers) with a unified payload model, per-session configuration, and provider adapters.
- Scope: Assess provider adapters, payload canonicalization, session isolation, security considerations, testing strategy, deployment plan, and governance deliverables.

Key findings
- Architecture alignment: The current design supports two primary providers with a thin shim layer to normalize API differences. A canonical payload surface has been defined and enforced across frontend/backend boundaries.
- Per-session isolation: Config (provider, base_url, api_key, model) is persisted per session to prevent cross-session leakage.
- Adapters and unification: A provider adapter layer exists to route to provider-specific endpoints; an OpenAI-compatible shim reduces duplication when integrating new providers.
- Testing posture: Initial payload canonicalization tests are deterministic. A CI harness plan is in place to cover unit, integration, and end-to-end scenarios using mocks to avoid live LLM dependencies.
- Security posture: Per-session API keys are not logged; lookups are ephemeral; recommend institutionalizing a short-lived key mechanism and vault integration for production.
 
Open questions
- Should there be a universal default provider, and if so, what governs its selection (env, tenant, or session-level)?
- How should new providers be registered (static enum vs dynamic registry) and how will their base_urls be discovered?
- What is the exact SLA for end-to-end tests when a provider is unavailable or rate-limited? How will retries be modeled in tests?
- Are there any compliance considerations for cross-border data routing when using multiple providers?

Recommendations
- Freeze the current canonical payload surface and ensure all new providers route through the adapter shim.
- Implement per-session secret management with an abstraction to swap in a vault-backed secret store in production.
- Extend tests to cover at least three scenarios per provider: (a) full payload with input_content, (b) payload using input/content, (c) payload using prompt, across both ZAI and OpenAI.
- Finalize CI harness details and commit to the repo with a dedicated test suite.
- Schedule a formal architecture review with stakeholders before release.

Deliverables
- Final architecture document (this file) + a published sprint plan (docs/sprint_plan.md).
- A formal acceptance criteria checklist and a risk register.
- A plan for deployment and rollback in case of provider-specific issues.

Action items (next steps for the team)
- Implement and validate the per-session configuration persistence in code paths used by session_create/start/generate.
- Complete and integrate the CI mock end-to-end harness for deterministic validation.
- Schedule and conduct an architecture review session with stakeholders; capture decisions and update the plan accordingly.
