n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for i in money:
    for j in range(i, k + 1):
        cases = dp[j - i]
        dp[j] += cases

print(dp[k])
