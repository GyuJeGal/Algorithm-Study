import sys

input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

# 대소 관계 그래프
# Ex) graph[1][2] == 1이면 1 > 2이라는 의미
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 대소 관계 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 자기 자신으로의 대소 관계 0으로 설정
for i in range(1, N + 1):
    graph[i][i] = 0

# 플로이드 워셜 진행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 대소관계가 그리지면 1로 설정
            if graph[i][k] != INF and graph[k][j] != INF:
                graph[i][j] = 1

# N까지 연산 불가능한 물건 개수 세기
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        # i > j 관계, i < j 관계 확인 -> 둘다 관계가 없는 경우 -> count 증가
        if graph[i][j] == INF and graph[j][i] == INF:
            count += 1
    print(count)

