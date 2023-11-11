from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [True] + [False] * 100
que = deque([(1, 0)])
link = [0] * 101
for _ in range(n+m):
    a, b = map(int, input().split())
    link[a] = b

while que:
    v, t = que.popleft()
    if v == 100:
        print(t)
        break
    t += 1
    for i in range(1, 7):
        to_v = v+i
        if to_v > 100 or visited[to_v]:
            continue
        visited[to_v] = True
        if link[to_v]:
            que.append((link[to_v], t))
        else:
            que.append((to_v, t))