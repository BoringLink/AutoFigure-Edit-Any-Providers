Topic: ZAI UI & Backend Upgrades

- This compression summarizes the combined changes across three blocks (b6, b7, b8) related to the ZHIPUAI (ZAI) integration in AutoFigure. The work spans frontend UI updates, backend wiring, diagnostics scaffolding, and testing plans for multi-provider support. (b6) 

1) Frontend enhancements (SettingsModal.tsx, ImageGenSettings.tsx, and type definitions)
- Completed: SettingsModal now surfaces ZAI as a methodology provider with fixed ZAI-friendly models. The model dropdown includes ZAI-specific options like glm-4.7-flash and UI hints adapt to ZAI.
- Completed: ImageGenSettings recognizes ZAI as a provider; default base URL is wired to ZHIPUAI_BASE_URL; placeholders updated to reflect ZAI prompts.
- Expanded LLProvider enum in frontend types to include zhipuai and adjusted default mappings for ZAI-derived flows.
- Result: Frontend UX aligns with ZAI provider usage and supports per-session config for ZAI models.
(b6) 

2) Backend enhancements (autofigure_routes.py)
- Completed/partially completed: Back-end now recognizes ZHIPUAI as a provider, wiring API key/base URL/model through the start flow. Reset logic initializes ZHIPUAI keys to avoid cross-session leakage.
- Added a path for OpenAI compatibility and image-generation shim to stabilize multi-provider usage. Implemented per-provider model mapping for ZHIPUAI and OPENAI in start_generation, and extended the model field handling to set ZHIPUAI_MODEL when provided.
- Health and session lifecycle remain intact; health endpoints accessible at /health and /api/autofigure/health. Routes for session/create, session/start, and generate-image are recognized by the backend and can be exercised with provider-specific payloads.
(b7) 

3) Diagnostics scaffolding and documentation (tests payloads)
- Added scripts/diagnostics.sh to exercise health endpoints and attempt session creation; added docs/api_payload_examples.md with ZAI/OpenAI-compatible payload templates and a generate-image example.
- Created a lightweight OpenRouter shim path for image generation to improve stability while building OpenAI-compatible endpoints.
(b8) 

4) Current status and next steps
- Remaining tasks include finalizing a unified OpenAI-compatible backend surface, implementing end-to-end tests for ZAI and OpenAI flows, and coordinating an Oracle review. The plan is to finalize OpenAI wiring, run diagnostics, then perform a fresh Oracle review with clear milestones and a two-week plan.
