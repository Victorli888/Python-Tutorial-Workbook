"""
This is Problem 1.1 for the Full Course @ Interview Cake.
Question: Your company built an in-house calender tool and you want to add a feature to see the times in a day when
Everyone is available. Starting at 9AM
1) in this question each integer represents a 30-minute time block starting from 9:00am.
    - (1,3) -> (9:30am to 10:30am)
"""


def merge_ranges(meetings):
    # Sort by the time
    sorted_meetings = sorted(meetings)

    # initialize merged meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meetings_start, current_meetings_end in sorted_meetings[1:]:
        last_merged_meetings_start, last_merged_meetings_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the later end time of the two
        if current_meetings_start <= last_merged_meetings_end:
            merged_meetings[-1] = (last_merged_meetings_start, max(last_merged_meetings_end, current_meetings_end))

        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meetings_start, current_meetings_end))

    return merged_meetings


times = [(1, 2), (2, 3)]

merge_ranges(times)
