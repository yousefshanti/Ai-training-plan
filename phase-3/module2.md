## 1. User Story

**As a** homeowner with solar panels, **I want** an AI agent to alert me when my system produces less than expected for the current weather, **so that** I can fix faults early and avoid losing energy and money.

## 2. Acceptance Criteria

1. **Given** clear skies and output 25% below expected for 2 hours, **when** the agent checks, **then** an alert is sent within 15 minutes.
2. **Given** a drop caused by clouds, **when** the agent checks, **then** no alert is sent.
3. **Given** any alert, **then** it shows a confidence level and a short reason.
4. **Given** an alert, **when** the user marks it "False alarm", **then** the feedback is saved for retraining.
5. **Given** no data for 60 minutes in daylight, **then** the user gets a "Connection lost" notice instead of a fault alert.

## 3. AI‑Specific Considerations

**Low confidence:** High (≥ 80%) sends an alert; Medium (50–79%) is monitored for 3 days before alerting; Low (< 50%) is logged only.

**Override:** The user can mark alerts as "Confirmed" or "False alarm", snooze them, or adjust sensitivity.

**Transparency:** Each alert shows the confidence score, expected vs. actual output, and a one‑line reason.

**Fallback / Human‑in‑the‑loop:** Simple rules run if the model or data fails; critical faults are escalated to a technician, and the agent never changes system settings itself.
