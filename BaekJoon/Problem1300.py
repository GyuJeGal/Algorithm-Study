import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

def countLessOrEquals(mid):
    result = 0
    for i in range(1, N + 1):
        if i > mid:
            break
        else:
            if int(mid/i) >= N:
                result += N
            else:
                result += int(mid/i)
    return result


left = 1
right = int(N * N)
result = 0
while left <= right:
    mid = int((left + right)/2)
    if countLessOrEquals(mid) >= k:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)
