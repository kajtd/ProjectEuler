fib = [1, 1]

number = 0
index = 1

while number <= 4000000:
    number = fib[index] + fib[index-1]
    fib.append(number)
    index += 1

evenValuedSum = sum(n for n in fib if n % 2 == 0)
print(evenValuedSum)
