#!/usr/bin/env bash
set -euo pipefail

echo "=== AutoFigure Diagnostics ==="
echo
echo "Backend health (legacy /health):"
curl -s http://127.0.0.1:8796/health | head -n 20
echo
echo "Backend health (api health):"
curl -s http://127.0.0.1:8796/api/autofigure/health | head -n 20
echo
echo "Attempting to create a session (requires API keys in payload; may fail)" 
payload='{"config":{"contentType":"paper","maxIterations":3,"qualityThreshold":9.0,"minImprovement":0.2,"humanInLoop":true,"llmProvider":"zhipuai","model":"glm-4.7-flash","svgWidth":800,"svgHeight":600},"input_content":"Sample input for session creation.","input_type":"text"}'
curl -s -X POST -H "Content-Type: application/json" -d "$payload" http://127.0.0.1:8796/api/autofigure/session/create | head -n 20 || true
echo
echo "Diagnostics finished."
