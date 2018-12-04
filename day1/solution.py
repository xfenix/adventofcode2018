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
print(len(freq_list))
print(len(set(freq_list)))
