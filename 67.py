data = [list(map(int, line.split())) for line in open('triangle67').readlines()]

n = len(data)-1

for row in range(n, 0, -1):
    for col in range(row):
        data[row-1][col] += max(data[row][col], data[row][col+1])

print("Maximum sum in triangle", data[0][0])
