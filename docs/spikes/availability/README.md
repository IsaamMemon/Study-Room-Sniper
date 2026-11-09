# Can the reader find a free slot in time?

The reader has to revisit every room within two minutes and make at most 20 library requests per rolling minute, including confirmations. This replay tests whether one shared reader can do both with 200 Active watches.

## What the public pages showed

On 3 November the public library index listed nine group rooms and eight smart rooms. The group-room page returned HTTP 429, the all-rooms page could not be retrieved, and the smart-room page showed the calendar legend without dated slots in the retrieved text. The replay therefore uses simulated openings. The library still needs to confirm how to read live slots and at what rate. [Library index](https://libcal.utdallas.edu/) · [Group rooms](https://libcal.utdallas.edu/spaces?gid=6673&lid=3972) · [Smart rooms](https://libcal.utdallas.edu/spaces?lid=4255) · [All rooms](https://libcal.utdallas.edu/allspaces)

## Reproduce the experiment

From this directory, run the command below with Python 3.10 or later. It uses only the standard library. The JSON output should match [the recorded run](result.json). A failed check raises an error.

```sh
python replay.py
```

Over one simulated day, 100 slots open in five groups of 20. Each slot fits one watch. A second watch requests the same time for a group too large for the room. One extra slot disappears between the first read and confirmation. The reader polls a room every six seconds and checks it again three seconds later if it finds new matches.

| Measurement | Observed in the replay |
| --- | ---: |
| Scheduled room polls / extra confirmation reads | 14,400 / 86 |
| Longest gap between consecutive polls of the same room | 102 s |
| Peak requests in any rolling 60 s, confirmations included | 20 |
| Eligible persistent watch/slot pairs alerted / fleeting candidates suppressed | 100 / 1 |
| Release to simulated acceptance, 5 s sink delay | 100/100 within 180 s, p95 103 s, max 109 s |
| Release to simulated acceptance, 90 s sink delay | 87/100 within 180 s, p95 188 s, max 194 s |

The two email-delay runs use the same 100 releases. The 95th-percentile time includes the assumed email delay. Each recipient in this run has one qualifying slot. In UC-02, a student can match several rooms in one cycle. An opening found in the first room could wait another 96 seconds for the last room's read, then need a fresh confirmation. The next experiment should time that whole path through acceptance at a test mailbox.

## Decision for P3

Keep one reader with a shared request budget. Run against fixtures until the library answers Q1/Q2 with an approved source and rate. Then check whether one read covers a room's full booking horizon, whether it returns a stable room identifier, slot boundaries, status and capacity, and how the service signals throttling. If the feed requires a separate request for each room and each of seven dates, a sweep alone needs 119 reads against a two-minute allowance of 40. In that case the team needs a bulk feed or a change request before enabling live polling.

The slow-sink run missed QR-01. A pilot should timestamp release and acceptance at a test mailbox and count per-recipient volume before choosing a provider. As of 3 November 2026, Resend listed a free limit of 100 emails a day, exactly the 100 distinct recipients in this fixture. Firebase listed Cloud Messaging at no cost. Account eligibility, delivery to UTD addresses, handling of push subscriptions under QR-06 and real demand remain open for CON-03. [Resend pricing](https://resend.com/pricing) · [Firebase pricing](https://firebase.google.com/pricing)

## Independent rerun
8 November 2026 · Isaam Memon · Python 3.13.3 on Windows, fresh clone of main.
`python replay.py` completed with no failed checks, and its JSON output matched result.json exactly.