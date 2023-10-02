import sys

input = sys.stdin.readline

# N: 용맥의 수, H: 몬스터의 체력
N, H = map(int, input().split())

# 용맥의 종류 문자열 입력
inputStr = input()

# 용맥의 종류에 따라 0(S), 1(R), 2(W)로 저장
dragonVein = []
for i in range(N):
    if inputStr[i] == 'S':
        dragonVein.append(0)
    elif inputStr[i] == 'R':
        dragonVein.append(1)
    else:
        dragonVein.append(2)

# 몬스터의 체력이 4이상인 경우 모든 몬스터 처치 불가 가능성
if H >= 4:
    # 몬스터가 한 마리인 경우 0번으로 가능
    if N == 1:
        print(0)
    # 몬스터가 두 마리인 경우
    elif N == 2:
        # 두 용맥의 타입이 같으면 용맥 변환 1번 필수
        if dragonVein[0] == dragonVein[1]:
            print(1)
        # 두 용맥의 타압이 다르면 0번으로 가능
        else:
            print(0)
    # 몬스터가 세 마리인 경우 -> 같은 타입의 용맥의 개수에 따라 횟수 결정
    # 용맥 타입 3 중복 -> 용맥 변환 2번 필요
    # 용맥 타입 2 중복 -> 용맥 변환 1번 필요
    # 용맥 타입 중복 없음 -> 용맥 변환 0번 필요
    elif N == 3:
        lst = [0, 0, 0]
        answer = 0
        for i in range(3):
            lst[dragonVein[i]] += 1
        for i in range(3):
            if lst[i] == 0:
                answer += 1
        print(answer)
    # 몬스터가 네 마리 이상인 경우 -> 한 몬스터를 잡기 전에 다음 용맥으로 이동하기 때문
    else:
        print(-1)
else:
    answer = 0
    # 체력이 1인 경우 -> 0번으로 다 가능
    if H == 1:
        print(answer)
    # 체력이 2인 경우
    elif H == 2:
        # 첫 인덱스 부터 돌면서 다음 인덱스 값이랑 타입이 중복되면 다다음 인덱스 값까지 3개의 데이터 확인하면서 용맥 변환
        for i in range(N - 1):
            # 다음 인덱스와 중복되는 경우
            if dragonVein[i] == dragonVein[i + 1]:
                # 마지막 인덱스 일때 용맥 변환 아무거나 한번
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
        # 가능한 6가지의 용맥 타입 리스트를 저장
        lst = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        count = [0] * 6
        # 각 용맥 타입 리스트를 돌면서 차이가 얼마나 나는지 계산
        for i in range(N):
            for j in range(6):
                if dragonVein[i] != lst[j][i % 3]:
                    count[j] += 1
        # 가장 차이가 덜 나는 횟수를 결과값으로 반환
        answer = min(count)
        print(answer)