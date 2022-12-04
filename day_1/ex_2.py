data = list(map(lambda s: s.strip(), open('input_1.txt').readlines()))
result = [0, 0, 0]
temp = 0

for i in data:
    if i:
        temp += int(i)
        continue

    for count, j in enumerate(result):
        if temp >= j:
            result.insert(count, temp)
            result.pop(-1)
            break
    temp = 0

print(result[0] + result[1] + result[2])
