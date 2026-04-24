Payload Schema: Canonical vs Legacy (AutoFigure multi-provider)

Canonical fields (per session):
- provider: one of zhipuai|openai|openrouter|bianxie|gemini|openrouter
- base_url: provider base URL for the API endpoint
- api_key: per-session secret key (not logged)
- model: provider-specific model name (e.g., glm-4.7-flash, gpt-4x, etc.)
- input_content: structured input (content, prompts, or content blocks) to feed the model

Legacy fields and migration
- Legacy fields may include: prompt, input, content, input_content
- Canonical mapper translates legacy fields into input_content when possible; validation ensures no data loss.

Validation rules
- base_url must be a valid URL; api_key must be non-empty; model must be non-empty and valid for provider.
- If provider is zhipuai, base_url must start with https://open.bigmodel.cn/api/paas/v4
- Per-session isolation checks ensure no leakage of keys between sessions.

Examples
- Canonical payload (ZAI):
  {
    provider: "zhipuai",
    base_url: "https://open.bigmodel.cn/api/paas/v4",
    api_key: "******",
    model: "glm-4.7-flash",
    input_content: { prompt: "Describe figure..." }
  }
