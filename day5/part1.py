# https://adventofcode.com/2018/day/5
def calc_polymer_reaction(polymer_list):
    total_len = len(polymer_list)
    new_polymer = []
    index = 0
    while True:
        char = polymer_list[index]
        new_polymer.append(char)
        if index + 1 >= total_len:
            break
        next_char = polymer_list[index + 1]
        if char != next_char and char.lower() == next_char.lower():
            new_polymer.pop()
            index += 2
        else:
            index += 1
    return new_polymer


source_polymer = list(open('data.txt', 'r').read().strip())
step_result = source_polymer[:]
while True:
    # progress
    print('.', end='', flush=True)
    previous_len = len(step_result)
    step_result = calc_polymer_reaction(step_result)
    if previous_len == len(step_result):
        # after 1360 steps...
        print('')
        print(len(step_result))
        break
