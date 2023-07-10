import collections
import sys
input = sys.stdin.readline

# 집의 개수
INF = 2147000000
n = int(input())

# 집을 R, G, B로 칠하는 비용 저장
cost = [[0, 0, 0]]

# 1번 집부터 R, G, B 비용 추가하기
for i in range(n):
    r, g, b = map(int, input().strip().split())
    cost.append([r, g, b])

result = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n + 1)]
    dp[1][i] = cost[1][i]
    for j in range(2, n + 1):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            result = min(result, dp[n][j])
print(result)