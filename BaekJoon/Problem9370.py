import sys, heapq

input = sys.stdin.readline

INF = int(1e9)

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    # 정점, 간선, 목적지 후보 개수
    n, m, t = map(int, input().split())
    # 출발 정점, 지나친 정점 두개(두 정점 사이의 도로를 지나침)
    s, g, h = map(int, input().split())
    # g, h 사이의 거리
    ghDist = 0

    # 그래프
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([d, b])
        graph[b].append([d, a])
        if (a == g and b == h) or (a == h and b == g):
            ghDist = d

    # 목적지 후보 정점
    candidate = [int(input()) for _ in range(t)]

    # 다익스트라 함수
    def dijkstra(start):
        # start 부터 다른 정점까지의 최단 거리
        distance = [INF] * (n + 1)
        distance[start] = 0

        # 최소힙 우선 순위 큐
        que = []
        heapq.heappush(que, (0, start))

        while que:
            weight, v = heapq.heappop(que)
            if weight > distance[v]:
                continue
            for dist, vertex in graph[v]:
                if dist + weight < distance[vertex]:
                    distance[vertex] = dist + weight
                    heapq.heappush(que, (dist + weight, vertex))
        return distance

    # s에서 다른 정점까지의 최단 거리 리스트
    sDistance = dijkstra(s)
    # h에서 다른 정점까지의 최단 거리 리스트
    hDistance = dijkstra(h)
    # g에서 다른 정점까지의 최단 거리 리스트
    gDistance = dijkstra(g)

    answer = []

    for c in candidate:
        # 시나리오 1: s -> g -> h -> candidate의 최단 거리가 s -> candidate의 최단 거리와 동일한 경우
        if sDistance[g] + ghDist + hDistance[c] == sDistance[c]:
            answer.append(c)

        # 시나리오 2: s -> h -> g -> candidate의 최단 거리가 s -> candidate의 최단 거리와 동일한 경우
        elif sDistance[h] + ghDist + gDistance[c] == sDistance[c]:
            answer.append(c)

    answer.sort()
    for i in answer:
        print(i, end=' ')
    print()