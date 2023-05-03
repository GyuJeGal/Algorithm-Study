N = int(input())
candy = [list(input()) for _ in range(N)]
result = 1

# 상하 방향 연속 되는 사탕 최대 개수 찾기
def downCheck(i, N):
    maximum = 1
    count = 1
    mem = candy[0][i]
    for j in range(1, N):
        if mem == candy[j][i]:
            count += 1
            if j == N - 1:
                maximum = max(count, maximum)
        else:
            maximum = max(count, maximum)
            count = 1
            mem = candy[j][i]
    return maximum

# 좌우 방향 연속 되는 사탕 최대 개수 찾기
def rightCheck(i, N):
    maximum = 1
    count = 1
    mem = candy[i][0]
    for j in range(1, N):
        if mem == candy[i][j]:
            count += 1
            if j == N - 1:
                maximum = max(count, maximum)
        else:
            maximum = max(count, maximum)
            count = 1
            mem = candy[i][j]
    return maximum

for i in range(N):
    result = max(result, downCheck(i, N))
    result = max(result, rightCheck(i, N))

for i in range(N - 1):
    for j in range(N):
        if candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            result = max(result, downCheck(j, N))
            result = max(result, rightCheck(i, N))
            result = max(result, rightCheck(i + 1, N))
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

    for j in range(N - 1):
        if candy[j][i] != candy[j][i + 1]:
            candy[j][i], candy[j][i + 1] = candy[j][i + 1], candy[j][i]
            result = max(result, rightCheck(j, N))
            result = max(result, downCheck(i, N))
            result = max(result, downCheck(i + 1, N))
            candy[j][i], candy[j][i + 1] = candy[j][i + 1], candy[j][i]

print(result)