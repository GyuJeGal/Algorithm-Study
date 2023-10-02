import sys

input = sys.stdin.readline

# N: 용사의 수, M: 탑의 층수, K: 사냥하는 기간
N, M, K = map(int, input().split())

# 용사 레벨 리스트 입력
hero = list(map(int, input().split()))

# 몬스터 레벨 리스트 입력
monster = list(map(int, input().split()))

# 모든 히어로가 각 층을 몇 번 방문하는지 저장
visit = [0] * M

for h in hero:
    candidate = [[monster[i], i] for i in range(M)]
    candidate.sort()

    # 히어로가 사냥 가능한 일수 계산
    day = min(K, 200 - h)

    point = 0
    for i in range(M):
        if candidate[i][0] <= h:
            point = i
        else:
            break

    while day > 0:
        nextLevel = 0
        # 현재 사냥할 몬스터 보다 더 높은 레벨이 없는 경우
        if point == M - 1:
            nextLevel = day
        # 다음 몬스터를 잡기 위해 올려하는 레벨
        else:
            nextLevel = min(candidate[point + 1][0] - h, day)

        visit[candidate[point][1]] += nextLevel
        h += nextLevel
        day -= nextLevel
        point += 1

# 처음 층은 무시 가능 -> 어차피 시간 소요 안함
visit[0] = 0

firstPos = 1
secondPos = 2
answer = 0

# 원래 걸리는 시간
originTime = 0
for i in range(1, M):
    originTime += i * visit[i]

# i는 0층과 연결할 다른 층수를 의미
for i in range(1, M):
    time = 0
    for j in range(1, M):
        if i == j or visit[j] == 0:
            continue
        nearDistance = min(abs(i - j), j)
        time += nearDistance * visit[j]

    # 절약한 시간이 더 크면 갱신
    if answer < originTime - time:
        answer = originTime - time
        secondPos = i + 1

print(firstPos, secondPos)
print(answer)