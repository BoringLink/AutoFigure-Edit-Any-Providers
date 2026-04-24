# OpenAI API Compatibility Upgrade Plan (AutoFigure Backend + Frontend)

## 1. Current State Assessment

Backend and frontend are now aligned to a unified "OpenAI-compatible provider" model.

### Backend
- `POST /api/autofigure/session/create`
  - Accepts canonical payload and OpenAI-style payload variants.
  - Normalizes:
    - provider: `provider`, `llm_provider`, `config.llmProvider`, aliases (`zai` -> `zhipuai`)
    - base URL: top-level or nested `base_url/baseUrl`
    - model: top-level or nested `model`
    - input text:
      - `input_content`, `input`, `content`, `prompt`
      - OpenAI-style `messages[*].content` (text parts)
      - Responses-like `input` array of message objects
- Session start path applies provider runtime config consistently.
- Image generation endpoint (`/api/autofigure/generate-image`) routes OpenAI-compatible providers through one compatible path.
- Fixed backend syntax/runtime blocker (`IndentationError`) in image generation section.

### Frontend
- Provider metadata includes `zhipuai` with default base URL:
  - `https://open.bigmodel.cn/api/paas/v4`
- Default AutoFigure config now initializes Zhipu base URLs/models.
- Settings and beautification flows now use provider default base URL directly (no hardcoded `/chat/completions` append).
- Frontend can correctly choose ZhipuAI in layout, methodology, enhancement LLM, and image generation settings.

## 2. Compatibility Target

### OpenAI-Compatible Providers
Unified in backend and generator/enhancer:
- `openai`
- `zhipuai`
- `openrouter`
- `deepseek`
- `siliconflow`
- `bianxie` (legacy-compatible endpoint family)

### Zhipu Target Endpoint
- Recommended base URL:
  - `https://open.bigmodel.cn/api/paas/v4`

## 3. Key Upgrade Work Completed

1. Backend payload normalization
- Added extraction/normalization utilities for provider/base_url/model/input content.
- Reduced payload-shape fragility and "Input content is required" false negatives.

2. Backend provider runtime wiring
- Centralized provider-to-runtime config application.
- Removed duplicated/contradictory provider branches in session start flow.

3. SDK provider support expansion
- Extended generator/config/enhancer to treat OpenAI-compatible providers as first-class.

4. Frontend provider consistency
- Ensured provider switch updates base URL deterministically.
- Added clearer model/base URL placeholders for OpenAI and Zhipu.

## 4. Verification Summary

- Backend syntax verification: `python3 -m py_compile` passed for modified Python modules.
- Frontend type verification: `npx tsc --noEmit` passed.
- Existing repo lint baseline still contains unrelated issues; not introduced by this upgrade.

## 5. Remaining Recommendations

1. Add API-level regression tests
- Add tests for all accepted create-session payload shapes:
  - canonical config payload
  - top-level OpenAI-like payload
  - `messages`/`input` array payload variants

2. Add live smoke tests (optional in CI, required in staging)
- Validate real Zhipu key + model + endpoint with:
  - session create
  - session start (layout generation)
  - generate-image

3. Document model allowlist
- Maintain recommended model list per provider in docs/UI hints to reduce runtime trial-and-error.
