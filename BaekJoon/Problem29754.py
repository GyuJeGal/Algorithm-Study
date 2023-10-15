import sys

input = sys.stdin.readline

# N: 방송의 수, M: 마지막으로 방송을 본 날짜
N, M = map(int, input().split())

# 확인해야 할 총 주차 개수
totalWeek = int((M - 1) / 7) + 1

# 유튜버 이름 저장
youtuber = []
# key(유튜버 이름) : value(인덱스)
d = {}
# 각 인덱스에 주차별로 방송 횟수 저장
count = []
# 각 인덱스에 주차별로 방송 시간 저장
time = []

for _ in range(N):
    name, day, start, end = input().split()

    week = int((int(day) - 1) / 7)

    startHour, startMin = map(int, start.split(":"))
    endHour, endMin = map(int, end.split(":"))

    duration = (endHour - startHour) * 60 + (endMin - startMin)

    if name not in youtuber:
        index = len(youtuber)
        d[name] = index
        youtuber.append(name)
        count.append([0] * totalWeek)
        time.append([0] * totalWeek)
        count[index][week] += 1
        time[index][week] += duration

    else:
        index = d[name]
        count[index][week] += 1
        time[index][week] += duration

answer = []

for i in range(len(youtuber)):
    check = 0
    for j in range(totalWeek):
        if count[i][j] < 5 or time[i][j] < 3600:
            check = 1
            break
    if check == 0:
        answer.append(youtuber[i])

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)

# 30분 소요