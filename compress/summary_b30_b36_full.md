Topic: OpenFigure multi-provider context (b30-b36) - full snapshot

- (b30) UI and backend groundwork
  - ZAI integration touched SettingsModal; ZAI models exposed; fixed model options; default base URL wired for ZAI flows.
  - ImageGenSettings updated to recognize ZAI; provider defaults wired to ZHIPUAI_BASE_URL; UI hints reflect ZAI paths.

- (b31) Backend consolidation
  - OpenAI shim integrated; routing unified for OpenAI-compatible providers; per-session isolation enforced to prevent cross-session leakage.
  - Health endpoints confirmed; architecture kept provider-agnostic where possible.

- (b32) Diagnostics & docs
  - Diagnostics script added; payload templates added; OpenRouter shim implemented to stabilize provider expansion; docs updated accordingly.

- (b33) Validation results
  - Basic API payloads for ZAI and OpenAI validated; health checks OK; end-to-end requires live LLM responses or robust mocks for full workflow.

- (b34) Plan and next steps
  - Prepare fresh Oracle final architecture review session; outline and publish a 2-week sprint plan with milestones; end-to-end validation approach and rollout notes.

- (b35) OpenAI consolidation progress
  - Create canonical OpenAI surface; ensure per-session isolation; plan rollout.

- (b36) End-to-end test harness design
  - Design mocks for start/continue to enable CI validation; define acceptance criteria and reporting format.

This file serves as a consolidated record for continued work with minimal surface area.
