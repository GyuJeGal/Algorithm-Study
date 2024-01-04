import sys
import heapq
import collections

input = sys.stdin.readline

# 정점의 개수
n = int(input())

# 양방향 그래프
graph = [[] for _ in range(n + 1)]
# 트리 구조 단방향 그래프
tree = [[] for _ in range(n + 1)]

for _ in range(n):
    conn = list(map(int, input().split()))

    start = conn[0]
    i = 1
    while True:
        if conn[i] == -1:
            break
        graph[start].append([conn[i], conn[i + 1]])
        i += 2

answer = 0

order = collections.deque()
order.append(1)
que = collections.deque()
que.append(1)
visited = [0] * (n + 1)
visited[1] = 1
while que:
    v = que.popleft()
    for g in graph[v]:
        if visited[g[0]] == 0:
            que.append(g[0])
            order.appendleft(g[0])
            visited[g[0]] = 1
            tree[v].append([g[0], g[1]])

dist = [[] for _ in range(n + 1)]

for i in order:
    if len(tree[i]) == 0:
        dist[i].append(0)
    elif len(tree[i]) == 1:
        v, w = tree[i][0]
        dist[i].append(-(w - dist[v][0]))
    else:
        for v, w in tree[i]:
            heapq.heappush(dist[i], -(w - dist[v][0]))
        check = heapq.heappop(dist[i])
        answer = max(answer, -(dist[i][0] + check))
        heapq.heappush(dist[i], check)

answer = max(answer, -dist[1][0])

if answer == 0 and len(dist[1]) == 1:
    print(-dist[1][0])
else:
    print(answer)

