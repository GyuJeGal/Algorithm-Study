import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

que = []
heapq.heappush(que, (0, k))

distance = [INF] * (V + 1)
distance[k] = 0

while que:
    dist, cur = heapq.heappop(que)

    if dist > distance[cur]:
        continue

    for i in graph[cur]:
        if distance[i[0]] > dist + i[1]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(que, (dist + i[1], i[0]))

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

