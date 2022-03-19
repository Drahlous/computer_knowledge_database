import unittest

sample_events = {}
sample_events["A"] = { "start": 10, "end": 15 }
sample_events["B"] = { "start": 14, "end": 15 }
sample_events["C"] = { "start": 16, "end": 19 }
sample_events["D"] = { "start": 16, "end": 20 }
sample_events["E"] = { "start": 20, "end": 25 }

# The next event must end after the current event
# and we'll pick the one with the earliest end-time
def get_next_valid_earliest(remaining_events, previous_end_time):
    next_earliest = None

    for event, times in list(remaining_events.items()):
        start = times["start"]
        end = times["end"]

        # It's too late to take this item, it begins before the previous event is finished
        if start < previous_end_time:
            remaining_events.pop(event)
        elif next_earliest is None or end < remaining_events[next_earliest]["end"]:
                next_earliest = event

    return next_earliest
        

def greedy_schedule(events):
    final_schedule = []
    previous_end_time = 0
    remaining_events = events
    while remaining_events is not None:
        next = get_next_valid_earliest(events, previous_end_time)
        if next is not None:
            previous_end_time = events[next]["end"]
            final_schedule.append(next)
            remaining_events.pop(next)
        else:
            break
    return final_schedule


# Unit Tests
class GreedySchedulingTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(greedy_schedule(sample_events), ["A", "C", "E"])
