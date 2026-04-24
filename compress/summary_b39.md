Topic: Emergency context compression (b39)

Summary:
- In this emergency compression, we consolidate the latest status around two remaining tasks:
  1) in_progress: Validate API endpoints with ZAI and OpenAI-compatible payloads
  2) pending: Consult Oracle for final architecture/review check
- Prior progress:
  - OpenAI payload handling has been hardened to accept multiple content keys (input, content, prompt) and normalize to a canonical input_content. This reduced the incidence of "Input content is required" errors.
  - Session-create validations have produced several session IDs across ZAI and OpenAI payload shapes; health endpoint is healthy.
  - End-to-end validation has been blocked due to environment lack of deterministic LLM responses; plan to switch to a CI-friendly mock end-to-end harness for determinism.
- Current blockers:
  - Live LLM path in this environment does not yield deterministic results; mock path needed for CI validation.
- Planned next steps:
  - Re-run six payload tests with robust normalization to ensure deterministic success for all plausible shapes.
  - Implement CI-friendly end-to-end harness (mock LLM) to validate start -> generate-image flows and finalize results.
  - Draft and publish the Oracle final architecture brief + a two-week sprint plan with milestones and success criteria.
  - Update payload documentation with canonical fields (provider, base_url, api_key, model, and content sinks) and rollout notes.
- Context placeholder:
  - This compression corresponds to block (b39) and serves as the authoritative summary for continuity across the session.
