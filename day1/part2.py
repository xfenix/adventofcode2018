# https://adventofcode.com/2018/day/1
import sys


result = 0
freq_list = [result, ]

with open('./data.txt', 'r') as advfile:
    data = advfile.read().strip().split("\n")
    while True:
        print('.', end='', flush=True)
        for item in data:
            result += eval(item)
            if result in freq_list:
                print('Yeah: ', result)
                sys.exit(0)
            freq_list.append(result)
