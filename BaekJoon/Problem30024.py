import sys, heapq

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

corn = []

for _ in range(N):
    lst = list(map(int, input().split()))
    corn.append(lst)

K = int(input())

# 최대 힙 우선 순위 큐
# 큐에는 옥수수를 수확할 수 있는 위치와 가치 저장
# 큐에 [옥수수 가치, 행, 열]로 저장
que = []

# 가장자리 큐에 푸시
for i in range(N):
    heapq.heappush(que, [-corn[i][0], i, 0])
    corn[i][0] = 0
    heapq.heappush(que, [-corn[i][M - 1], i, M - 1])
    corn[i][M - 1] = 0
for i in range(1, M - 1):
    heapq.heappush(que, [-corn[0][i], 0, i])
    corn[0][i] = 0
    heapq.heappush(que, [-corn[N - 1][i], N - 1, i])
    corn[N - 1][i] = 0

answer = []

# 옥수수 수확 시작
while que:
    if K == 0:
        break
    value, x, y = heapq.heappop(que)
    answer.append([x + 1, y + 1])
    corn[x][y] = 0
    K -= 1

    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
            if corn[x + dx[i]][y + dy[i]] != 0:
                heapq.heappush(que, [-corn[x + dx[i]][y + dy[i]], x + dx[i], y + dy[i]])
                corn[x + dx[i]][y + dy[i]] = 0

for pos in answer:
    print(pos[0], pos[1])
