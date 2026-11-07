<!-- @format -->

## 0 Revision and contribution record

Team 4, Section 003 · CE/CS/SE 3354 · 3 November 2026

| Revision                    | Record                                                                                                                                        | Changes                                                                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| v0.1 · 18 October           | [P1 proposal](https://github.com/PaperBagTrick/Study-Room-Sniper/blob/0ad8db1651e596903e6688aca1606540d964b289/docs/Study_Room_Sniper_P1.pdf) | Set out the room watch, the alert conditions, 23 requirements and four use cases.                                                 |
| v1.0 candidate · 3 November | [P2 pull request #19](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19)                                                             | Carries the same requirements through the design. Adds a polling experiment, a student survey and a plan for testing the service. |

### Response to P1 feedback

| Rubric item                           | Changes in P2                                                                                                                                                                      | Next step                                                                                                       |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| C1 · Need and feasibility · 6.5/8     | The survey asks what students did the last time they couldn't find a room. The spike measures how often a single reader can check 17 rooms and how long an alert takes.            | Pilot the survey with at least ten enrolled students. Ask the library which source and read rate it supports.   |
| C2 · Requirements · 10/10             | The acceptance checks keep the stub tests and numerical thresholds. Section 8 reports results for the request cap and the simulated alert delay.                                   | Measure the full delay at a test mailbox. Run the timed watch-creation task and the accessibility walkthroughs. |
| C3 · Use cases and traceability · 8/8 | UC-01 and UC-02 now have scenario tables and sequence diagrams. UC-03 follows a student through cancellation. Section 9 links all 23 IDs to the design.                            | Ask a teammate to trace one cancellation and one alert from the student's action to the recorded outcome.       |
| C4 · Team plan and repository · 3.5/6 | The report, the editable sections and the replay now sit together in PR #19. Section 10 proposes a Wednesday meeting and GitHub Issues for team decisions.                         | Each member commits their own section or findings and asks a teammate to review the change.                     |
| C5 · Individual contribution · 4/8    | The student survey and its collection instructions are in [the survey commit](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/28cad858389b412f6399438f779a350c804a76bb). | Record the pilot dates, the response counts and any change students suggest to the watch settings.              |

The P1 team score was **28/32**.

### P2 change evidence

Halogen419 opened [PR #19](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19) on 3 November with the five commits below.

| Commit                                                                                                          | Issue | Files and decisions                                                                 |
| --------------------------------------------------------------------------------------------------------------- | ----- | ----------------------------------------------------------------------------------- |
| [`b4a7b98`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/b4a7b98d1980640afa08ba2a5d6540dbd320e0f2) | #14   | Availability replay, its output and instructions for reproducing it.                |
| [`d0f955c`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/d0f955cffbe851089b370e2a44fdd4585d2be120) | #15   | Use cases, five diagrams, four architecture decisions and requirement traceability. |
| [`62dd643`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/62dd6434b94f5e09dbcf4d610e0bbdd8262fa7be) | #12   | Requirements, constraints and the acceptance checks for each.                       |
| [`28cad85`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/28cad858389b412f6399438f779a350c804a76bb) | #4    | Survey questions, collection instructions, working agreement and P3 schedule.       |
| [`0e1a232`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/0e1a232d8ac8d843ea9388b8b2d520442d4a2805) | #4    | P2 report, contribution record and README.                                          |

### Team responsibilities

The P1 roles continue through the review. The proposed tasks below show who handles each follow-up. Completed changes are logged in the [PR commit history](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19/commits).

| Member         | Area                       | Next contribution                                                                                                     |
| -------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Alexander Eng  | Change control             | Log the review decisions and the commit the team accepts as v1.0.                                                     |
| Arshan Khimani | Feasibility                | Compare what the library officially supports in a response against the fields and request budget used in the replay.  |
| Lee Baillard   | Elicitation                | Summarize the replies from the library and OIT, with dates and the requirement IDs they affect.                       |
| Mayand Dhami   | Quality and accessibility  | Pilot the survey, fix any unclear questions and publish the aggregate counts.                                         |
| Henry McGahan  | Use cases and traceability | Walk through a watch that is cancelled between matching and dispatch. Check the sequence and the trace against FR-09. |
| Isaam Memon    | Risk and integration       | Rerun the spike from a clean checkout and review the assembled report.                                                |
