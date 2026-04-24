Oracle final architecture for multi-provider AutoFigure integration

Executive summary
- This document formalizes the target architecture for integrating multiple LLM providers (ZhipuAI, OpenAI, and future providers) into the AutoFigure workflow, with a unified payload model, per-session configuration, and provider adapters.
- The architecture emphasizes deterministic, testable behavior, per-session isolation of keys/config, and a minimal OpenAPI-compatible shim to normalize provider differences.

1. System overview
- Frontend (UI): selects provider, model, base URL, and API key; passes canonical payload components to the backend.
- Backend: contains a provider adapter layer that routes to provider-specific endpoints. It normalizes incoming payloads into a canonical shape and maintains per-session configurations.
- Providers supported (current): zhipuai, openai. Additional providers can be added via the adapter layer with minimal code changes.

2. Core data model and payload canonicalization
- Canonical payload fields (incoming from frontend):
  - provider (e.g., zhipuai, openai)
  - base_url (provider base API URL)
  - api_key (provider API key, per-session isolation)
  - model (provider-specific model identifier)
  - input_content | input | content | prompt (normalized to input_content for downstream processing)
- Normalization rules: the backend resolves input_content by checking, in order, input_content, input, content, prompt, including nested config.config structures. If none exist, treat as empty string and return a controlled error.

3. Provider adapters (backend)
- A single adapter interface handles common calls and translates to provider-specific API endpoints.
- zhipuai adapter: maps to zhipuai API endpoints using provided base_url and api_key.
- openai adapter: maps to OpenAI API endpoints (base_url default https://api.openai.com/v1).
- OpenAPI-compatible shim: existing providers can be routed through the shim to unify behavior when necessary.

4. Session lifecycle
- Create session: store per-session config (provider, base_url, api_key, model).
- Start/Continue: validate inputs; persist state in-session; propagate canonical payload to provider adapter.
- Generate image: route to generate-image path (with provider adapter); supports both ZAI and OpenAI-compatible requests via the adapter.
- Finalize: complete lifecycle, free resources; health endpoints reflect session state.

5. Security and data handling
- API keys are never logged beyond necessary call-time usage; per-session isolation ensures no leakage across sessions.
- Do not persist secrets in logs, caches, or O/S history.
- Validate payloads strictly; return meaningful errors on missing fields.

6. Validation plan and tests
- Unit tests: payload canonicalization logic, per-provider adapter call builders.
- Integration tests: simulate session lifecycle using mocks for both ZAI and OpenAI providers.
- End-to-end tests: CI harness with deterministic mocks to validate session.create -> start -> generate-image flows.

7. Rollout considerations
- Stepwise rollout with feature flags; monitor error rates per provider; provide quick rollback if issues arise.
- Documentation and examples updated for canonical payload shapes.

8. Risks and mitigations
- Provider drift: implement adapters with a thin shim layer to minimize downstream changes.
- Secrets leakage: implement strict per-session storage and secure retrieval only during request handling.
- End-to-end tests relying on real LLMs: use CI mocks to validate flows deterministically.

Deliverables
- Oracle final architecture document (this file)
- Two-week sprint plan (see docs sprint plan)
- Updated payload documentation with canonical fields and examples
