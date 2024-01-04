import sys
import heapq
import collections

input = sys.stdin.readline

INF = int(1e9)

# N: 마을의 수, M: 도로의 수, X: 파티가 열리는 마을 번호
N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reversedGraph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
    reversedGraph[e].append([s, t])


def dijkstra(conn, start):
    dist = [INF] * (N + 1)
    dist[start] = 0

    que = []
    heapq.heappush(que, [0, start])

    while que:
        d, v = heapq.heappop(que)

        if dist[v] < d:
            continue

        for nxt, w in conn[v]:
            if w + d < dist[nxt]:
                heapq.heappush(que, [w + d, nxt])
                dist[nxt] = w + d

    return dist


# 목적지에서 다른 정점으로 가는 최단거리 저장
dist = dijkstra(graph, X)

# 다른 정점에서 목적지로 가는 최단거리 저장
# 단방향 간선을 뒤집어서 다익스트라 알고리즘을 적용하면 목적지로 도착하는 최단거리를 구할 수 있다
reversedDist = dijkstra(reversedGraph, X)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, reversedDist[i] + dist[i])

print(answer)
