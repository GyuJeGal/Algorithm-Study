import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def solution(n, m):
    if m == 1:
        return n % c
    else:
        stan = int(m / 2)
        if m % 2 == 0:
            return (solution(n, stan) ** 2) % c
        else:
            stan = int(m / 2)
            return ((solution(n, stan) ** 2) * n) % c

print(solution(a, b))


