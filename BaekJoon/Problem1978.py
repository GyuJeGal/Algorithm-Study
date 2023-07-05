import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().strip().split()))

def isPrime(m):
    if m == 1:
        return False
    if m < 4:
        return True
    else:
        size = int(m / 2) + 1
        for i in range(2, size):
            if m % i == 0:
                return False
        return True

result = 0
for num in nums:
    if isPrime(num):
        result += 1

print(result)