# https://adventofcode.com/2018/day/5#part2
# BEARware - this script running about 5 minutes
def calc_polymer_reaction(polymer_list):
    total_len = len(polymer_list)
    new_polymer = []
    index = 0
    while True:
        try:
            char = polymer_list[index]
        except IndexError:
            break
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


source_polymer = open('data.txt', 'r').read().strip()
distinct_chars = set(source_polymer.lower())
total_lenghts = []

for one_char in distinct_chars:
    step_result = list(filter(
        lambda char: char != one_char and char != one_char.upper(),
        list(source_polymer)))
    while True:
        # progress
        previous_len = len(step_result)
        step_result = calc_polymer_reaction(step_result)
        if previous_len == len(step_result):
            result_len = len(step_result)
            print('Calced polymer without char', one_char, 'Length:', result_len)
            total_lenghts.append(result_len)
            break

print('Finally!', min(total_lenghts))
