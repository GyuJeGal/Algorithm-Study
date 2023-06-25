import collections
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 정점 개수, 간선 개수
n, e = map(int, input().split())
connect = [[] for _ in range(n + 1)]

# 정점 연결 관계 생성
for _ in range(e):
    a, b, c = map(int, input().split())
    connect[a].append((b, c))
    connect[b].append((a, c))

# 필수로 거쳐야 할 두 정점
v1, v2 = map(int, input().split())

def dijkstra(start, end):
    result = [0xffffff] * (n + 1)
    result[start] = 0
    que = []
    heappush(que, (0, start))
    while que:
        weight, vertex = heappop(que)
        if weight > result[vertex]:
            continue
        for conn, distance in connect[vertex]:
            if result[conn] > result[vertex] + distance:
                result[conn] = result[vertex] + distance
                heappush(que, (result[conn], conn))
    return result[end]

can1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
can2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if can1 >= 0xffffff and can2 >= 0xffffff:
    print(-1)
else:
    print(min(can1, can2))