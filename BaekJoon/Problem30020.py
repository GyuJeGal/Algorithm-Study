import sys

input = sys.stdin.readline

a, b = map(int, input().split())

if a <= b:
    print('NO')
else:
    diff = a - b

    # 만들어야 하는 버거의 개수가 치즈의 개수를 초과하는 경우
    if diff > b:
        print('NO')
    else:
        print('YES')
        print(diff)
        for i in range(diff):
            if i == diff - 1:
                for j in range(a + b):
                    if j % 2 == 0:
                        print('a', end='')
                    else:
                        print('b', end='')
            else:
                print('aba')
                a -= 2
                b -= 1