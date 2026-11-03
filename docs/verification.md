# Verification guide

Use the tracked P1 requirements as the acceptance baseline. This guide describes how to verify them and identifies the subset exercised by the P2 spike. Check live-dependent criteria after the matching source, identity or provider is approved. The [P2 trace](traceability.md) maps each check to its use case and design decision.

## Functional checks

Use a controllable library stub, a clock that can be advanced, two distinct student identities, an operator identity, and separate email and push sinks. Capture release, read, confirmation, dispatch and acceptance timestamps on the same clock. Keep test personal information synthetic.

| ID | Exercise | Pass condition |
| --- | --- | --- |
| FR-01 | Sign in and create a watch within the next seven days with a date, time window and group size. Try again with a date eight days ahead. | The list reflects each valid value. The out-of-horizon date is refused with a message. |
| FR-02 | Attempt create, list and cancel separately before and after signing in. | All three signed-out actions send the student to NetID. Each permitted action becomes available after a valid sign-in. |
| FR-03 | Keep the stub reachable for 60 minutes during simulated opening hours. Record each room's first, intermediate and last read. | Every in-scope room is covered, with no gap above 120 seconds, including coverage at the run boundaries. |
| FR-04 | Release a free slot on the watch date, wholly inside its window with enough capacity. Add wrong-date, partially overlapping and too-small controls. | Within one cycle the fitting slot matches and the controls do not. |
| FR-05 | Remove a candidate after discovery and before confirmation. | No alert for the removed slot reaches either sink. A different slot still free at confirmation remains eligible. |
| FR-06 | Release several matches across rooms during one cycle for one owner, plus a match for another owner. | The test inbox for each owner receives exactly one email covering their confirmed matches for that cycle. No other owner's data appears. |
| FR-07 | Inspect the delivered message and follow its link. | Each match lists room name, start and end times. The link opens the library booking page. |
| FR-08 | Enable push for one watch and leave another email-only. Release a distinct matching slot for each. | Both matches appear by email. Only the opted-in match appears in browser push. |
| FR-09 | Cancel an Active watch. After cancellation, release a slot that would match it. | The list shows Cancelled and no new alert for that watch reaches a sink. |
| FR-10 | Under each of two accounts, create, expire and cancel watches. Try to read or change the other owner's watch. | Each account sees only its own watches with correct status. Cross-owner requests reveal no watch details and change nothing. |
| FR-11 | Advance the clock past an Active watch's end. Release a matching slot after the end. | The watch becomes Expired within five minutes and no subsequent match produces an alert. |
| FR-12 | Keep a slot free across ten read cycles for a single watch. Repeat across a worker restart. | Exactly one logical alert covers the pair. A channel accepted before a retry is not resent. |
| FR-13 | With five Active watches, attempt a sixth. Cancel one, then submit another. Also race two creates for the fifth place. | The sixth is refused with a message. A place becomes available after cancellation. At most five are Active under contention. |
| FR-14 | Disable the stub for ten minutes, restore it, then advance the clock through the rolling one-hour failure window. | Last success freezes during the outage, failed reads rise above zero, and the figures recover as new successful cycles complete and old failures age out. |

## Quality and constraint checks

| ID | Evidence and acceptance threshold |
| --- | --- |
| QR-01 | Under up to 200 Active watches, compare 100 scripted opening times to acceptance timestamps at the student's email service. At least 95 must take 180 seconds or less. Include cycle-end batching, reconfirmation and actual service acceptance. |
| QR-02 | Probe every five minutes during published library opening hours for 14 consecutive days. Count missed probes as failures. At least 99% of scheduled opening-hours checks must succeed. |
| QR-03 | Time at least ten first-time UTD students on phones from the first screen to the new watch appearing in their list. At least 90% must finish in under 90 seconds without help. |
| QR-04 | Evaluate every screen in UC-01 and UC-03 against WCAG 2.2 AA. Require zero serious or critical automated findings and a complete keyboard-only and screen-reader walkthrough. Record manual findings as well as scan results. |
| QR-05 | With 200 Active watches for 24 hours, count every library request, including retries and confirmations. The maximum over any rolling 60 seconds must be at most 20. |
| QR-06 | Review complete data exports for three test students, including linked logs and delivery metadata. The only stored personal data allowed are NetID, email and watches. Resolve push endpoint retention before enabling that channel. |
| CON-01 | Inspect the configured identity provider and exercise all three protected actions. NetID is the sole student sign-in route. Record OIT approval and the attributes actually released. |
| CON-02 | Inspect adapter capabilities and all outbound requests on the stub, including cancellation. No operation creates, changes or cancels a reservation. The student's browser opens the external booking page. |
| CON-03 | Record proposed hosting, storage and delivery quotas, the account configuration, usage at pilot load and any invoice. The team must incur zero cost. |

## P2 evidence and issue index

The [controlled replay](spikes/availability/README.md) exercises the per-room read gap, rolling-minute traffic cap, match filtering, stale-slot suppression, deduplication during a single run and simulated delivery delay. A real provider, a full-cycle batch, restart recovery, NetID and human walkthroughs still require separate evidence.

The [issue tracker](https://github.com/PaperBagTrick/Study-Room-Sniper/issues) contained these titled requirements when checked on 3 November. QR-01 appears twice (#1 and #2), as does FR-05 (#16 and #17). Related records are QR-02 #3, QR-03 #4, QR-04 #6, QR-05 #7, QR-06 #8, CON-01–03 #9–11, FR-01–04 #12–15, FR-06 #18 and FR-10 #5. At that check FR-07–09 and FR-11–14 had no matching issue title. The requirements and checks above retain their IDs independently of issue numbering.
