import sys
import collections

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

answer = 0
visited = [[0] * M for _ in range(N)]
board = []
start = [0, 0]
check = True

for i in range(N):
    s = input()
    if check:
        for j in range(M):
            if s[j] == "I":
                start[0] = i
                start[1] = j
                check = False
                break
    board.append(s)

que = collections.deque()
visited[start[0]][start[1]] = 1
que.append([start[0], start[1]])

while que:
    x, y = que.popleft()

    for i in range(4):
        if x + dx[i] >= N or x + dx[i] < 0 or y + dy[i] >= M or y + dy[i] < 0:
            continue
        if visited[x + dx[i]][y + dy[i]] == 0 and board[x + dx[i]][y + dy[i]] != "X":
            if board[x + dx[i]][y + dy[i]] == "P":
                answer += 1
            visited[x + dx[i]][y + dy[i]] = 1
            que.append([x + dx[i], y + dy[i]])

if answer == 0:
    print("TT")
else:
    print(answer)