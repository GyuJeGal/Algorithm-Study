import sys

input = sys.stdin.readline

# N: 백준에서 해결한 문제 수, N: 유니온 레벨, L: 최고 레벨
N, U, L = map(int, input().split())

# 선행 조건
if N >= 1000:
    # 다음 조건
    if U >= 8000 or L >= 260:
        print('Very Good')
    else:
        print('Good')
# 선행 조건 불만족
else:
    print('Bad')