import sys

input = sys.stdin.readline

N, H = map(int, input().split())

inputStr = input()
dragonVein = []
for i in range(N):
    if inputStr[i] == 'S':
        dragonVein.append(0)
    elif inputStr[i] == 'R':
        dragonVein.append(1)
    else:
        dragonVein.append(2)


if H >= 4:
    if N == 1:
        print(0)
    elif N == 2:
        if dragonVein[0] == dragonVein[1]:
            print(1)
        else:
            print(0)
    elif N == 3:
        lst = [0, 0, 0]
        answer = 0
        for i in range(3):
            lst[dragonVein[i]] += 1
        for i in range(3):
            if lst[i] == 0:
                answer += 1
        print(answer)

    else:
        print(-1)
else:
    answer = 0
    if H == 1:
        print(answer)
    elif H == 2:
        for i in range(N - 1):
            if dragonVein[i] == dragonVein[i + 1]:
                # 마지막 인덱스 일때
                if i == N - 2:
                    answer += 1
                    break
                # 첫번째랑 세번째가 같은 경우
                if dragonVein[i] == dragonVein[i + 2]:
                    dragonVein[i + 1] = (dragonVein[i] + 1) % 3
                # 첫번째랑 세번째가 다른 경우
                else:
                    visit = [0, 0 ,0]
                    visit[dragonVein[i]] = 1
                    visit[dragonVein[i + 2]] = 1
                    for j in range(3):
                        if visit[j] == 0:
                            dragonVein[i + 1] = j
                answer += 1
        print(answer)
    # H == 3일때
    else:
        lst = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        count = [0] * 6
        for i in range(N):
            for j in range(6):
                if dragonVein[i] != lst[j][i % 3]:
                    count[j] += 1
        answer = min(count)
        print(answer)

# 50분 걸림 -> 2시간 중 10분 초과