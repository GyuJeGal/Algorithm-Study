import sys

input = sys.stdin.readline

result = [[0] for _ in range(15)]

for i in range(1, 15):
    result[0].append(i)

for i in range(1, 15):
    count = 0
    for j in range(1, 15):
        count += result[i - 1][j]
        result[i].append(count)

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(result[k][n])
