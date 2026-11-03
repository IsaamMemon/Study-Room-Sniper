# Can the reader find a free slot in time?

P1 leaves two questions coupled. Can the library supply credential-free, timestamped availability (A1), and can one shared reader confirm matches quickly enough without exceeding the library request budget (FR-03, FR-05, QR-01, QR-05)?

## What the public pages showed

On 3 November 2026, an unauthenticated web-text lookup of the library index showed nine group rooms and eight smart rooms. Following its links yielded HTTP 429 for the group view, a retrieval cache miss for the all-rooms view, and a calendar legend with no timestamped slot rows in the retrieved Smart Rooms page. These observations establish the public inventory. They leave availability access and the library's permitted read rate open. The group view was not retried. [Library index](https://libcal.utdallas.edu/) · [Group view](https://libcal.utdallas.edu/spaces?gid=6673&lid=3972) · [Smart Rooms view](https://libcal.utdallas.edu/spaces?lid=4255) · [All rooms](https://libcal.utdallas.edu/allspaces)

## Reproduce the experiment

Run from this directory with Python 3.10 or later. The program uses a virtual clock, the standard library and fictional room availability. It prints JSON and exits with an error on an unexpected recipient, missed or duplicate pair, stale send or baseline threshold failure. Compare stdout with [the recorded run](result.json).

```sh
python replay.py
```

The service runs for 24 simulated hours with 17 open rooms and 200 Active watches. Five waves each release 20 slots at once. Every persistent slot has an eligible owner and a second watch whose group is too large. A 101st slot disappears between discovery and confirmation. The reader visits one room every six seconds and can read that same room three seconds later to confirm all new candidates together. Already-alerted pairs remain in memory for the run.

| Measurement | Observed in the replay |
| --- | ---: |
| Scheduled room polls / extra confirmation reads | 14,400 / 86 |
| Longest gap between consecutive polls of the same room | 102 s |
| Peak requests in any rolling 60 s, confirmations included | 20 |
| Eligible persistent watch/slot pairs alerted / fleeting candidates suppressed | 100 / 1 |
| Release to simulated acceptance, 5 s sink delay | 100/100 within 180 s, p95 103 s, max 109 s |
| Release to simulated acceptance, 90 s sink delay | 87/100 within 180 s, p95 188 s, max 194 s |

The p95 is the 95th sorted delay over the same 100 persistent releases in both runs. The sink delay is an input. The replay dispatches each owner's single eligible match after that room's confirmation. UC-02 groups a student's matches across a complete cycle. For a match found in the first room, waiting for the last of 17 rooms at six-second spacing could add 96 seconds and require another confirmation. The P3 spike must include that wait and any extra reads. Live source latency, process recovery, provider throttling and delivery to a student's email service also need evidence.

## Decision for P3

Keep one reader with a shared request budget. Run against fixtures until the library answers Q1/Q2 with an approved source and rate. Then check whether one read covers a room's full booking horizon, whether it returns a stable room identifier, slot boundaries, status and capacity, and how the service signals throttling. If the feed requires a separate request for each room and each of seven dates, a sweep alone needs 119 reads against a two-minute allowance of 40. In that case the team needs a bulk feed or a change request before enabling live polling.

The slow-sink run missed QR-01. A pilot should timestamp release and acceptance at a test mailbox and count per-recipient volume before choosing a provider. As of 3 November 2026, Resend listed a free limit of 100 emails a day, exactly the 100 distinct recipients in this fixture. Firebase listed Cloud Messaging at no cost. Account eligibility, delivery to UTD addresses, handling of push subscriptions under QR-06 and real demand remain open for CON-03. [Resend pricing](https://resend.com/pricing) · [Firebase pricing](https://firebase.google.com/pricing)
