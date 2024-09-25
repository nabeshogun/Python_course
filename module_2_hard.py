print('Введите число от 3 до 20:')
n = int(input())
result = ''
for i in range(1, n//2+1):
    for j in range(2, n):
        if (n % (i+j) == 0) and i < j:
            result += str(i)
            result += str(j)

print(result)


