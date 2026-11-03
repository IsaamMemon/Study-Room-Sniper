# Study Room Sniper

Study Room Sniper alerts enrolled UT Dallas students when a McDermott Library study room fits their date, time window and group size. The student follows the alert to the library's booking page and makes their own reservation.

**Milestone:** P2 analysis and high-level design, v1.0 candidate for team review. The Python availability spike is the executable artifact for this milestone. Live library polling and NetID integration depend on responses from the library and OIT.

## Read the project

| Artifact | What it covers |
| --- | --- |
| [P2 analysis and high-level design (PDF)](docs/Study_Room_Sniper_P2.pdf) | Integrated report, figures, measured spike and baseline declaration |
| [Revision history and response to P1 feedback](docs/records.md) | Rubric scores, changes since P1, commit and PR evidence, and individual follow-up |
| [Requirements](docs/requirements.md) · [Constraints](docs/constraints.md) · [Verification](docs/verification.md) | The 14 functional requirements, six quality requirements and three constraints carried forward from P1 |
| [Use cases and analysis models](docs/analysis.md) | Create a watch, receive an alert, and review or cancel a watch |
| [Architecture](docs/architecture.md) · [Design decisions](docs/decisions.md) | Quality scenarios, deployment boundaries and the costs of the four architecture decisions |
| [Requirement traceability](docs/traceability.md) | Each requirement's path to a use case, model concept, component, decision and evidence |
| [Availability spike](docs/spikes/availability/README.md) | Reproduction command, measured results and what remains to check on a real source |
| [Elicitation](docs/elicitation/README.md) · [P3 plan and open questions](docs/plan.md) | Student survey, evidence status, working agreement, risks and proposed v1.0 baseline |
| [P1 proposal and requirements (PDF)](docs/Study_Room_Sniper_P1.pdf) | Historical v0.1 baseline |

## Run the P2 spike

From the repository root, with Python 3.10 or later:

```sh
python docs/spikes/availability/replay.py
```

The run uses a virtual clock and fictional availability for 17 rooms and 200 Active watches. Compare the printed JSON with [the recorded output](docs/spikes/availability/result.json). The peak was 20 requests per rolling minute. Slowing the simulated email acknowledgment from 5 to 90 seconds reduced the number of releases meeting the 180-second target from 100/100 to 87/100.

## Team and workflow

CE/CS/SE 3354 Software Engineering, Fall 2026 · Team 4, Section 003 · Prof. Sekir.

Alexander Eng, Arshan Khimani, Lee Baillard, Mayand Dhami, Henry McGahan and Isaam Memon.

Use a short-lived `type/description` branch, begin each logical commit with the issue it serves, and open a pull request. Another member reviews the work before merge to `main`. Each member commits their own work and links the commit and review in the contribution record. Changes to a baselined requirement go through a `change-request` issue. The [working agreement](docs/plan.md) gives the proposed meeting cadence and identifies GitHub Issues as the coordination channel.
