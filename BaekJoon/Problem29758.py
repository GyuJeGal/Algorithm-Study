import math
import sys

input = sys.stdin.readline

# 테스트 케이스
T = int(input())

for _ in range(T):
    N, L = map(int, input().split())

    # N이 70,000이어도 최대 5자리까지 가능
    if L > 5:
        print(0)
    else:
        dp = [[0] * 70001 for _ in range(L + 1)]
        dp[1][N] = 1

        for i in range(1, L):
            for j in range(2, N + 1):
                if dp[i][j] > 0:
                    size = 0
                    # j가 16일때, sqrt(j) == int(sqrt(j)) == 4로 일치
                    # 이 경우 다음 for 문이 1부터 (4 - 1)까지 돌아야 함
                    if math.sqrt(j) == int(math.sqrt(j)):
                        size = int(math.sqrt(j))
                    # j가 17일때, sqrt(j) != int(sqrt(j))로 불일치
                    # 이 경우 다음 for 문이 1부터 (4)까지 돌아야 함
                    else:
                        size = int(math.sqrt(j)) + 1

                    for k in range(1, size):
                        dp[i + 1][k] += dp[i][j]

        print(dp[L][1])