# 1. Introduction

Study Room Sniper helps an enrolled UT Dallas student find a study room at Eugene McDermott Library. Today a student who finds the rooms occupied must revisit the library calendar to see whether a cancellation or a lapsed hold has freed a slot. The student saves a date, time window and group size once. When a matching slot appears, the service sends a link to the library calendar. The student makes any reservation there.

This record carries the 18 October 2026 P1 requirements into the P2 analysis and design review for Team 4, Section 003. The course instructor, TA and team can use the stable IDs to follow each requirement into its analysis, design decision and proposed acceptance check. [P1 baseline](Study_Room_Sniper_P1.pdf) · [Constraint details](constraints.md) · [Verification](verification.md)

### Scope and vocabulary

The responsive web service covers the library's nine group study rooms and eight smart rooms. Students use NetID, manage their own watches, receive email, and can opt into browser push. Operators can inspect read health. The P1 scope excludes booking or altering reservations, the One Button Studio, other locations, SMS, native apps, predictions and room recommendations.

| Term | Meaning in this baseline |
| --- | --- |
| Watch | One student's saved date, time window and minimum group size. Its state is Active, Cancelled or Expired. An alert leaves the watch Active. |
| Slot and room | A slot is a library-published time interval for one room. The room's listed capacity determines whether the group will fit. |
| Bookable | Provisionally, the library shows the slot as free. Q4 asks whether a student's own reservation limits must also be considered. The library determines final eligibility when the student opens the link. |
| Match | A free slot on the requested date, wholly inside an Active watch's window, in a room with enough capacity. |
| Read cycle | One read-only sweep of all in-scope rooms. The request cap applies across the service, including reads that confirm a match. |
| Alert | Email describing matches for a student, with optional browser push. Delivery time and whether the student notices the alert are separate observations. |
| Operator | Team member who monitors the source reader and investigates failures. |

P1 draws on ISO/IEC/IEEE 29148:2018 for requirements-writing style (R1), the library inventory and policies (R2–R4), W3C WCAG 2.2 (R5), and the course syllabus and P1 template on Canvas (R6). The library statements below carry the P1 interpretation pending Q1–Q4. [R2, library calendar](https://libcal.utdallas.edu/) · [R3, reservation policy](https://library.utdallas.edu/about-the-library/reserve-a-study-room) · [R4, room policies](https://libcal.utdallas.edu/reserve/spaces/study-rooms) · [R5, WCAG 2.2](https://www.w3.org/TR/WCAG22/)

# 2. Overall description

The team controls the watch interface, watch state, periodic reader, matching, alert dispatch and operator view. The library owns room inventory, policy, availability and booking. OIT owns the NetID sign-in service. Email and web push providers deliver messages. The application never requests a student's library password.

| Stakeholder | Need and evidence status |
| --- | --- |
| Students | Set up a watch quickly on a phone, receive enough detail to act and stop alerts when plans change. P1 inferred these needs from student experience and library policy. Q5 calls for direct student evidence. |
| Students using assistive technology | Complete watch creation and watch management with keyboard or screen reader and receive information independent of color or sound. P1 references WCAG. Direct consultation and campus guidance remain open under Q6. |
| Library reservations staff | Keep library traffic within an acceptable rate and preserve fair access. P1 inferred this from published policies. The library's approval of the source and rate remains open. |
| UTD OIT | Approve NetID integration and the attributes a student project can receive. Q3 and Q6 require an OIT or campus accessibility response. |
| Team and operators | Work within a zero-cost budget and detect stale reads and failures. P1 identifies these as the team's own needs. |

### Assumptions and feasibility at P2

| P1 ID | Working assumption | Evidence and consequence |
| --- | --- | --- |
| A1 | A program can read timestamped slots without student credentials. | The public list identifies rooms. The lookup did not establish a supported slot feed. Until Q1 is answered, FR-03 and FR-04 can be demonstrated against fixtures. |
| A2 | The library permits automated reads at up to 20 requests/minute total. | The limit is a ceiling set by P1. Ask for the library's approved rate under Q2 and pause if requested. A lower rate may change achievable alert delay. |
| A3 | OIT approves NetID sign-in and supplies NetID and email. | Obtain approved attributes under Q3. If access is refused, changing CON-01 needs a change request. Email verification would lose the original enrollment assurance. |
| A4 | The 17-room inventory remains small, with at most 20 rooms anticipated. | The spike exercised 17 rooms. Future inventory and how many dates one response covers determine whether FR-03 fits QR-05. |
| A5 | Students notice an alert within a few minutes on a phone. | A simulated or real delivery timestamp cannot measure attention. Ask students under Q5 before revising channels or thresholds. |
| A6 | The library can supply a reliable listed capacity per room. | Confirm the source and reconcile all 17 room IDs. Dropping group-size matching would require a change to FR-01 and FR-04. |

The offline spike supports a shared reader under its fixture assumptions. Live operation depends on library access, OIT approval and measured provider delivery. No-cost plans have quotas, and 100 simulated recipients in one day could consume one candidate email plan's full daily allowance. These gates affect the P3 schedule. [Spike method and results](spikes/availability/README.md)

# 3. Specific requirements

The IDs, priorities and thresholds below carry forward P1. The use-case key is UC-01 create a room watch, UC-02 receive an alert, UC-03 manage watches, and UC-04 monitor service health. The acceptance column states what the reviewer should observe. [Step-by-step checks](verification.md) · [Design traceability](traceability.md)

### 3.1 Functional requirements

| ID and priority | Student or operator outcome | Acceptance and use case |
| --- | --- | --- |
| FR-01 · MUST | As a signed-in student, I can save a date within the next seven days, a time window and minimum group size so I can stop refreshing the calendar. | The saved watch displays all entered criteria. A date more than seven days ahead is refused with a message. UC-01. |
| FR-02 · MUST | As a student, I sign in with UTD NetID before I can create, see or cancel my watches. | Each signed-out action requires NetID sign-in. The action becomes available after successful sign-in. UC-01, UC-03. |
| FR-03 · MUST | While the library is open, the service reads availability for every in-scope room at least once every two minutes. | Against a reachable stub, the request log for a 60-minute run shows no room with a read gap above 120 seconds. UC-02. |
| FR-04 · MUST | As a student, I receive matches only for free slots on my date, fully inside my window and in a room that fits my group. | Release one fitting slot and one outside the window. Within one read cycle only the fitting slot is matched. UC-01, UC-02. |
| FR-05 · SHOULD | Before sending an alert, the service confirms that the matching slot is still bookable. | Withdraw a slot between discovery and confirmation. Its owner receives no alert for it. UC-02. |
| FR-06 · MUST | As a student, I receive email covering every match found in a read cycle. | Release a matching slot. The owning student's test inbox receives exactly one alert. UC-02. |
| FR-07 · MUST | I can identify the room and time from the alert and open the library booking page. | Received alert contains room name, slot start and end, and a working library booking link. UC-02. |
| FR-08 · SHOULD | I can choose browser push as an additional channel for a watch. | Release a match for each of two watches. The opted-in watch receives email and push, the other email only. UC-01, UC-02. |
| FR-09 · MUST | I can cancel an Active watch. | After cancellation the watch shows Cancelled, and a later matching release produces no alert. UC-03. |
| FR-10 · MUST | I can list my own watches and see Active, Expired or Cancelled status. | In a two-account check, each owner sees only their watches with the correct states. UC-01, UC-03. |
| FR-11 · MUST | When the watch window ends, the service marks it Expired and stops evaluating it. | Advance the clock past the end. Within five minutes it shows Expired. A later matching slot produces no alert. UC-02, UC-03. |
| FR-12 · MUST | A watch receives at most one alert for a given slot. | Keep one slot free across ten cycles. Its owner receives exactly one alert for that watch and slot. UC-02. |
| FR-13 · SHOULD | A student can hold at most five Active watches. | With five Active watches, attempting a sixth is refused with a message. UC-01. |
| FR-14 · COULD | As an operator, I can see the last successful availability read and the number of failed reads in the last hour. | Stop the stub for ten minutes. The timestamp freezes and failures rise above zero. Reads resume after restoration and failures age out of the rolling hour. UC-04. |

### 3.2 Quality requirements

| ID and priority | Requirement | Acceptance method |
| --- | --- | --- |
| QR-01 · MUST | At up to 200 Active watches, at least 95% of alerts reach the student's email service within 180 seconds of a slot becoming bookable. | Compare release timestamps with delivery logs over 100 scripted releases. At least 95 must meet the deadline. |
| QR-02 · SHOULD | The service is available at least 99% of library opening hours over a continuous 14-day trial. | Probe every five minutes and divide successful opening-hours checks by all scheduled opening-hours checks. |
| QR-03 · MUST | At least 90% of first-time users create a watch on a phone in under 90 seconds without help. | Moderate at least ten first-time UTD students, timing first screen to watch appearing in the list. At ten participants, at least nine must succeed. |
| QR-04 · MUST | Every screen used in UC-01 and UC-03 meets WCAG 2.2 Level AA with zero serious or critical violations. | Scan every screen and complete every step in both cases using keyboard-only and screen-reader walkthroughs. |
| QR-05 · MUST | Total traffic to the library reservation system stays at or below 20 requests per minute, independent of the number of Active watches. | Inspect the 24-hour request log with 200 Active watches, including confirmation and retry traffic. No minute may exceed 20. |
| QR-06 · MUST | The only personal data stored about a student are NetID, email address and watches. | Review full exports for three test accounts against those permitted categories. |

### 3.3 Constraints and baseline relationships

CON-01 governs student sign-in, CON-02 protects the library's reservation boundary, and CON-03 binds the project to free services. Their sources, effects and verification are documented separately. [Constraints](constraints.md)

FR-14 is the sole functional requirement for UC-04. FR-11 covers expiry discovered during alert processing as well as the list state seen by a student. FR-13 reaches the refusal flow in UC-01. The P2 matrix extends the original functional links to cover architecture, quality requirements and constraints. [Traceability matrix](traceability.md)
