# 10.3 Risks (updated)

Study Room Sniper · P2 · Owner: Isaam Memon (risk and integration lead)

| Risk | Status since P1 | Likelihood / impact | Mitigation and owner |
| --- | --- | --- | --- |
| R1: Library availability cannot be read by a program, or changes format (A1) | Open / in progress via Spike S-01 | Medium / High | Arshan Khimani runs the spike. If it fails, re-scope via change control to demonstrate against recorded sample data. |
| R2: Library or OIT objects to automated reading (A2) | Open | Low / High | Lee Baillard contacts the library (Q2). QR-05 caps the request rate at 20 req/min; reading is paused immediately if requested. |
| R3: NetID SSO cannot be used by a student project (A3) | Open | Medium / Medium | Lee Baillard inquires with OIT (Q3). If refused, Alexander Eng raises a change request to CON-01 to permit email-verified accounts. |
| R4: Members unavailable around midterms | Active monitoring | Medium / High | Isaam Memon reviews progress weekly; every task has a named backup recorded in its issue. If behind, drop FR-14 then FR-08 via change control. |
| R5: Alerts arrive too late or sit unseen (A5, QR-01) | Under verification | Medium / Medium | Arshan Khimani measures alert delay with scripted releases. Mayand Dhami revises the threshold based on survey evidence if needed. |
| R6: Free-tier hosting limits (idle sleep, quotas) stop the 2-minute read cycle (QR-02, CON-03, ADR-04) | New in P2 | Medium / High | Isaam Memon checks the chosen provider's idle and quota rules before the build starts. If a limit blocks the cycle, Arshan Khimani raises a change request to QR-02 or moves to another free tier. See [free-tier-notes.md](free-tier-notes.md). |
