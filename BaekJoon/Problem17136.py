import sys
input = sys.stdin.readline

paper = [list(map(int, input().split())) for _ in range(10)]

remain = [0, 5, 5, 5, 5, 5]
answer = 25

def findSize(i, j):
    size = 1
    while True:
        if size == 5:
            break
        flag = 0
        for col in range(size + 1):
            if i + size >= 10 or j + col >= 10:
                flag = 1
                break
            elif paper[i + size][j + col] != 1:
                flag = 1
                break
        for row in range(size + 1):
            if i + row >= 10 or j + size >= 10:
                flag = 1
                break
            if paper[i + row][j + size] != 1:
                flag = 1
                break
        if flag == 1:
            break
        else:
            size += 1
    return size

def dfs(x, y, candidate):
    global answer, remain
    # 종료 조건
    if x >= 10:
        answer = min(answer, candidate)
        return
    # 오른쪽으로 색종이 사이즈를 넘어선 경우, 다음 열로 이동
    if y >= 10:
        dfs(x + 1, 0, candidate)
        # 다음 열로 이동하고, 함수 끝나면 다음 줄이 실행되지 않도록 return 해주기!!
        return
    # 색종이에서 현재 위치가 1인 경우
    if paper[x][y] == 1:
        # 현재 위치에서 최대로 붙일 수 있는 색종이의 크기
        size = findSize(x, y)
        # 색종이를 붙일 수 있는 크기 다 붙여보기
        for i in range(1, size + 1):
            # 붙일려고 하는 색종이가 없을 경우, 다음 크기로 진행
            if remain[i] == 0:
                continue
            # 색종이 붙이기
            for j in range(i):
                for k in range(i):
                    paper[x + j][y + k] = 0
            remain[i] -= 1
            dfs(x, y + i, candidate + 1)
            # 색종이 다시 떼기
            remain[i] += 1
            for j in range(i):
                for k in range(i):
                    paper[x + j][y + k] = 1
    # 색종이에서 현재 위치가 0인 경우
    else:
        dfs(x, y + 1, candidate)

dfs(0, 0, 0)
if answer == 25:
    print(-1)
else:
    print(answer)

