## 9 Traceability and gap analysis

For each requirement, the tables show where the behavior occurs, which component owns it, and how to check it. Component IDs C1–C6 and the shared store S1 appear in §6.

### 9.1 Functional requirements

| ID | Use case and analysis concept | Design owner | Decision | Evidence needed or available |
| --- | --- | --- | --- | --- |
| FR-01 | UC-01 · Student, Watch | C1, C2 | ADR-01 | Save a valid watch and reject a date beyond the seven-day horizon. |
| FR-02 | UC-01, UC-03 · Student, Watch | C1, C2 | ADR-04 | Exercise signed-out create, list and cancel against the OIT-approved NetID exchange. Q3 is open. |
| FR-03 | UC-02 · Room, ReadCycle | C3 | ADR-02 | §8 measures per-room gaps on fixtures. Q1 and Q2 govern the live source. |
| FR-04 | UC-01, UC-02 · Watch, Slot, Room | C2, C3, C4 | ADR-02 | Compare known matches with wrong time, date and capacity. The meaning of “bookable” awaits Q4. |
| FR-05 | UC-02 · Slot, AlertItem | C3, C4, C5 | ADR-02 | Remove a matching slot between its discovery and confirmation. Verify suppression. |
| FR-06 | UC-02 · Student, Alert, AlertItem, DeliveryAttempt | C4, C5, S1 | ADR-03 | Check a test inbox for all confirmed matches grouped by owner. §8 uses a simulated sink. |
| FR-07 | UC-02 · Room, Slot, Alert | C5 | ADR-03 | Inspect the name, both times and the library booking link in the received message. |
| FR-08 | UC-01, UC-02 · Watch, DeliveryAttempt | C1, C2, C5 | ADR-03, ADR-04 | Compare email-only and opted-in watches after the QR-06 subscription decision. |
| FR-09 | UC-03 · Student, Watch, AlertItem | C2, C4, C5, S1 | ADR-03, ADR-04 | Cancel before dispatch and check the final status and absence of new alerts. |
| FR-10 | UC-01, UC-03 · Student, Watch | C1, C2, S1 | ADR-04 | Two signed-in owners see only their own Active, Expired and Cancelled watches. |
| FR-11 | UC-02, UC-03 · Watch | C2, C4, C5 | ADR-01, ADR-03 | Advance past window end, confirm Expired within five minutes and suppress later sends. |
| FR-12 | UC-02 · Watch, Slot, AlertItem | C4, C5, S1 | ADR-03 | Hold one slot free across ten cycles. Include restart and ambiguous delivery in later checks. |
| FR-13 | UC-01 · Student, Watch | C2, S1 | ADR-01 | With four Active watches, submit two creates together. Only one may take the fifth place. |
| FR-14 | UC-04 · ReadCycle | C3, C6, S1 | ADR-01, ADR-02 | During a ten-minute source outage, last success freezes and the failure count rises. Restore the stub and check recovery. |

### 9.2 Quality requirements and constraints

| ID | Path and analysis concept | Design owner | Decision | Evidence needed or available |
| --- | --- | --- | --- | --- |
| QR-01 | UC-02 · Slot, Alert, DeliveryAttempt | C3, C4, C5 | ADR-02, ADR-03 | §8 measures simulated acceptance. A real email-service timestamp is still needed for QA-1. |
| QR-02 | UC-01 to UC-04 · Watch, ReadCycle | C1, C3, C6 | ADR-01 | Complete the 14-day opening-hours trial in QA-3. |
| QR-03 | UC-01 · Student, Watch | C1, C2 | ADR-01 | Time at least ten first-time UTD students on a phone under QA-4. |
| QR-04 | UC-01, UC-03 · Student, Watch | C1 | ADR-01 | Scan each screen and complete the keyboard and screen-reader walks in QA-4. Q6 is open. |
| QR-05 | UC-02 · Room, ReadCycle | C3 | ADR-02 | Count all outbound requests on the same clock. §8 exercises the proposed schedule. |
| QR-06 | UC-01 to UC-03 · Student, Watch, DeliveryAttempt | C1, C2, C5, S1 | ADR-03, ADR-04 | Inspect exports for three test accounts, including stored metadata. Resolve push endpoint retention. |
| CON-01 | UC-01, UC-03 · Student | C1, C2 | ADR-04 | Obtain OIT direction for NetID-only sign-in and authorized claims (Q3). |
| CON-02 | UC-02 · Room, Slot, ReadCycle | C3 | ADR-02 | Inspect allowed source requests. The student alone follows the separate library booking link. |
| CON-03 | All use cases · ReadCycle, DeliveryAttempt | C1-C6, S1 | ADR-01, ADR-03 | Demonstrate that hosting, storage, email and push fit approved zero-cost quotas at the intended load. |

### 9.3 Gaps and their consequences

1. **Live availability.** Fixture results are conditional on the amount of data one read returns and on available capacity metadata. Without an approved credential-free source and rate, FR-03, FR-04, QR-01 and QR-05 remain unverified against McDermott. Record the Q1/Q2 response and source shape before selecting a live schedule. Q4 separately determines whether a free slot is reservable by a particular student.
2. **Delivery and identity.** The spike sends after each room confirmation. A student matching more than one room may wait for the full cycle's email batch. At six seconds per room, the last of 17 reads starts 96 seconds after the first. Measure that wait, fresh confirmations and provider acceptance together before judging QR-01. An unknown provider outcome leaves FR-06 in tension with FR-12 (ADR-03). Obtain an OIT decision for FR-02 and CON-01. Keep FR-08 gated until QR-06 is resolved.
3. **Human and operating evidence.** The repository needs observed usability and accessibility outcomes, a sustained availability trial and measured operating quotas for QR-02 through QR-04 and CON-03. FR-14 remains the sole functional requirement of UC-04 and the first scope reduction proposed by P1 if time is short. Record any cut through change control.
