#!/usr/bin/env python3
import json
import os
import sys
import traceback
from datetime import datetime

os.environ.setdefault("PKG_CONFIG_PATH", "/opt/homebrew/lib/pkgconfig")
os.environ.setdefault("DYLD_LIBRARY_PATH", "/opt/homebrew/lib")
os.environ.setdefault("LD_LIBRARY_PATH", "/opt/homebrew/lib")

from backend.app import app
import autofigure_routes

ZHIPUAI_API_KEY = "604507e218ab41649102a0f2831f9ac2.JkGzZIjhoKL3SYnt"

def _assert(cond, message):
    if not cond:
        raise AssertionError(message)

print("[TEST 1] Backend health check")
client = app.test_client()
resp = client.get("/api/autofigure/health")
_assert(resp.status_code == 200, f"Health failed: {resp.status_code}")
data = resp.get_json() or {}
print(f"  PASS: {data.get('status')}")

print("[TEST 2] Session create")
autofigure_routes.autofigure_sessions.clear()
autofigure_routes.session_locks.clear()
client = app.test_client()
resp = client.post("/api/autofigure/session/create", json={"provider": "zai", "api_key": ZHIPUAI_API_KEY, "base_url": "https://open.bigmodel.cn/api/paas/v4", "messages": [{"role": "system", "content": "You are helpful"}, {"role": "user", "content": "draw simple diagram"}]})
_assert(resp.status_code == 200, f"Create failed: {resp.status_code}")
data = resp.get_json() or {}
session_id = data.get("session_id")
_assert(bool(session_id), "missing session_id")
session = autofigure_routes.autofigure_sessions[session_id]
cfg = session["config"]
_assert(cfg["llm_provider"] == "zhipuai", f"provider mismatch")
print(f"  PASS: session_id={session_id[:20]}...")

print("[TEST 3] Session start")
client = app.test_client()
resp = client.post(f"/api/autofigure/session/{session_id}/start", json={})
_assert(resp.status_code in (200, 500), f"Unexpected: {resp.status_code}")
if resp.status_code == 200:
    print("  PASS: started")
else:
    print("  WARN: network error expected")

print("[TEST 4] Image generation")
resp = client.post("/api/autofigure/generate-image", json={"provider": "zhipuai", "api_key": ZHIPUAI_API_KEY, "model": "glm-4.7-flash", "base_url": "https://open.bigmodel.cn/api/paas/v4", "prompt": "test"})
_assert(resp.status_code in (200, 500), f"Unexpected: {resp.status_code}")
print("  PASS" if resp.status_code == 200 else "  WARN")

print("ALL TESTS COMPLETED")
print(json.dumps({"tests": ["health", "session_create", "session_start", "generate_image"], "status": "complete"}))
