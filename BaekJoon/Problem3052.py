import sys

result = []

for _ in range(10):
    n = int(sys.stdin.readline())
    result.append(n % 42)

result = set(result)

print(len(result))