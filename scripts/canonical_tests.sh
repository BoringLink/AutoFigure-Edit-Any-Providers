#!/usr/bin/env bash
set -euo pipefail

BASE="http://127.0.0.1:8796/api/autofigure/session/create"

payloads=(
  '{"config":{"llmProvider":"zhipuai","api_key":"TEST","base_url":"","model":"glm-4.7-flash"},"input_content":"Hello ZAI canonical D"}'
  '{"config":{"llmProvider":"openai","api_key":"TEST","base_url":"","model":"gpt-4e"},"input_content":"Hello OpenAI canonical D"}'
)

echo "Running canonical payload tests (additional)"
for p in "${payloads[@]}"; do
  echo "POST payload: $p"
  curl -s -X POST -H 'Content-Type: application/json' -d "$p" "$BASE" | head -n 5
  echo
done
