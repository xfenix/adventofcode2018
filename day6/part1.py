# https://adventofcode.com/2018/day/6
from collections import defaultdict


lines = [line.strip() for line in open('./data.txt', 'r').readlines()]
coords = set()
max_x = max_y = 0
for line in lines:
    x, y = map(int, line.split(','))
    coords.add((x, y))
    max_x = max(max_x, x)
    max_y = max(max_y, y)

coord_id_to_point = {coord_id: point for coord_id, point in enumerate(coords, start=1)}
region_sizes = defaultdict(int)
infinite_ids = set()
for i in range(max_x + 1):
    for j in range(max_y + 1):
        min_dists = sorted([(abs(x - i) + abs(y - j), coord_id) for coord_id, (x, y) in coord_id_to_point.items()])
        if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
            coord_id = min_dists[0][1]
            region_sizes[coord_id] += 1
            if i == 0 or i == max_x or j == 0 or j == max_y:
                infinite_ids.add(coord_id)

print(
    max(size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids)
)
