#!/usr/bin/env bash
set -euo pipefail
ROOT_URL=${ROOT_URL:-http://127.0.0.1:8796}

echo "== Validating ZAI payloads (session create) =="
cat > /tmp/payload_zai.json <<'JSON'
{
  "config": {
    "contentType": "paper",
    "maxIterations": 2,
    "qualityThreshold": 9.0,
    "minImprovement": 0.2,
    "humanInLoop": true,
    "llmProvider": "zhipuai",
    "apiKey": "DUMMY_ZHIPUAI_KEY",
    "baseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "model": "glm-4.7-flash",
    "svgWidth": 1333,
    "svgHeight": 750,
    "enableMethodologyExtraction": true,
    "methodologyLlmProvider": "zhipuai",
    "methodologyLlmApiKey": "DUMMY",
    "methodologyLlmBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "methodologyLlmModel": "glm-4.7-flash",
    "enhancementMode": "code2prompt",
    "artStyle": "",
    "enhancementCount": 1,
    "enhancementProvider": "zhipuai",
    "enhancementLlmProvider": "zhipuai",
    "enhancementLlmApiKey": "DUMMY",
    "enhancementLlmBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "enhancementLlmModel": "glm-4.7-flash",
    "imageGenProvider": "zhipuai",
    "imageGenApiKey": "DUMMY",
    "imageGenBaseUrl": "https://open.bigmodel.cn/api/paas/v4",
    "imageGenModel": "glm-4.7-flash"
  },
  "input_content": "Test input",
  "input_type": "text"
}
JSON

echo "Posting ZAI session create..."
curl -s -X POST -H "Content-Type: application/json" -d @/tmp/payload_zai.json ${ROOT_URL}/api/autofigure/session/create | head -n 20

echo "== Validating OpenAI payloads (session create) with shim =="
cat > /tmp/payload_openai.json <<'JSON'
{
  "config": {
    "contentType": "paper",
    "maxIterations": 2,
    "qualityThreshold": 9.0,
    "minImprovement": 0.2,
    "humanInLoop": true,
    "llmProvider": "openai",
    "apiKey": "DUMMY_OPENAI_KEY",
    "baseUrl": "https://api.openai.com/v1",
    "model": "gpt-4",
    "svgWidth": 1333,
    "svgHeight": 750,
    "enableMethodologyExtraction": false,
    "methodologyLlmProvider": "openai",
    "methodologyLlmApiKey": "",
    "methodologyLlmBaseUrl": "",
    "methodologyLlmModel": "",
    "enhancementMode": "none",
    "artStyle": "",
    "enhancementCount": 1,
    "enhancementProvider": "openai",
    "enhancementLlmProvider": "openai",
    "enhancementLlmApiKey": "",
    "enhancementLlmBaseUrl": "",
    "enhancementLlmModel": "",
    "imageGenProvider": "openai",
    "imageGenApiKey": "",
    "imageGenBaseUrl": "https://api.openai.com/v1",
    "imageGenModel": "gpt-4-image"
  },
  "input_content": "Test input OpenAI",
  "input_type": "text"
}
JSON

echo "Posting OpenAI session create..."
curl -s -X POST -H "Content-Type: application/json" -d @/tmp/payload_openai.json ${ROOT_URL}/api/autofigure/session/create | head -n 20

echo "Diagnostics: End of basic endpoint validation."
