# https://adventofcode.com/2018/day/4
from datetime import datetime


EVENT_START = 0
EVENT_SLEEP = 1
EVENT_WAKE = 2
shifts_by_days = {}
guards_sleep = {}

with open('./data.txt', 'r') as ffile:
    data_rows = ffile.read().strip().split('\n')
    current_guard = None
    for one_row in data_rows:
        parts = one_row.split(']')
        parsed_date = datetime.strptime(parts[0].lstrip('['), '%Y-%m-%d %H:%M')
        current_date = str(parsed_date.date())
        if current_date not in shifts_by_days:
            shifts_by_days[current_date] = dict()
        event = parts[1].strip()
        if event == 'wakes up':
            event_type = EVENT_WAKE
        elif event == 'falls asleep':
            event_type = EVENT_SLEEP
        else:
            event_type = EVENT_START
            shifts_by_days[current_date]['guard'] = event.replace('Guard', '')\
                .replace('begins shift', '').strip()
        if 'list' not in shifts_by_days[current_date]:
            shifts_by_days[current_date]['list'] = []
        shifts_by_days[current_date]['list'].append(dict(
            event=event_type,
            date=parsed_date,
        ))

for _, data in shifts_by_days.items():
    if 'guard' in data:
        guard_id = data['guard']
        shift_log = sorted(data['list'], key=lambda item: item['date'])
        total_sleep = 0
        for log_row in shift_log:
            if log_row['event'] == EVENT_SLEEP:
                start_sleep = log_row['date']
            elif log_row['event'] == EVENT_WAKE:
                total_sleep += int((log_row['date'] - start_sleep).seconds/60 - 1)
        if guard_id not in guards_sleep:
            guards_sleep[guard_id] = 0
        guards_sleep[guard_id] += total_sleep
    else:
        pass

most_sleepy_list = sorted(guards_sleep.items(), key=lambda item: item[1], reverse=True)
most_sleepy_guard = most_sleepy_list[0][0]
