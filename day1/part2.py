# https://adventofcode.com/2018/day/1
result = 0
freq_list = [result, ]

with open('./data.txt', 'r') as advfile:
    data = advfile.read().strip().split("\n")
    for item in data:
        result += eval(item)
        # print(result)
        if result in freq_list:
            print('Yeah: ', result)
            break
        freq_list.append(result)

print(freq_list)
