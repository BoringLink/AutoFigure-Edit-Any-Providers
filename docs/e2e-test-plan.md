End-to-end Test Plan: AutoFigure multi-provider integration (ZAI/OpenAI/OpenRouter)

Overview
- Validate six canonical payload shapes across ZAI, OpenAI, and OpenRouter without invoking real LLMs.
- Ensure per-session isolation holds across test runs.

Test matrix (six canonical shapes)
- Shape 1: ZAI layout (glm-4.7-flash)
- Shape 2: ZAI methodology (glm-4.7-flash)
- Shape 3: OpenAI layout (gpt-4x)
- Shape 4: OpenRouter layout (rg) TBD
- Shape 5: Mixed-provider session (ZAI + OpenAI in separate sessions)
- Shape 6: Backward-compat legacy payload path (to ensure migration path works)

Test cases
- Valid payloads initialize a session and begin a generation flow.
- Invalid provider/base_url/api_key combinations fail gracefully with actionable errors.
- Per-session isolation verified by running two sessions concurrently with different keys.
- Error paths: missing fields, invalid model names, unsupported provider combinations.

Validation approach
- Use CI with a mock LLM backend returning deterministic responses.
- Assertions around request construction, correct routing to provider adapters, and session-scoped data.
- End-to-end smoke tests to cover session create, start/generate, and finalize flows.

Success criteria
- All six canonical shapes pass under mock backend with no leakage across sessions.
- No unhandled errors; correct error handling for invalid inputs.
- Documentation updated with payload shapes and test coverage.
