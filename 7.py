from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def findPrime(n):
    howManyPrimes = 0
    prime = 1

    while howManyPrimes < n:
        prime += 1
        if isPrime(prime):
            howManyPrimes += 1
    return prime


print(findPrime(10001))