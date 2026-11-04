# Study Room Sniper

When a McDermott Library room is booked, students have to check the calendar again to catch a cancellation. Study Room Sniper lets an enrolled UT Dallas student save a date, time window and group size. If a room opens up, the student gets an email with a link to book it on the library's site.

P2 is ready for team review in [PR #19](https://github.com/PaperBagTrick/Study-Room-Sniper/pull/19). The polling experiment runs locally with Python. Live availability and NetID sign-in depend on the library and OIT.

Read the [P2 analysis and design report (PDF)](docs/Study_Room_Sniper_P2.pdf) or the [original P1 proposal (PDF)](docs/Study_Room_Sniper_P1.pdf).

## Run the P2 spike

From the repository root, with Python 3.10 or later:

```sh
python docs/spikes/availability/replay.py
```

The replay runs a day of openings for 17 rooms and 200 watches. It peaked at 20 library requests in a rolling minute. With a five-second email delay, all 100 alerts met the three-minute target. With a 90-second delay, 87 did. See the [experiment](docs/spikes/availability/README.md) and [recorded output](docs/spikes/availability/result.json).

## Project files

- What the service must do · [requirements](docs/requirements.md), [constraints](docs/constraints.md) and [acceptance checks](docs/verification.md).
- How a watch works · [use cases and diagrams](docs/analysis.md), [architecture](docs/architecture.md), [design decisions](docs/decisions.md) and [traceability](docs/traceability.md).
- Team work · [changes since P1](docs/records.md), [student survey and library questions](docs/elicitation/README.md), and [P3 schedule and open questions](docs/plan.md).

## Team and workflow

CE/CS/SE 3354 Software Engineering, Fall 2026 · Team 4, Section 003 · Prof. Sekir.

Alexander Eng, Arshan Khimani, Lee Baillard, Mayand Dhami, Henry McGahan and Isaam Memon.

Start a `type/description` branch and put the issue number first in each commit message. Another teammate reviews the pull request before it goes into `main`. For changes to a baselined requirement, open a `change-request` issue. The [working agreement](docs/plan.md) covers meetings, decisions and individual contributions.
