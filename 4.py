from math import sqrt

def isPalindrome(n):
    rev = 0
    temp = n
    while (n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        return True
    return False

max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if isPalindrome(i * j):
            if (i * j) > max:
                max = i * j

print(max)