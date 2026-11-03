# 3.3 Constraints

These three P1 constraints bind every proposed design. The team must record and review any relaxation through its change-control process. [P1 requirements](requirements.md) · [Verification](verification.md)

### CON-01 · UTD NetID sign-in only

UTD NetID single sign-on is the only student sign-in mechanism. P1 attributes this to an assumed campus requirement. Q3 asks OIT whether the project may register and which attributes establish identity and provide an email address. Only the student's own verified session may create, list or cancel that student's watches.

P3 can exercise the identity boundary with synthetic principals while OIT advice is pending. A live pilot requires approved settings and claims. Replacing NetID with an email-verified account would require an approved baseline change. Verify the three protected operations signed out and as two different signed-in students, and inspect the registered identity-provider configuration. [Issue #9](https://github.com/PaperBagTrick/Study-Room-Sniper/issues/9)

### CON-02 · Read-only library access

The service may read permitted availability. It must never create, change or cancel a reservation or hold a student's library credentials. The constraint comes from the P1 team decision and the library reservation policy. Q1/Q2 concern the source and permission to automate reads. Students finish any booking on the library's own site.

The reader accepts only approved availability operations. A booking link transfers control to the student's browser. If the source changes or is withdrawn, pause live reads and use fixtures while the team reviews the impact. Verify the outbound operation log through matching, confirmation and cancellation, including an attempted unsupported operation against a stub. [Issue #10](https://github.com/PaperBagTrick/Study-Room-Sniper/issues/10)

### CON-03 · Zero cost to the team

All services used to build and run the project must cost the team nothing. This is a team budget decision. The design must account for hosting, storage, email and optional push, including retries and expected peak volume. A free tier can be exhausted even during a small pilot.

Record provider limits, account conditions and expected usage before enabling delivery. Under a hard quota, surface exhaustion and pause affected sends instead of allowing a paid overage. Waiting for quota renewal can violate an alert's delivery deadline and must be recorded under QR-01. Verify the configuration, expected volume, quota behavior and actual cost for the proposed pilot. [Issue #11](https://github.com/PaperBagTrick/Study-Room-Sniper/issues/11) · [Quota observations](spikes/availability/README.md)
