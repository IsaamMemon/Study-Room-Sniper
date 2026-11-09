# 9 Traceability

Study Room Sniper · P2 · Owner: Isaam Memon

## 9.1 Extended traceability matrix

| Requirement | Use case | Analysis classes | Component(s) | QAS / ADR | Evidence |
| --- | --- | --- | --- | --- | --- |
| FR-01 | UC-01 | Student, Watch | Web Client, Watch Service, Watch Store | QAS-05 | 5.2.1 rows 7 to 12 |
| FR-02 | UC-01, UC-03 | Student | Identity Adapter, Watch Service | QAS-04; ADR-03 | 5.2.1 rows 1 to 4 |
| FR-03 | UC-02 | ReadCycle, Room, Slot | Cycle Coordinator, Availability Reader | QAS-01, QAS-03; ADR-02 | 5.2.2 rows 1 to 3; spike S-01 (pending) |
| FR-04 | UC-02 | Watch, Slot, Room | Match Engine | QAS-01; ADR-01 | 5.2.2 rows 4 and 5 |
| FR-05 | UC-02 | Slot, Room | Alert Dispatcher, Availability Reader | QAS-01 | 5.2.2 row 7 |
| FR-06 | UC-02 | Alert, Watch, Student | Alert Dispatcher | QAS-01 | 5.2.2 rows 8 to 10 |
| FR-07 | UC-02 | Alert, Room, Slot | Alert Dispatcher | QAS-01 | 5.2.2 rows 8 to 10 |
| FR-08 | UC-01, UC-02 | Watch, Alert | Web Client, Watch Service, Alert Dispatcher | ADR-01 | 5.2.1 row 7; 5.2.2 row 9 |
| FR-09 | UC-03 | Watch | Web Client, Watch Service | ADR-01 | 4.2 UC-03 steps 3 to 6 |
| FR-10 | UC-01, UC-03 | Student, Watch | Watch Service, Watch Store | QAS-04 | 5.2.1 rows 5 and 6; 4.2 UC-03 step 2 |
| FR-11 | UC-03 | Watch | Cycle Coordinator, Watch Service | ADR-01 | 4.2 UC-03 step 2 |
| FR-12 | UC-02 | Alert, Watch, Slot | Match Engine, Alert Dispatcher, Watch Store | QAS-01 | 5.2.2 row 6 |
| FR-13 | UC-01 | Student, Watch | Watch Service | ADR-01 | 5.2.1 row 9 |
| FR-14 | UC-04 (not analyzed) | ReadCycle | Health View, Availability Reader | QAS-02 | None yet |
| QR-01 | UC-02 | Alert, Slot, Watch | Cycle Coordinator, Availability Reader, Match Engine, Alert Dispatcher | QAS-01; ADR-01, ADR-02 | Spike S-01 (pending) |
| QR-02 | UC-02, UC-04 | ReadCycle | Cycle Coordinator, Availability Reader, Health View | QAS-02; ADR-04 | None yet |
| QR-03 | UC-01 | Watch | Web Client | QAS-05 | None yet (usability test planned) |
| QR-04 | UC-01, UC-03 | (screens only) | Web Client | QAS-05 | None yet (Q6 pending) |
| QR-05 | UC-02 | ReadCycle, Room | Availability Reader, Cycle Coordinator | QAS-03; ADR-02 | Spike S-01 (pending) |
| QR-06 | UC-01 | Student, Watch, Alert | Watch Store, Watch Service, Identity Adapter | QAS-04; ADR-03 | Deployment view 6.4 |
| CON-01 | UC-01, UC-03 | Student | Identity Adapter | ADR-03; QAS-04 | Q3 pending |
| CON-02 | UC-02 | Slot, Room | Availability Reader (read-only) | ADR-02 | Deployment view 6.4 (HTTPS GET only) |
| CON-03 | (all) | (none) | Application host, Database host | ADR-04, ADR-01 | None yet |

## 9.2 Gap analysis

| Gap | Items | What we did about it |
| --- | --- | --- |
| Requirements with no component | None. | Every requirement in 9.1 reaches at least one component; FR-14 is realized by the Health View and CON-03 by the two hosts. |
| Components with no requirement, QAS or ADR | None. | Every component in 6.3 answers to at least one use case, scenario or decision. |
| Use cases not analyzed (and why that is acceptable) | UC-04 Monitor service health | COULD priority (FR-14), one actor, one screen that reads data already analyzed (ReadCycle). It will be expanded in P3 if FR-14 is kept. |
