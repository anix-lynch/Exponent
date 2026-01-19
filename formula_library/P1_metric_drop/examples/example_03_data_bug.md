# Example 3: Data Bug

**Prompt:** "DAU dropped 15% today."

3 (data bug)

**Prompt:** "DAU dropped 15% today."

```text
1) Clarify
- DAU definition: unique users with 'app_open' event?
- Timezone cutoff? rolling 24h?

2) Data Check
- 'app_open' event missing from Android build?
- Pipeline delay today?
- Sampling changed?
=> If yes: measurement issue

6) Action
- Fix instrumentation/pipeline
- Recompute DAU using backup signal (sessions, server auth hits)
- Postmortem + add monitors for event volume anomalies
```