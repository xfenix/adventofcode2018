# https://adventofcode.com/2018/day/3
total_overlaps = 0
fabric = {}

with open('./data.txt', 'r') as ffile:
    data = ffile.read().strip().split('\n')
    for data_row in data:
        parts = data_row.split('@')
        parts2 = parts[1].split(':')
        left, top = parts2[0].split(',')
        width, height = parts2[1].split('x')
        width = int(width)
        height = int(height)
        left = int(left)
        top = int(top)
        for width_shift in range(width):
            for height_shift in range(height):
                coord_x = left + width_shift + 1
                coord_y = top + height_shift + 1
                if coord_x not in fabric:
                    fabric[coord_x] = {}
                if coord_y not in fabric[coord_x]:
                    fabric[coord_x][coord_y] = 0
                fabric[coord_x][coord_y] += 1

total_rows = 0
for index, value in fabric.items():
    for subindex, subvalue in fabric[index].items():
        if subvalue > 1:
            total_overlaps += 1

print(total_overlaps)
