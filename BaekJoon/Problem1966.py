import sys

input = sys.stdin.readline

c = int(input())
for i in range(c):
    n, m = map(int, input().split())
    # 입력 리스트, 입력 당시의 순서를 기록할 리스트
    my_list = list(map(int, input().split()))
    order_list = [x for x in range(len(my_list))]

    cnt = 0
    while True:
        # 맨 앞의 원소가 가장 클 때
        if my_list[0] >= max(my_list):
            cnt += 1
            # m번째 원소가 맞다면 스탑
            if order_list[0] == m:
                break
            else:  # 그렇지 않은 경우 계속 반복
                my_list = my_list[1:]
                order_list = order_list[1:]
        # 맨 앞의 원소가 가장 크지는 않은 경우
        else:
            my_list = my_list[1:] + my_list[:1]
            order_list = order_list[1:] + order_list[:1]
    print(cnt)