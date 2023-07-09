import collections
import sys

input = sys.stdin.readline

n = int(input().strip())
stack = collections.deque()
result = collections.deque()
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in result:
        print(i)

