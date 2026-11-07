<!-- @format -->

## 7 Design rationale

Three limits drive the design: the library's request budget, how long a student can reasonably wait for an alert, and the team's zero-cost budget.

### ADR-01 Keep one deployable and one background reader

**Choice.** Build the web interface and the scheduled work as modules inside a single application that uses a private transactional store. Because the store is shared, the worker can see watch cancellations, ownership and alert claims. One active scheduler holds the library request budget.

**Alternatives and cost.** Deploying web, polling and delivery services separately would let each scale on its own. It would also call for a queue, shared rate coordination and recoverable messages between the services. Polling from the browser would cut server work, but every open tab would draw on the same 20-request budget, and closing the browser would end email watches. The proposed host is a single point of failure, and a restart can hold up a cycle. Revisit this if the 14-day QR-02 trial falls short of 99% or if the platform cannot keep a worker awake at zero cost.

### ADR-02 Share room reads and budget confirmations

**Choice.** Poll rooms on one common schedule and match the results locally against every Active watch. Route every library request through the same rolling-minute limiter, including the fresh confirmation made before each alert batch. When a single read covers the slots in question, share one confirmation across all candidate watches for that room. If a confirmation cannot be read, the affected item is suppressed, and a later cycle may find it again.

**Alternatives and cost.** Reading separately for each watch makes library traffic rise with the number of students. Reusing the earlier snapshot as the final confirmation saves requests but misses any slot taken between discovery and sending. If one response covers the required horizon for a room, 17 rooms need at least 17 scheduled reads every 120 s. Confirming each room one more time in that interval takes another 17 of the 40 available requests. Timing within each minute still matters. Under pressure, protect scheduled reads, put off excess confirmations, and count delayed alerts against QR-01. If the source needs one call per room per date, seven dates would need 119 scheduled reads per 120 s before any confirmation. Reopen this decision if Q1 identifies that contract or Q2 sets a lower cap.

### ADR-03 Keep a durable identity for each alert item

**Choice.** C4 confirms candidate slots through C3 and claims each eligible watch/slot pair once in S1, using the library room identifier and the normalized slot start and end. A logical alert groups the claimed items by recipient and cycle. Its email lists each room and time once, even if two of that student's watches qualify. Push lists only items from opted-in watches. C5 records outcomes separately for each channel and, at dispatch, rechecks ownership, Active status and the window end. A delayed send or a retry needs a fresh C3 confirmation. Cancelling a watch suppresses that watch's unsent items. A message already handed to a provider cannot be recalled.

**Alternatives and cost.** An in-memory "already sent" set loses its history on restart. Sending before recording leaves a crash window in which an email could be duplicated. Instead, store the item and the attempt outcome durably, including a pending attempt recorded before the handoff. Retry a definite provider rejection up to three times within five minutes, with fresh checks each time. If a timeout or crash leaves it unclear whether the provider accepted the message, reconcile with a provider receipt or idempotency key where one is supported. Otherwise, record the unresolved attempt and suppress any automatic resend. This upholds FR-12 at the price of a possibly missed FR-06 delivery. Release an unsent item's claim once its slot fails confirmation, so a later genuine reopening stays eligible. Revisit this if the provider cannot tell a rejection from an unknown acceptance often enough to meet QR-01.

### ADR-04 Bind every watch operation to a campus identity

**Choice.** C1 validates the UTD sign-in response, and C2 derives the owner from its verified subject. Store the NetID, email and watch data. Keep operating logs free of student names, addresses, IPs, raw sign-in claims and full notification payloads. Tie each deduplication record to the watch that produced it. Use role checks for the read-health view, and keep health counters free of student data.

**Alternatives and cost.** Local passwords would add credentials and require a change to CON-01. Trusting an owner ID sent by the browser would let one student read or cancel another student's watch. Relying on the NetID alone depends on OIT approval and on which claims OIT releases. Browser push usually needs a stored endpoint and keys tied to the user, which QR-06 does not explicitly allow. Keep this delivery path gated until there is a documented privacy decision or an approved change. Email remains the required channel.

### 7.1 Trade-offs to revisit

| Pressure                                          | What the choice protects                                                                 | Cost the team must measure or resolve                                                       |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Faster discovery versus library load              | A single global budget caps scheduled reads, retries and rechecks.                       | A tighter library cap, paging or a long confirmation queue could push email past 180 s.     |
| Delivery coverage versus duplicate messages       | Durable item claims and per-channel receipts keep students from getting repeated alerts. | An ambiguous provider response can leave a student without an email until it is reconciled. |
| Independent scale versus zero cost                | One host avoids a distributed queue and keeps the budget in one place.                   | Host sleep or downtime hits both the web interface and the scheduled reads.                 |
| More delivery options versus minimal student data | Email works within the P1 data allowance.                                                | Push needs an explicit decision on endpoints, keys and deletion before it is enabled.       |
