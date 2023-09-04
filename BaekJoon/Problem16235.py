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
answer = M

for _ in range(N):
    temp = list(map(int, input().split()))
    plusFood.append(temp)

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for i in range(K):
    if answer == 0:
        break
    # 가을에 나무를 생성할 좌표
    createQue = collections.deque()

    # 봄, 여름, 겨울 진행
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
                            answer -= 1
                        break
                    # 양분이 있을 경우, 나무 나이 +1
                    else:
                        # 양분 흡수
                        food[j][k] -= trees[j][k][p]
                        # 나무 나이 +1
                        trees[j][k][p] += 1
                        # 나무의 나이가 5의 배수인 경우, createQue에 추가
                        if trees[j][k][p] % 5 == 0:
                            createQue.append([j, k])
                food[j][k] += plusFood[j][k]

            # 나무가 없을 때, 그냥 겨울 진행
            else:
                food[j][k] += plusFood[j][k]
    # 가을 진행
    while createQue:
        x, y = createQue.popleft()
        for j in range(8):
            # 좌표 검사
            if 0 <= x + dx[j] < N and 0 <= y + dy[j] < N:
                trees[x + dx[j]][y + dy[j]].appendleft(1)
                answer += 1

print(answer)