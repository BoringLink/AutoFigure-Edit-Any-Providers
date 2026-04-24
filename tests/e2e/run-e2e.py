import json
import os
import traceback

# Ensure cairo native libs are discoverable before backend app import.
os.environ.setdefault("PKG_CONFIG_PATH", "/opt/homebrew/lib/pkgconfig")
os.environ.setdefault("DYLD_LIBRARY_PATH", "/opt/homebrew/lib")
os.environ.setdefault("LD_LIBRARY_PATH", "/opt/homebrew/lib")

from backend.app import app
import autofigure_routes


def _assert(cond, message):
    if not cond:
        raise AssertionError(message)


def run_backend_e2e():
    autofigure_routes.autofigure_sessions.clear()
    autofigure_routes.session_locks.clear()

    client = app.test_client()

    # 1) create session via OpenAI-style payload + alias provider
    create_resp = client.post(
        "/api/autofigure/session/create",
        json={
            "provider": "zai",
            "api_key": "fake-zhipu-key",
            "base_url": "https://open.bigmodel.cn/api/paas/v4",
            "messages": [
                {"role": "system", "content": "You are helpful"},
                {"role": "user", "content": "draw training pipeline"},
            ],
        },
    )
    _assert(create_resp.status_code == 200, f"create failed: {create_resp.status_code} {create_resp.get_data(as_text=True)}")
    create_data = create_resp.get_json() or {}
    session_id = create_data.get("session_id")
    _assert(bool(session_id), f"missing session_id: {create_data}")

    session = autofigure_routes.autofigure_sessions[session_id]
    cfg = session["config"]
    _assert(cfg["llm_provider"] == "zhipuai", f"provider mismatch: {cfg['llm_provider']}")
    _assert(cfg["base_url"] == "https://open.bigmodel.cn/api/paas/v4", f"base_url mismatch: {cfg['base_url']}")
    _assert(cfg["model"] == "glm-4.7-flash", f"model mismatch: {cfg['model']}")
    _assert(session["input_content"] == "draw training pipeline", f"input extraction mismatch: {session['input_content']}")

    # 2) start session should reach provider call path (expected network error in sandbox)
    start_resp = client.post(f"/api/autofigure/session/{session_id}/start", json={})
    _assert(start_resp.status_code in (200, 500), f"unexpected start status: {start_resp.status_code}")

    if start_resp.status_code == 500:
        err = (start_resp.get_json() or {}).get("error", "")
        _assert("Connection error" in err or "Failed" in err, f"unexpected start error: {err}")

    # 3) generate-image route through openai-compatible zhipu endpoint
    image_resp = client.post(
        "/api/autofigure/generate-image",
        json={
            "provider": "zhipuai",
            "api_key": "fake-zhipu-key",
            "model": "glm-4.7-flash",
            "base_url": "https://open.bigmodel.cn/api/paas/v4",
            "prompt": "draw a neural network icon",
        },
    )
    _assert(image_resp.status_code in (200, 500), f"unexpected image status: {image_resp.status_code}")

    if image_resp.status_code == 500:
        err = (image_resp.get_json() or {}).get("error", "")
        _assert("open.bigmodel.cn" in err or "Image generation failed" in err, f"unexpected image error: {err}")

    return {
        "session_id": session_id,
        "create_status": create_resp.status_code,
        "start_status": start_resp.status_code,
        "image_status": image_resp.status_code,
    }


def main():
    try:
        result = run_backend_e2e()
        print(json.dumps({"ok": True, "result": result}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e), "trace": traceback.format_exc()}, ensure_ascii=False))
        raise


if __name__ == "__main__":
    main()
