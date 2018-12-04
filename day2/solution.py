from collections import Counter


counters = {2: 0, 3: 0}

with open('./data.txt', 'r') as advfile:
    data = advfile.read().strip().split("\n")
    for item in data:
        freqs = Counter(item)
        freqs_ready = {y: x for x, y in freqs.items()}
        for index, _ in counters.items():
            if index in freqs_ready:
                counters[index] += 1

print(counters)
print(counters[2] * counters[3])
