// Lightweight E2E runner for AutoFigure multi-provider canonical payloads
// This is a scaffold. Replace actual HTTP calls with CI-mediate mocks in CI.

const fetch = require('node-fetch');

// Base URLs (adjust to your local dev environment)
const BACKEND_BASE = process.env.BACKEND_BASE_URL || 'http://localhost:8796';

// Canonical payload shapes (placeholders, replace with real values in your environment)
const payloads = [
  { provider: 'zhipuai', base_url: 'https://open.bigmodel.cn', model: 'glm-4.7-flash', input_content: 'Sample prompt A', session_id: 'sess-zai-1' },
  { provider: 'zhipuai', base_url: 'https://open.bigmodel.cn', model: 'glm-4.7-flash', input_content: 'Sample prompt B', session_id: 'sess-zai-2' },
  { provider: 'zhipuai', base_url: 'https://open.bigmodel.cn', model: 'glm-4.7-flash', input_content: 'Sample prompt C', session_id: 'sess-zai-3' },
  { provider: 'openai', base_url: 'https://api.openai.com/v1', model: 'gpt-4', input_content: 'Sample prompt D', session_id: 'sess-openai-1' },
  { provider: 'openai', base_url: 'https://api.openai.com/v1', model: 'gpt-4', input_content: 'Sample prompt E', session_id: 'sess-openai-2' },
  { provider: 'openai', base_url: 'https://api.openai.com/v1', model: 'gpt-4', input_content: 'Sample prompt F', session_id: 'sess-openai-3' },
  { provider: 'custom', base_url: 'https://custom-api.example.com/v1', model: 'custom-model-v1', input_content: 'Sample prompt custom', session_id: 'sess-custom-1' },
];

async function createSession(p) {
  // You may need to adjust endpoint path to your actual API
  const res = await fetch(`${BACKEND_BASE}/api/autofigure/session/create`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' , 'Accept': 'application/json' },
    body: JSON.stringify({ provider: p.provider, base_url: p.base_url, model: p.model, input_content: p.input_content, session_id: p.session_id })
  });
  return res.json();
}

async function startSession(id, p) {
  const res = await fetch(`${BACKEND_BASE}/api/autofigure/session/${id}/start`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: p.model, input_content: p.input_content })
  });
  return res.json();
}

async function generateImage(id, p) {
  const res = await fetch(`${BACKEND_BASE}/api/autofigure/generate-image`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ session_id: id, model: p.model, input_content: p.input_content, provider: p.provider })
  });
  return res.json();
}

async function run() {
  for (const p of payloads) {
    try {
      const c = await createSession(p);
      console.log('Create session response:', c);
      if (c?.session_id) {
        const s = await startSession(c.session_id, p);
        console.log('Start response for', c.session_id, s);
        const g = await generateImage(c.session_id, p);
        console.log('Generate image response for', c.session_id, g);
      }
    } catch (err) {
      console.error('E2E step failed for payload:', p, err);
    }
  }
}

run().catch(e => console.error('E2E runner failed', e));
