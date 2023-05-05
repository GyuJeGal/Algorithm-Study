n = int(input())
house = [list(map(int, input())) for _ in range(n)]

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
result = []

# 상하좌우로 순회하면서 인접한 집 개수 세는 메서드
def check(i, j):
    que = [(i, j)]
    count = 1
    while len(que) != 0:
        (r, c) = que.pop(0)
        for k in range(4):
            if (r + dir_x[k]) < 0 or (r + dir_x[k]) >= n:
                continue
            elif (c + dir_y[k]) < 0 or (c + dir_y[k]) >= n:
                continue
            else:
                if house[r + dir_x[k]][c + dir_y[k]] == 1:
                    que.append((r + dir_x[k], c + dir_y[k]))
                    house[r + dir_x[k]][c + dir_y[k]] = 0
                    count += 1
    return count


for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            house[i][j] = 0
            result.append(check(i, j))

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])

