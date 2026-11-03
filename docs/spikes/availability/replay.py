"""Replay a fictional library day and print the P2 measurements. Python 3.10+."""

from dataclasses import dataclass
from math import ceil
import json


ROOMS = 17
DAY_SECONDS = 24 * 60 * 60
POLL_SPACING = 6
CONFIRM_AFTER = 3
PERSISTENT_SLOTS = 100
ROOM_CAPACITY = 6


@dataclass(frozen=True)
class Slot:
    room: int
    day: int
    start: int  # minutes from midnight; all fixture slots last 30 minutes
    released: int  # simulated seconds from start of replay
    removed: int | None = None

    def visible(self, now):
        return self.released <= now and (self.removed is None or now < self.removed)


@dataclass(frozen=True)
class Watch:
    day: int
    start: int
    end: int
    group: int

    def matches(self, slot):
        return (self.day == slot.day and self.start <= slot.start
                and slot.start + 30 <= self.end and self.group <= ROOM_CAPACITY)


def fixtures():
    slots = []
    watches = []
    for index in range(PERSISTENT_SLOTS):
        # Five simultaneous waves of 20 releases. Their phase shifts vs. the reader.
        wave, period = divmod(index, 20)
        day = 2 + wave
        start = 8 * 60 + 30 * period
        released = 601 + wave * 18_007
        slots.append(Slot(index % ROOMS, day, start, released))
        # Distinct owners. One positive and one too-large group for this window.
        watches.extend([Watch(day, start, start + 30, 4), Watch(day, start, start + 30, 8)])

    # Room 1 is read at t=6. A second slot for watch 0 vanishes before t=9.
    slots.append(Slot(1, slots[0].day, slots[0].start, released=5, removed=8))
    return slots, watches


def peak_minute(requests):
    """Largest request count in any interval (t-60, t]."""
    first = peak = 0
    for last, timestamp in enumerate(requests):
        while requests[first] <= timestamp - 60:
            first += 1
        peak = max(peak, last - first + 1)
    return peak


def delivery_metrics(confirmation_delays, sink_delay):
    delays = sorted(delay + sink_delay for delay in confirmation_delays)
    return {
        "assumed_sink_delay_s": sink_delay,
        "within_180s": sum(delay <= 180 for delay in delays),
        "p95_s": delays[ceil(0.95 * len(delays)) - 1],
        "max_s": delays[-1],
    }


def simulate():
    slots, watches = fixtures()
    by_room = [[] for _ in range(ROOMS)]
    for slot_id, slot in enumerate(slots):
        by_room[slot.room].append((slot_id, slot))

    requests = []
    polls = [[] for _ in range(ROOMS)]
    sent = set()  # In-memory (watch, slot) keys for this experiment.
    confirmed_delays = []
    rechecks = suppressed = 0
    for poll_time in range(0, DAY_SECONDS, POLL_SPACING):
        room = poll_time // POLL_SPACING % ROOMS
        requests.append(poll_time)
        polls[room].append(poll_time)
        candidates = [
            (watch_id, slot_id)
            for slot_id, slot in by_room[room] if slot.visible(poll_time)
            for watch_id, watch in enumerate(watches)
            if (watch_id, slot_id) not in sent and watch.matches(slot)
        ]
        if candidates:
            # A single confirmation reads this room for every candidate pair.
            confirm_time = poll_time + CONFIRM_AFTER
            requests.append(confirm_time)
            rechecks += 1
            for watch_id, slot_id in candidates:
                slot = slots[slot_id]
                if slot.visible(confirm_time):
                    confirmed_delays.append(confirm_time - slot.released)
                    sent.add((watch_id, slot_id))
                else:
                    suppressed += 1

    expected_pairs = {(2 * slot_id, slot_id) for slot_id in range(PERSISTENT_SLOTS)}
    if sent != expected_pairs or len(confirmed_delays) != len(expected_pairs) or suppressed != 1:
        raise AssertionError("Unexpected recipient, missing or duplicate alert, or stale slot sent")
    max_gap = max(later - earlier for room_polls in polls
                  for earlier, later in zip(room_polls, room_polls[1:]))
    peak = peak_minute(requests)
    base = delivery_metrics(confirmed_delays, 5)
    if max_gap > 120 or peak > 20 or base["within_180s"] < 95:
        raise AssertionError("Baseline replay missed a P1 threshold")
    return {
        "simulated_hours": DAY_SECONDS // 3600,
        "rooms": ROOMS,
        "active_watches": len(watches),
        "persistent_releases": PERSISTENT_SLOTS,
        "stale_candidates_suppressed": suppressed,
        "unique_watch_slot_alerts": len(sent),
        "room_polls": sum(map(len, polls)),
        "shared_confirmation_reads": rechecks,
        "max_per_room_poll_gap_s": max_gap,
        "peak_library_requests_in_rolling_60s": peak,
        "baseline": base,
        "slow_sink": delivery_metrics(confirmed_delays, 90),
    }


if __name__ == "__main__":
    print(json.dumps(simulate(), indent=2))
