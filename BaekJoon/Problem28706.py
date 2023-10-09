import sys

input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 턴의 개수
    N = int(input())

    # 7로 나눈 나머지를 저장할 배열
    result = [0] * 7
    # 처음 주어진 나머지는 1
    result[1] = 1

    for _ in range(N):
        # 입력 받으면서 나머지 저장할 배열
        temp = [0] * 7

        op1, v1, op2, v2 = map(str, input().split())
        v1 = int(v1)
        v2 = int(v2)

        # result를 순회하면서 1이면 temp에 나머지 저장
        for i in range(7):
            if result[i] == 1:
                if op1 == "+":
                    temp[(i + v1) % 7] = 1
                else:
                    temp[(i * v1) % 7] = 1

                if op2 == "+":
                    temp[(i + v2) % 7] = 1
                else:
                    temp[(i * v2) % 7] = 1

        # result 배열 temp로 갱신
        result = temp.copy()

    # result[0] == 1이면 7로 나눈 나머지가 0이라는 의미
    if result[0] == 1:
        print("LUCKY")
    else:
        print("UNLUCKY")