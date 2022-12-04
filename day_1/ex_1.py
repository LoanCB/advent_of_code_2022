data = list(map(lambda s: s.strip(), open('input_1.txt').readlines()))
result = 0
temp = 0

for i in data:
    if not i:
        temp = 0
        continue
    temp += int(i)
    if temp > result:
        result = temp

print(result)
