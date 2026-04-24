Provider Adapters: ZAI/OpenAI/OpenRouter

- ZAI: Base URL https://open.bigmodel.cn/api/paas/v4; model names glm-4.7-flash, etc.
- OpenAI: Base URL https://api.openai.com/v1; models gpt-4o, etc.; authentication via Bearer token (api_key)
- OpenRouter: Base URL depends on deployment; compatibility layer for OpenAI-style endpoints

Per-session isolation policy applies across all adapters:
- session_id binds provider, base_url, and api_key; no leakage across sessions
- rotation/revocation handled via a per-session vault scope
