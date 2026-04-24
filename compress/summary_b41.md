Topic: Emergency context continuation (b41)
Summary:
- Objective: Finish two remaining tasks - in_progress Validate API endpoints with ZAI and OpenAI-compatible payloads; pending Oracle final architecture/review check.
- Context: Prior efforts established robust OpenAI payload normalization to support multiple content keys (input, content, prompt). Several session-create tests across ZAI/OpenAI showed successes when input_content was provided, but other shapes still produced Input content errors in this environment. A CI-backed end-to-end mock harness is planned to deterministically validate the start->generate path.
- Plan: (1) re-run six augmented payload tests to converge on deterministic results, (2) implement a CI mock end-to-end harness to validate end-to-end flows, (3) draft and publish Oracle final architecture brief + two-week sprint plan, (4) update payload docs with canonical fields and examples.
- Risks: environmental determinism of LLM backends; mitigated by CI mocks.
- Milestones: six-payload deterministic success; harness; Oracle brief; docs.
