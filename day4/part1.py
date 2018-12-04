# https://adventofcode.com/2018/day/4
EVENT_START = 0
EVENT_SLEEP = 1
EVENT_WAKE = 2
sleep_log = {}

with open('./data.txt', 'r') as ffile:
    data_rows = ffile.read().strip().split('\n')
    current_guard = None
    for one_row in data_rows:
        parts = one_row.split(']')
        date = parts[0].lstrip('[')
        event = parts[1].strip()
        if event == 'wakes up':
            event_type = EVENT_WAKE
        elif event == 'falls asleep':
            event_type = EVENT_SLEEP
        else:
            event_type = EVENT_START
            current_guard = event.replace('Guard', '')\
                                 .replace('begins shift').strip()
