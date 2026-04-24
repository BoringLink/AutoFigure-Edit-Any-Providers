# AutoFigure API Payload Examples

This document contains sample payload shapes for common endpoints to help QA and integration tests. Replace placeholder values with real credentials in your environment when running end-to-end tests.

- Create Session (POST /api/autofigure/session/create)

```
{
  "config": {
    "contentType": "paper",
    "maxIterations": 3,
    "qualityThreshold": 9.0,
    "minImprovement": 0.2,
    "humanInLoop": true,
    "llmProvider": "zhipuai",
    "apiKey": "<YOUR_ZHIPUAI_API_KEY>",
    "baseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4.7-flash",
    "svgWidth": 1333,
    "svgHeight": 750,
    "enableMethodologyExtraction": true,
    "methodologyLlmProvider": "zhipuai",
    "methodologyLlmApiKey": "<YOUR_ZHIPUAI_API_KEY>",
    "methodologyLlmBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "methodologyLlmModel": "glm-4.7-flash",
    "enhancementMode": "code2prompt",
    "artStyle": "",
    "enhancementCount": 3,
    "enhancementProvider": "zhipuai",
    "enhancementLlmProvider": "zhipuai",
    "enhancementLlmApiKey": "<YOUR_ZHIPUAI_API_KEY>",
    "enhancementLlmBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "enhancementLlmModel": "glm-4.7-flash",
    "imageGenProvider": "zhipuai",
    "imageGenApiKey": "<YOUR_ZHIPUAI_API_KEY>",
    "imageGenBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "imageGenModel": "glm-4.7-flash"
  },
  "input_content": "Sample content for session creation",
  "input_type": "text"
}
```

- Generate Image (POST /generate-image)

```
{
  "prompt": "A schematic diagram of AI workflow",
  "provider": "zhipuai",
  "api_key": "<YOUR_ZHIPUAI_API_KEY>",
  "model": "glm-4.7-flash",
  "base_url": "https://open.bigmodel.cn/api/paas/v4"
}
```

- Extend: OpenRouter/OpenAI-style payload compatibility can be added via the backend routing shim.
