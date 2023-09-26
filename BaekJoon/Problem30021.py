import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print('YES')
    print(1)
elif N == 2:
    print('NO')
else:
    result = [1, 3, 2]

    for i in range(4, N + 1):
        result.append(i)

    # 결과 출력
    print('YES')
    for i in result:
        print(i, end=' ')