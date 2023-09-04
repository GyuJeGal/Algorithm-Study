import collections
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())

# 좌표당 현재 양분
food = [[5] * N for _ in range(N)]
# 겨울에 추가할 양분
plusFood = []
# 나무 좌표
trees = [[collections.deque() * N for _ in range(N)] for _ in range(N)]

for _ in range(N):
    temp = list(map(int, input().split()))
    plusFood.append(temp)

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

def spring_summer():
    # 봄, 여름 진행
    for j in range(N):
        for k in range(N):
            # 현재 좌표에 나무가 있을 때
            if trees[j][k]:
                size = len(trees[j][k])
                for p in range(size):
                    # 양분이 없을 경우, 같은 좌표의 뒤에 나무들도 다 죽음
                    if food[j][k] < trees[j][k][p]:
                        for _ in range(p, size):
                            food[j][k] += trees[j][k].pop() // 2
                        break
                    # 양분이 있을 경우, 나무 나이 +1
                    else:
                        # 양분 흡수
                        food[j][k] -= trees[j][k][p]
                        # 나무 나이 +1
                        trees[j][k][p] += 1

def fall_winter():
    # 가을 진행
    for j in range(N):
        for k in range(N):
            if trees[j][k]:
                for p in range(len(trees[j][k])):
                    if trees[j][k][p] % 5 == 0:
                        for t in range(8):
                            nx = j + dx[t]
                            ny = k + dy[t]
                            if 0 <= nx < N and 0 <= ny < N:
                                trees[nx][ny].appendleft(1)
            food[j][k] += plusFood[j][k]

for _ in range(K):
    spring_summer()
    fall_winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)