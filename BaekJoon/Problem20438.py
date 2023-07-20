import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleeper = list(map(int, input().split()))
receiver = list(map(int, input().split()))
receiver = list(set(receiver) - set(sleeper))

result = [1] * (N + 3)

for i in receiver:
    count = 1
    while i * count < N + 3:
        if i * count not in sleeper:
            result[i * count] = 0
        count += 1

for i in range(3, N + 3):
    if i != 3:
        result[i] += result[i - 1]

for _ in range(M):
    S, E = map(int, input().split())
    if S == 3:
        print(result[E])
    else:
        print(result[E] - result[S - 1])