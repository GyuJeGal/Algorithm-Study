import sys
import heapq

input = sys.stdin.readline

N, A, B = map(int, input().split())

p = []
q = []

# 최대 힙기반 우선 순위 큐
que = []
answer = 0

for i in range(N):
    j1, j2 = map(int, input().split())
    p.append(j1)
    q.append(j2)
    diff = max(j1, j2) - min(j1, j2)
    heapq.heappush(que, [-diff, i])

for i in range(N):
    diff, idx = heapq.heappop(que)
    if A == 0:
        answer += q[idx]
        B -= 1
    elif B == 0:
        answer += p[idx]
        A -= 1
    elif p[idx] < q[idx]:
        answer += p[idx]
        A -= 1
    else:
        answer += q[idx]
        B -= 1

print(answer)
