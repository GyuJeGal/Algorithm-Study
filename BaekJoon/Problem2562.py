import sys
input = sys.stdin.readline

result = 0
index = 0

for i in range(1, 10):
    m = int(input())
    if result < m:
        result = m
        index = i

print(result)
print(index)