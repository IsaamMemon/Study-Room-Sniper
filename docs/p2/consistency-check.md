# 5.3 Consistency cross-check

Study Room Sniper · P2 · Checked by: Isaam Memon

Compares the expanded use cases (4.2), the domain model (5.1) and the UC-01 / UC-02 sequence diagrams (5.2).

| Check | Result (pass, or what failed) | Fixed in |
| --- | --- | --- |
| K1 Every item in an actor column (4.2) is an attribute in the domain model (5.1) | Pass: all items appear as attributes of Student, Watch, Room, or Slot. | n/a |
| K2 Every object on a sequence diagram is a domain class, a declared interaction object or an external system | Failed at first: WatchManager and AvailabilityMonitor are not in 5.1. Other objects are domain classes or external systems. | 5.2 (a): both declared as interaction objects |
| K3 Every message on a sequence diagram corresponds to exactly one scenario-table row | Pass: 12 messages for UC-01 and 10 for UC-02, numbered as in the tables. | n/a |
| K4 Every non-trivial step in 5.2 (a) has at least one scenario-table row | Pass: each step named in (a) cites its rows. | n/a |
| K5 Every analyzed use case traces to at least one functional requirement | Pass: UC-01 to FR-01, FR-02, FR-10, FR-13; UC-02 to FR-03 to FR-08 and FR-12; UC-03 to FR-02, FR-09 to FR-11. | n/a |
| K6 The last messages of each diagram make the use case postcondition true | Pass: UC-01 ends with the saved watch shown as Active; UC-02 ends with the alert recorded (row 8) and delivered (row 10). | n/a |

## Verification notes

Checked K1–K6 on 8 November 2026 against the text of §4.2, §5.1 and §5.2 and the diagrams (Fig. 5.1, 5.2.1, 5.2.2). All six pass: message numbers, senders and receivers match the scenario tables row for row (12 for UC-01, 10 for UC-02), and each use case's traces match §4.2. Wording fixes: K1 now names Slot (UC-02's free slot maps to Slot.availability), K2 now allows external systems, and UC-02 row 5 now lists room capacity, which use-case step 2 relies on.
