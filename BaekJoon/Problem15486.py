import sys

n = int(sys.stdin.readline())

days = [0]
price = [0]

for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    days.append(t)
    price.append(p)

dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    if i + days[i] <= n + 1:
        dp[i + days[i]] = max(dp[i + days[i]], dp[i] + price[i])

print(dp[n + 1])
