import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

board = []
answer = 0

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            que = collections.deque()
            que.append([i, j, 0])
            visit = [[0] * M for _ in range(N)]
            visit[i][j] = 1

            while que:
                x, y, count = que.popleft()

                if board[x][y] == 1:
                    answer = max(answer, count)
                    break

                for k in range(8):
                    if 0 <= x + dx[k] < N and 0 <= y + dy[k] < M:
                        if visit[x + dx[k]][y + dy[k]] == 0:
                            que.append([x + dx[k], y + dy[k], count + 1])
                            visit[x + dx[k]][y + dy[k]] = 1

print(answer)