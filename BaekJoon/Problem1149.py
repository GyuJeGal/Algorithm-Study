import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1,n):
    data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
    data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
    data[i][2] = min(data[i-1][0], data[i-1][1]) + data[i][2]

print(min(data[n-1]))