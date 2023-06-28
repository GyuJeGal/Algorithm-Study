import sys
input = sys.stdin.readline

n = int(input())

result = []

for _ in range(n):
    str = input().strip()
    result.append(str)

result = set(result)
result = list(result)

result.sort()
result.sort(key=len)

for str in result:
    print(str)