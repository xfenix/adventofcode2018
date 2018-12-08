# https://adventofcode.com/2018/day/6#part2
lines = [line.strip() for line in open('./data.txt', 'r').readlines()]
manhattan_limit = 10000
coords = set()
max_x = max_y = 0

for line in lines:
    x, y = map(int, line.split(','))
    coords.add((x, y))
    max_x = max(max_x, x)
    max_y = max(max_y, y)

size_shared_region = 0
for i in range(max_x + 1):
    for j in range(max_y + 1):
        if sum(abs(x - i) + abs(y - j) for x, y in coords) < manhattan_limit:
            size_shared_region += 1

print(size_shared_region)
