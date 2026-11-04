## 7 Design rationale

Three limits shape the design: the library request budget, the time a student can wait for an alert, and the team's zero-cost budget.

### ADR-01 Keep one deployable and one background reader

**Choice.** Run the web interface and scheduled work as modules of one application using a private transactional store. The common store makes watch cancellation, ownership and alert claims visible to the worker. A single active scheduler owns the library request budget.

**Alternatives and cost.** Independently deployed web, polling and delivery services would allow separate scaling. They would also need a queue, shared rate coordination and recoverable messages between services. Browser polling would reduce server work, but each open tab would compete for the 20-request budget, and closing the browser would stop email watches. The proposed host has a single failure point and a restart can delay a cycle. Revisit if the 14-day QR-02 trial misses 99% or the platform cannot keep a worker awake at zero cost.

### ADR-02 Share room reads and budget confirmations

**Choice.** Poll rooms on a common schedule and match the results locally against all Active watches. Put every library request through the same rolling-minute limiter, including a fresh confirmation before each alert batch. Share confirmations across candidate watches for the same room when one read covers those slots. An unreadable confirmation suppresses the affected item. A later cycle may discover it again.

**Alternatives and cost.** Reading separately for each watch makes library traffic grow with the number of students. Reusing the old snapshot as final confirmation saves requests but misses a slot taken between discovery and sending. With one response covering the required horizon of one room, 17 rooms require at least 17 scheduled reads per 120 s. Confirming each room once more in that interval requires another 17 of the 40 available requests. Timing within each minute still matters. Under pressure, protect scheduled reads, defer excess confirmations, and count delayed alerts against QR-01. If the source requires one call per room per date, seven dates would require 119 scheduled reads per 120 s before any confirmation. Reopen the decision if Q1 identifies that contract or Q2 sets a lower cap.

### ADR-03 Keep a durable identity for each alert item

**Choice.** C4 confirms candidate slots through C3 and claims each eligible watch/slot pair once in S1 using the library room identifier and normalized slot start and end. A logical alert groups claimed items by recipient and cycle. Its email lists a room and time once even when two of that student's watches qualify. Push lists only items from opted-in watches. C5 records outcomes separately by channel and rechecks ownership, Active status and window end at dispatch. A delayed send or retry requires a fresh C3 confirmation. Cancelling a watch suppresses unsent items for that watch. A message already handed off to a provider cannot be recalled.

**Alternatives and cost.** An in-memory “already sent” set loses history on restart. Sending before recording leaves a crash window that can duplicate an email. Keep the item and attempt outcome durably, including a pending attempt before handing off. Retry a definite provider rejection at most three times within five minutes, with fresh checks. If a timeout or crash leaves acceptance unknown, reconcile using a provider receipt or idempotency key where supported. Otherwise record the unresolved attempt and suppress an automatic resend. This preserves FR-12 at the cost of a possible missed FR-06 delivery. Release an unsent item claim after a slot fails confirmation so a later genuine reopening remains eligible. Revisit if the provider cannot distinguish rejection from unknown acceptance often enough to meet QR-01.

### ADR-04 Bind every watch operation to a campus identity

**Choice.** Validate the UTD sign-in response in C1 and derive the owner in C2 from its verified subject. Store NetID, email and watch data. Keep operating logs free of student names, addresses, IPs, raw sign-in claims and full notification payloads. Associate deduplication records with the watch that generated them. Use role checks for the read-health view and keep health counters free of student data.

**Alternatives and cost.** Local passwords would require extra credentials and a change to CON-01. Trusting an owner ID supplied by the browser would let one student read or cancel another student's watch. NetID-only access depends on OIT approval and the claims OIT releases. Browser push ordinarily needs a stored endpoint and keys linked to the user, which QR-06 does not explicitly permit. Keep this delivery path gated pending a documented privacy decision or approved change. Email remains the required channel.

### 7.1 Trade-offs to revisit

| Pressure | What the choice protects | Cost the team must measure or resolve |
| --- | --- | --- |
| Faster discovery versus library load | One global budget caps scheduled reads, retries and rechecks. | A tighter library cap, paging or a long confirmation queue may push email past 180 s. |
| Delivery coverage versus duplicate messages | Durable item claims and per-channel receipts protect students from repeated alerts. | An ambiguous provider response can leave a student without an email until reconciled. |
| Independent scale versus zero cost | One host avoids a distributed queue and keeps the budget in one place. | Host sleep or downtime affects both the web interface and scheduled reads. |
| More delivery options versus minimal student data | Email works with the P1 data allowance. | Push needs an explicit decision on endpoints, keys and deletion before enabling it. |
