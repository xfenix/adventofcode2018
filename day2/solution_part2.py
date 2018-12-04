# https://adventofcode.com/2018/day/2#part2
from collections import Counter


result = []

with open('./data.txt', 'r') as advfile:
    data = advfile.read().strip().split('\n')
    for item in data:
        for subitem in data:
            if item == subitem:
                continue
            tiker = 0
            char_index = None
            for index, char in enumerate(item):
                if item[index] != subitem[index]:
                    tiker += 1
                    char_index = index
                if tiker > 1:
                    char_index = None
                    break
            if char_index is not None:
                result.append((item, subitem, char_index, item[char_index]))


print(result)
