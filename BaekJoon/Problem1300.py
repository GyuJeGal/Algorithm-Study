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


low = 1
high = int(N * N)
while low + 1 < high:
    mid = int((low + high)/2)
    if countLessOrEquals(mid) < k:
        low = mid
    else:
        high = mid

if countLessOrEquals(low) >= k:
    print(low)
else:
    print(high)
