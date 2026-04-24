import os
import unittest


# Ensure cairo native libs are discoverable before importing backend app modules.
os.environ.setdefault("PKG_CONFIG_PATH", "/opt/homebrew/lib/pkgconfig")
os.environ.setdefault("DYLD_LIBRARY_PATH", "/opt/homebrew/lib")
os.environ.setdefault("LD_LIBRARY_PATH", "/opt/homebrew/lib")

from backend.app import app  # noqa: E402
import autofigure_routes  # noqa: E402


class OpenAICompatBackendTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        autofigure_routes.autofigure_sessions.clear()
        autofigure_routes.session_locks.clear()

    def _create_session(self, payload: dict) -> dict:
        response = self.client.post("/api/autofigure/session/create", json=payload)
        self.assertEqual(
            response.status_code,
            200,
            msg=f"create_session failed: {response.status_code} {response.get_data(as_text=True)}",
        )
        data = response.get_json()
        self.assertIsNotNone(data)
        self.assertIn("session_id", data)
        session_id = data["session_id"]
        self.assertIn(session_id, autofigure_routes.autofigure_sessions)
        return autofigure_routes.autofigure_sessions[session_id]

    def test_create_session_accepts_openai_messages_with_zai_alias(self) -> None:
        session = self._create_session(
            {
                "provider": "zai",
                "api_key": "k-zai",
                "base_url": "https://open.bigmodel.cn/api/paas/v4",
                "model": "glm-4.7-flash",
                "messages": [
                    {"role": "system", "content": "You are helpful"},
                    {"role": "user", "content": "draw a model pipeline"},
                ],
            }
        )

        self.assertEqual(session["config"]["llm_provider"], "zhipuai")
        self.assertEqual(session["config"]["base_url"], "https://open.bigmodel.cn/api/paas/v4")
        self.assertEqual(session["config"]["model"], "glm-4.7-flash")
        self.assertEqual(session["input_content"], "draw a model pipeline")

    def test_create_session_accepts_responses_input_array_with_zhipu_alias(self) -> None:
        session = self._create_session(
            {
                "provider": "zhipu",
                "api_key": "k-zhipu",
                "base_url": "https://open.bigmodel.cn/api/paas/v4",
                "model": "glm-4.7-flash",
                "input": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": "method section only"},
                        ],
                    }
                ],
            }
        )

        self.assertEqual(session["config"]["llm_provider"], "zhipuai")
        self.assertEqual(session["config"]["base_url"], "https://open.bigmodel.cn/api/paas/v4")
        self.assertEqual(session["config"]["model"], "glm-4.7-flash")
        self.assertEqual(session["input_content"], "method section only")

    def test_default_model_fallback_for_openai_compatible_providers(self) -> None:
        cases = [
            ("openai", "https://api.openai.com/v1", "gpt-4o-mini"),
            ("deepseek", "https://api.deepseek.com/v1", "deepseek-chat"),
            ("siliconflow", "https://api.siliconflow.cn/v1", "Qwen/Qwen2.5-72B-Instruct"),
        ]

        for provider, base_url, expected_model in cases:
            with self.subTest(provider=provider):
                session = self._create_session(
                    {
                        "provider": provider,
                        "api_key": f"key-{provider}",
                        "base_url": base_url,
                        "input_content": "hello",
                    }
                )
                self.assertEqual(session["config"]["llm_provider"], provider)
                self.assertEqual(session["config"]["base_url"], base_url)
                self.assertEqual(session["config"]["model"], expected_model)

    def test_custom_provider_with_arbitrary_endpoint(self) -> None:
        session = self._create_session(
            {
                "provider": "custom",
                "api_key": "k-custom",
                "base_url": "https://my-custom-endpoint.com/v1",
                "model": "my-custom-model",
                "input_content": "hello",
            }
        )
        self.assertEqual(session["config"]["llm_provider"], "custom")
        self.assertEqual(session["config"]["base_url"], "https://my-custom-endpoint.com/v1")
        self.assertEqual(session["config"]["model"], "my-custom-model")

    def test_start_generation_requires_api_key(self) -> None:
        session = self._create_session(
            {
                "provider": "zhipuai",
                "input_content": "paper content here",
            }
        )
        session_id = session["session_id"]

        start_response = self.client.post(f"/api/autofigure/session/{session_id}/start", json={})
        self.assertEqual(
            start_response.status_code,
            400,
            msg=f"unexpected start response: {start_response.get_data(as_text=True)}",
        )
        data = start_response.get_json() or {}
        self.assertEqual(data.get("code"), "API_KEY_REQUIRED")


if __name__ == "__main__":
    unittest.main()
