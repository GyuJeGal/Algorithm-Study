import math

m = int(input())
n = int(input())

result = []
def solution(num):
    if num == 1:
        return False
    check = int(math.sqrt(num)) + 1
    for i in range(2, check):
        if num % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if solution(i):
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])