n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)
dp[0] = 0

for coin in money:
    for i in range(coin, k + 1):
        if (i - coin) >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])