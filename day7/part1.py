from collections import defaultdict


lines = open('./data.txt', 'r').readlines()
graph = defaultdict(list)
counters = defaultdict(int)

for one_line in lines:
    parts = one_line.split()
    x = parts[1]
    y = parts[7]
    graph[x].append(y)
    counters[y] += 1

# find root
queue = []
for key in graph:
    if counters[key] == 0:
        queue.append(key)

# and finally build chain
result = []
while queue:
    item = sorted(queue)[0]
    queue = list(filter(lambda row: row != item, queue))
    result.append(item)
    for key in graph[item]:
        counters[key] -= 1
        if counters[key] == 0:
            queue.append(key)

print(''.join(result))
