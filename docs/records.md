## 0 Revision and contribution record

**Document status.** P2 analysis and high-level design, v1.0 candidate, 3 November 2026. Team 4, Section 003, CE/CS/SE 3354. The repository version of P1 at commit `0ad8db1` supplies the v0.1 requirements, IDs and use-case names.

| Revision | Evidence | Change |
| --- | --- | --- |
| P1 v0.1, 18 Oct | [P1 in the baseline tree](https://github.com/PaperBagTrick/Study-Room-Sniper/blob/0ad8db1651e596903e6688aca1606540d964b289/docs/Study_Room_Sniper_P1.pdf) | Proposal, acceptance criteria and four initial use cases. The instructor's review describes a different, earlier repository state at the submission deadline. |
| P2 v1.0 candidate, 3 Nov | [Pull request #19](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19) · [commit history](https://github.com/PaperBagTrick/Study-Room-Sniper/commits/docs/p2-analysis-design) | Preserves the 23 requirement IDs. Adds expanded use cases, five analysis/design diagrams, four decisions, the measured spike, survey instrument and P3 plan. |

### Response to P1 feedback

| Instructor finding | P2 response | Evidence still needed |
| --- | --- | --- |
| C1 · 6.5/8. Establish student need and technical feasibility. | Added a survey that asks enrolled students about recent attempts to reserve a McDermott room. The availability study distinguishes a public inventory from a supported feed and includes a reproducible latency experiment (§8). | At least ten student responses, the library's supported read contract, and permission for the intended rate. |
| C2 · 10/10. Precise stub tests and measurable quality thresholds. | Preserved the 14 functional requirements, six quality requirements and three constraints. The acceptance guide separates simulated observations from tests that need a provider or people. | Human usability and accessibility checks, provider acceptance evidence and the 14-day trial. |
| C3 · 8/8. Initial use cases and traceability. | Expanded UC-01 and UC-02, added the cancellation walkthrough, and mapped all 23 IDs to concepts, components and decisions in §9. | One independent member review of the analysis and the trace. |
| C4 · 3.5/6. Deadline tree lacked the cited commits, PRs and documents. Meeting cadence and channel were missing. | Kept the original P1 intact. The review branch contains the actual source files and spike. §10 specifies a proposed meeting time, a named channel and the evidence expected from each owner. | Each teammate must commit their own substantive follow-up and obtain another member's review. Later artifacts do not establish what was present at the P1 deadline. |
| C5 · 4/8. The individual commit and survey draft cited in P1 were absent. | Added a dated survey instrument and collection protocol under `docs/elicitation/`. Git identifies the account that added this draft. | Mayand can pilot and revise the instrument in a personal commit, then publish aggregate results and a review link. The P1 individual attribution remains unsupported. |

The instructor awarded **28/32 for the team portion**. Work completed for P2 is recorded against its actual revision. Dates and repository references from the original individual claims have not been reused as proof.

### P2 change evidence

| Account | Revision | Artifact a reviewer can inspect |
| --- | --- | --- |
| Halogen419 | [`b4a7b98`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/b4a7b98) | Runnable availability replay, observed JSON and reproduction instructions. Issue #14. |
| Halogen419 | [`d0f955c`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/d0f955c) | Three use cases, five diagrams, four decisions and the extended trace. Issue #15. |
| Halogen419 | [`62dd643`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/62dd643) | Carried-forward requirements, constraints and acceptance methods. Issue #12. |
| Halogen419 | [`28cad85`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/28cad85) | Survey draft, elicitation record, P3 milestones and working agreement. Issue #4. |
| Halogen419 | [`0e1a232`](https://github.com/PaperBagTrick/Study-Room-Sniper/commit/0e1a232) | Integrated P2 PDF, feedback record and repository guide. Issue #4. |

Halogen419 opened [pull request #19](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19) on 3 November to review these changes against `main`. The conversation and review history record any subsequent teammate feedback and baseline decision.

### Individual evidence ledger

| P1 owner and area | P2 evidence that a reviewer can verify | Next individually attributable action |
| --- | --- | --- |
| Alexander Eng · change control | P1 repository history records four commits under Alexander Eng. Individual P2 work awaits an authored change. | Record review decisions and resolve baseline approval in the PR. |
| Arshan Khimani · technical feasibility | The spike is present on the P2 branch. Its Git author is Halogen419. | Review the harness and commit a source-contract check when the library responds. |
| Lee Baillard · elicitation | A collection protocol exists. No stakeholder reply is recorded. | Submit a dated summary of actual library and OIT replies. |
| Mayand Dhami · quality and accessibility | This AI-assisted change was prepared for the requester under GitHub account Halogen419. The survey draft is now inspectable. | Commit pilot revisions and actual survey counts under the student's own account. |
| Henry McGahan · use cases and trace | The review branch contains the analysis and trace. Independent authorship has not been claimed. | Walk one alternate flow end to end and commit any corrections. |
| Isaam Memon · risk and integration | The risk register and PDF are included for review. | Rerun the spike, inspect the integration, and record an independent review. |

No team vote, teammate approval, survey response, instructor acceptance or retroactive signature is recorded here. The PR conversation and Git history are the evidence for subsequent work.
