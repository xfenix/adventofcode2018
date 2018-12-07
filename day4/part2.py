from datetime import datetime
from collections import defaultdict


lines = open('data.txt').read().split('\n')
lines.sort()

shifts_log = defaultdict(int)
guard = None
asleep = None
for line in lines:
    if not line:
        continue
    time = int(line.split(':')[-1].split(']')[0])
    if 'begins shift' in line:
        guard = int(line.split()[3][1:])
        asleep = None
    elif 'falls asleep' in line:
        asleep = time
    elif 'wakes up' in line:
        for one_minute in range(asleep, time):
            shifts_log[(guard, one_minute)] += 1

best_pair = None
for key, value in shifts_log.items():
    if best_pair is None or value > shifts_log[best_pair]:
        best_pair = key

best_guard, best_min = best_pair
print(best_guard, best_min)
print(best_guard * best_min)
