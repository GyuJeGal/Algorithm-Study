import sys
import heapq
import collections

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
dist = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])

answer = 0

order = collections.deque()
order.append(1)
que = collections.deque()
que.append(1)
while que:
    v = que.popleft()
    for g in graph[v]:
        que.append(g[0])
        order.appendleft(g[0])

for i in order:
    if len(graph[i]) == 0:
        dist[i].append(0)
    elif len(graph[i]) == 1:
        v, w = graph[i][0]
        dist[i].append(-(w - dist[v][0]))
    else:
        for v, w in graph[i]:
            heapq.heappush(dist[i], -(w - dist[v][0]))
        check = heapq.heappop(dist[i])
        answer = max(answer, -(dist[i][0] + check))
        heapq.heappush(dist[i], check)

answer = max(answer, -dist[1][0])

if answer == 0 and len(dist[1]) == 1:
    print(-dist[1][0])
else:
    print(answer)

