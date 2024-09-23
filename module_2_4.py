numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k = 0
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(2, numbers[i] // 2+1):
        if numbers[i] % j == 0:
            k = k+1
    if k <= 0:
        is_prime = True
    else:
        is_prime = False
    if numbers[i] > 1:
        if is_prime == 1:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
    i += 1
    k = 0
print(primes)
print(not_primes)
