#!/usr/bin/env bash
set -euo pipefail

BASE="http://127.0.0.1:8796/api/autofigure/session/create"

echo "Running extended canonical payload tests (additional)"

cat > /tmp/zai_payload5.json <<JSON
{ "config": {"llmProvider": "zhipuai", "api_key": "TEST", "base_url": "", "model": "glm-4.7-flash"}, "input_content": "Hello ZAI canonical E" }
JSON
cat > /tmp/openai_payload5.json <<JSON
{ "config": {"llmProvider": "openai", "api_key": "TEST", "base_url": "", "model": "gpt-4e"}, "input_content": "Hello OpenAI canonical E" }
JSON

echo "ZAI5 (expected SUCCESS):"; curl -s -X POST -H 'Content-Type: application/json' -d @/tmp/zai_payload5.json $BASE | head -n 5
echo "OpenAI5 (expected SUCCESS):"; curl -s -X POST -H 'Content-Type: application/json' -d @/tmp/openai_payload5.json $BASE | head -n 5

cat > /tmp/zai_payload6_missing.json <<JSON
{ "config": {"llmProvider": "zhipuai", "api_key": "TEST", "base_url": "", "model": "glm-4.7-flash"} }
JSON
echo "ZAI6-missing-input (expected error):"; curl -s -X POST -H 'Content-Type: application/json' -d @/tmp/zai_payload6_missing.json $BASE | head -n 5 || true
