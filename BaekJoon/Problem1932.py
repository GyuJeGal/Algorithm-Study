import sys

input = sys.stdin.readline

n = int(input())
dp = []
for i in range(n):
  dp.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(len(dp[i])):
    if j == 0:
      dp[i][j] = dp[i][j] + dp[i - 1][j]
    elif j == len(dp[i])-1:
      dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
    else:
      dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]
print(max(dp[n - 1]))