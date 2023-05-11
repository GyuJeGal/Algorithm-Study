# n = int(input())
# house = [list(map(int, input().split(' '))) for _ in range(n)]
# result = 0
#
# def checkPositon(pipe):
#     a, b = pipe[0], pipe[1]
#     c, d = pipe[2], pipe[3]
#     if a == c and b + 1 == d:
#         return 'horizontal'
#     elif b == d and a + 1 == c:
#         return 'vertical'
#     else:
#         return 'diagonal'
#
# que = [[0, 0, 0, 1]]
# while len(que) > 0:
#     pipe = que.pop()
#     if pipe[2] == n - 1 and pipe[3] == n - 1:
#         result += 1
#     else:
#         if checkPositon(pipe) == 'horizontal':
#             if pipe[3] + 1 < n:
#                 # 그냥 가로로 밀기, 대각선 밑으로 밀기 둘다 가능
#                 if pipe[2] + 1 < n:
#                     if house[pipe[2]][pipe[3] + 1] != 1:
#                         que.append([pipe[0], pipe[1] + 1, pipe[2], pipe[3] + 1])
#                         if house[pipe[2] + 1][pipe[3]] == 0 and house[pipe[2] + 1][pipe[3] + 1] == 0:
#                             que.append([pipe[0], pipe[1] + 1, pipe[2] + 1, pipe[3] + 1])
#                 # 가로로 밀기만 가능
#                 else:
#                     if house[pipe[2]][pipe[3] + 1] != 1:
#                         que.append([pipe[0], pipe[1] + 1, pipe[2], pipe[3] + 1])
#         elif checkPositon(pipe) == 'vertical':
#             if pipe[2] + 1 < n:
#                 # 그냥 세로로 밀기, 대각선 밑으로 밀기 둘다 가능
#                 if pipe[3] + 1 < n:
#                     if house[pipe[2] + 1][pipe[3]] != 1:
#                         que.append([pipe[0] + 1, pipe[1], pipe[2] + 1, pipe[3]])
#                         if house[pipe[2]][pipe[3] + 1] == 0 and house[pipe[2] + 1][pipe[3] + 1] == 0:
#                             que.append([pipe[0] + 1, pipe[1], pipe[2] + 1, pipe[3] + 1])
#                 # 세로로 밀기만 가능
#                 else:
#                     if house[pipe[2] + 1][pipe[3]] != 1:
#                         que.append([pipe[0] + 1, pipe[1], pipe[2] + 1, pipe[3]])
#         else:
#             if pipe[3] + 1 < n:
#                 # 세 방향으로 밀기 다 가능
#                 if pipe[2] + 1 < n:
#                     if house[pipe[2]][pipe[3] + 1] != 1:
#                         que.append([pipe[0] + 1, pipe[1] + 1, pipe[2], pipe[3] + 1])
#                     if house[pipe[2] + 1][pipe[3]] != 1:
#                         que.append([pipe[0] + 1, pipe[1] + 1, pipe[2] + 1, pipe[3]])
#                     if house[pipe[2]][pipe[3] + 1] != 1 and house[pipe[2] + 1][pipe[3]] != 1 and house[pipe[2] + 1][pipe[3] + 1] != 1:
#                         que.append([pipe[0] + 1, pipe[1] + 1, pipe[2] + 1, pipe[3] + 1])
#                 # 가로로 밀기만 가능
#                 else:
#                     if house[pipe[2]][pipe[3] + 1] != 1:
#                         que.append([pipe[0] + 1, pipe[1] + 1, pipe[2], pipe[3] + 1])
#             else:
#                 # 세로로 밀기만 가능
#                 if pipe[2] + 1 < n:
#                     if house[pipe[2] + 1][pipe[3]] != 1:
#                         que.append([pipe[0] + 1, pipe[1] + 1, pipe[2] + 1, pipe[3]])
# print(result)

import sys

N = int(input())
home = [list(map(int, input().split(' '))) for _ in range(N)]

DP = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# 0 가로, 1 세로, 2 대각선

DP[0][0][1] = 1
for i in range(2,N):
    if home[0][i] == 0:
        DP[0][0][i] = DP[0][0][i - 1]

for i in range(1,N):
    for j in range(1,N):
        if home[i][j] == 0 and home[i][j - 1] == 0 and home[i - 1][j] == 0:
            DP[2][i][j] = DP[0][i - 1][j - 1] + DP[1][i - 1][j - 1] + DP[2][i - 1][j - 1]
            # 대각선 파이프 놓기

        if home[i][j] == 0:
            DP[0][i][j] = DP[0][i][j - 1] + DP[2][i][j - 1]
            # 가로 파이프 놓기

            DP[1][i][j] = DP[1][i - 1][j] + DP[2][i - 1][j]
            # 세로 파이프 놓기
print(DP[0][N - 1][N - 1] + DP[1][N - 1][N - 1] + DP[2][N - 1][N - 1])