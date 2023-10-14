import sys

input = sys.stdin.readline

N = int(input())

answer = 0

for i in range(1, N):
    answer += (N * i) + i

print(answer)
