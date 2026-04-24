AutoFigure - Two-week Sprint Plan for Multi-Provider Integration

Objective
- Deliver a unified provider surface with deterministic payload handling (ZAI, OpenAI, and future providers) and establish a CI-end-to-end harness for deterministic validation.

Milestones (14 days)
- Day 1-2: Finalize Oracle architecture decisions and publish artifact (docs/Oracle_final_architecture.md).
- Day 2-4: Implement provider adapter scaffold in backend; implement canonical payload extraction utility.
- Day 3-5: Extend LLM_PROVIDER enum to include zhipuai with base_url mapping and OpenAI shim compatibility.
- Day 4-6: Implement per-session config persistence and start/continue paths; ensure security/isolation of api_key per session.
- Day 5-7: Implement generate-image path via provider adapters; ensure both ZAI and OpenAI shapes work via shim.
- Day 6-8: Build CI mock end-to-end harness; create deterministic end-to-end tests for at least one ZAI and one OpenAI session.
- Day 8-10: Run unit and integration tests; fix defects; validate payload normalization with 6 canonical payload shapes.
- Day 9-11: Documentation updates for canonical payload shapes; write usage examples.
- Day 11-12: Prepare rollback plan and kill-switch criteria; ensure observability and health endpoints.
- Day 12-13: Stakeholder review; incorporate feedback.
- Day 14: Finalize PRs, hand off to deployment.

Success criteria
- All six canonical payload shapes validated in CI and on real environment where possible.
- Oracle architecture approved with a clear two-week sprint plan and milestones.
- CI mock-end-to-end harness functioning and demonstrated end-to-end path deterministically.

Risks
- CI harness readiness; mitigations include staged rollout and clear fallback paths.
- Provider adapter complexity; mitigations include shim architecture and per-provider tests.
