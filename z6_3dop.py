first = int(input('Введите число от 3 до 20:'))
result = ''

for i in range(1,first):
    for k in range(i+1,first):
        if first % (i+k) ==0:
            result += str(i) + str(k)
print(result)