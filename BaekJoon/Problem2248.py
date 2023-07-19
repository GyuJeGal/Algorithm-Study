import sys
input = sys.stdin.readline

N, L, I = map(int, input().strip().split())

dp = [[0 for _ in range(32)] for _ in range(32)]

#dp 테이블에 저장
for i in range(31):
    dp[0][i] = 1
for i in range(1, 32):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 32):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

one_count = 0
cur_count = 0
for i in reversed(range(1, N + 1)):
    if i == 1:
        if I > cur_count + 1:
            print(1, end='')
        else:
            print(0, end='')
    elif I > cur_count + dp[i - 1][L - one_count]:
        cur_count += dp[i - 1][L - one_count]
        one_count += 1
        print(1, end='')
    else:
        print(0, end='')
