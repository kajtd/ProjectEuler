data = [i for i in range(2, 21)]

for i in range(len(data)):
    for j in range(1, i+1):
        if data[i] % data[i - j] == 0:
            data[i] = int(data[i] / data[i - j])

answer = 1

for i in range(len(data)):
    answer *= data[i]

print(answer)