#!/usr/bin/env bash
set -euo pipefail

BASE_URL=${BASE_URL:-http://127.0.0.1:8796}

cat > /tmp/zai_payload1.json <<'JSON'
{ "config": {"llmProvider": "zhipuai", "api_key": "TEST", "base_url": "", "model": "glm-4.7-flash"}, "input_content": "Hello ZAI AAA" }
JSON
cat > /tmp/zai_payload2.json <<'JSON'
{ "config": {"llmProvider": "zhipuai", "api_key": "TEST", "base_url": "", "model": "glm-4.7-flash"}, "input": "Hello ZAI BBB" }
JSON
cat > /tmp/zai_payload3.json <<'JSON'
{ "config": {"llmProvider": "zhipuai", "api_key": "TEST", "base_url": "", "model": "glm-4.7-flash"}, "prompt": "Hello ZAI CCC" }
JSON

cat > /tmp/openai_payload4.json <<'JSON'
{ "config": {"llmProvider": "openai", "api_key": "TEST", "base_url": "", "model": "gpt-4e"}, "input_content": "Hello OpenAI DDD" }
JSON
cat > /tmp/openai_payload5.json <<'JSON'
{ "config": {"llmProvider": "openai", "api_key": "TEST", "base_url": "", "model": "gpt-4e"}, "input": "Hello OpenAI EEE" }
JSON
cat > /tmp/openai_payload6.json <<'JSON'
{ "config": {"llmProvider": "openai", "api_key": "TEST", "base_url": "", "model": "gpt-4e"}, "prompt": "Hello OpenAI FFF" }
JSON

printf "Running six payload tests...\n"
for f in /tmp/zai_payload1.json /tmp/zai_payload2.json /tmp/zai_payload3.json /tmp/openai_payload4.json /tmp/openai_payload5.json /tmp/openai_payload6.json; do
  echo "Testing $f"
  curl -s -X POST -H "Content-Type: application/json" -d @$f $BASE_URL/api/autofigure/session/create | head -n 6
  echo
done
