import math
import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        size = int(math.sqrt(num)) + 1
        for i in range(2, size):
            if num % i == 0:
                return False
        return True

for i in range(m, n + 1):
    if isPrime(i):
        print(i)