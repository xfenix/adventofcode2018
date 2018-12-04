# https://adventofcode.com/2018/day/3#part2
fabric = {}


def parse_row(data_row):
    parts = data_row.split('@')
    claim_id = parts[0]
    parts2 = parts[1].split(':')
    left, top = parts2[0].split(',')
    width, height = parts2[1].split('x')
    width = int(width)
    height = int(height)
    left = int(left)
    top = int(top)
    return width, height, left, top, claim_id


with open('./data.txt', 'r') as ffile:
    data = ffile.read().strip().split('\n')

    # fill up fabric matrix
    for data_row in data:
        width, height, left, top, _ = parse_row(data_row)
        for width_shift in range(width):
            for height_shift in range(height):
                coord_x = left + width_shift + 1
                coord_y = top + height_shift + 1
                if coord_x not in fabric:
                    fabric[coord_x] = {}
                if coord_y not in fabric[coord_x]:
                    fabric[coord_x][coord_y] = 0
                fabric[coord_x][coord_y] += 1

    # find intact claim
    for data_row in data:
        width, height, left, top, claim_id = parse_row(data_row)
        failed = False
        for width_shift in range(width):
            if failed:
                break
            for height_shift in range(height):
                coord_x = left + width_shift + 1
                coord_y = top + height_shift + 1
                # good situations: zero or one claim for this cells
                if coord_x not in fabric or coord_y not in fabric[coord_x] or fabric[coord_x][coord_y] == 1:
                    continue
                failed = True
                break
        if not failed:
            print('Winner is: ', claim_id)
            break
