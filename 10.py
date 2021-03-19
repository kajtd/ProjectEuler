def findSum(n):
    sumOfPrimes, sieve = 0, [True] * n
    for i in range(2, n):
        if sieve[i]:
            sumOfPrimes += i
            for j in range(i ** 2, n, i):
                sieve[j] = False
    return sumOfPrimes


print(findSum(2000000))