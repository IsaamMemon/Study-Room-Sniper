## 10 Plan to P3

### Milestones and working agreement

These dates are a proposed working schedule in Central time. The P1 document gives 8 November as the P2 deadline. The team still needs to confirm the P3 due date against the course calendar.

| Target | Owner from P1 | Output and completion condition |
| --- | --- | --- |
| Wed 4 Nov, 7:00–7:30 p.m. CT | Alexander, all owners | First proposed weekly meeting. Review the branch and open questions, assign a backup per item, and agree on the review and meeting cadence. |
| 4–6 Nov | Lee, Mayand | Ask the library and OIT Q1–Q4/Q6 through the team's normal channels. Pilot the survey, invite eligible students and report the real response count. Include dates, method and limitations. |
| 6–8 Nov | Henry, Arshan, Isaam | Independently walk both sequences, rerun the spike and review the assembled report. One teammate records a substantive PR review before merge. Alexander records the baseline decision. |
| First P3 week following P2 | Henry, Arshan | Detail the ownership and matching paths against a stub. Exercise the full-cycle batch and any fresh confirmation. Identify which failures require an approved requirement change. |
| Second P3 week | Mayand, Isaam | Compare measured provider acceptance, keyboard access, first-time task completion and free-tier quotas against §3. Start the 14-day availability observation as soon as a trial build is available. |
| P3 integration, before the confirmed course deadline | All owners, Isaam integrating | Each member commits their own accepted work. Resolve red checks or document approved deviations with issue, reviewer and commit links. |

**Cadence and channel.** Proposed team meeting every Wednesday at 7:00 p.m. CT for 30 minutes. The named asynchronous channel is GitHub Issues in `PaperBagTrick/Study-Room-Sniper`. Keep one thread per decision, post a short meeting summary in the active milestone issue, and use the pull request for artifact review. The owner proposes a resolution, the group votes if contested, and a tie or a 48-hour deadlock goes to the instructor or TA, as in P1.

### Risks carried forward

| Risk | Trigger | Response and owner |
| --- | --- | --- |
| R1 · source unavailable or changed | An approved anonymous read cannot return stable room, slot and capacity data. | Arshan keeps the fixture path and asks for a supported bulk feed. Alexander raises a change request if live FR-03/04 cannot be demonstrated. |
| R2 · rate or permission objection | The library objects, throttles requests or specifies a lower limit. | Lee records the terms. Arshan pauses live reads and recalculates the full read and confirmation budget before any restart. |
| R3 · NetID access | OIT cannot provide the required sign-in or permitted claims. | Lee records the decision. Alexander proposes a CON-01 change for review. Continue fixture-based identity checks in the meantime. |
| R4 · incomplete individual evidence | A milestone has no named owner, review, or authored work by its checkpoint. | Isaam asks the owner and backup to split the remaining work, records responsibility, and raises any proposed FR-14 or FR-08 deferral through change control. |
| R5 · late or unseen alerts | Fewer than 95 of 100 emails reach the service in 180 s, or students report the delay is unhelpful. | Arshan separates source, cycle-end batching and delivery delays. Mayand compares the result with survey evidence before proposing a revised threshold. |

**Repository and AI use.** Markdown specifications live in `docs/`. The controlled experiment and its result live in `docs/spikes/availability/`, and elicitation materials live in `docs/elicitation/`. Work branches use issue-numbered commits and a peer-reviewed PR into main. The P2 drafting session used OpenAI Codex for the written analysis, diagrams, fixture code, report assembly and repository checks. Checks included comparing requirement IDs to the tracked P1, rerunning the experiment and reviewing the rendered report. Human review and acceptance remain with the named owners.

## 11 Open questions

| Question | Evidence and interim decision | Who can close it |
| --- | --- | --- |
| Q1 · Supported availability source? | Public inventory exists. A text reader did not obtain timestamped slots for a supported feed. Use fixtures until a response establishes the endpoint, fields and granularity. | Library systems staff and Arshan |
| Q2 · Automated reads and alerts permitted? | Twenty requests per rolling minute is an internal ceiling. The library has not approved it. Live scheduled polling awaits written terms. | Library reservations staff and Lee |
| Q3 · NetID and allowed claims? | Design assumes a verified campus subject and email. Exact exchange, enrollment assurance and claim release require OIT confirmation. | OIT and Lee |
| Q4 · What does bookable mean for one student? | Match the library's free slot and listed capacity. The library decides personal eligibility when the student follows the link. | Library reservations staff and Henry |
| Q5 · Do the thresholds fit students' experience? | The survey asks about room need, three minutes, five Active watches, channel preference and what should happen after an alert. The watch remains Active under v0.1. No responses have been recorded. | Students and Mayand |
| Q6 · Applicable accessibility standard? | Carry WCAG 2.2 AA forward. The keyboard and screen-reader walks still require a review environment and participants. | OIT/accessibility contact and Mayand |

The privacy decision on push endpoints under QR-06 belongs with Q3. The delivery-provider quota and complete-cycle latency checks belong with R5. A technical observation in the spike closes neither policy question.

## 12 Baseline declaration

**Proposed v1.0 baseline as of 3 November 2026.** The candidate comprises this report, the editable specifications, the survey instrument and the reproducible availability spike. It preserves FR-01–FR-14, QR-01–QR-06 and CON-01–CON-03 from the tracked P1 baseline. It is offered for team review.

To adopt v1.0, each owner checks the sections assigned above, an independent member reviews the PR, and the change-control lead records the accepted merge commit and tag. Until that decision is recorded, v1.0 is a candidate. The original P1 signatures apply to v0.1 only.
