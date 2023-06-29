import collections
import sys
input = sys.stdin.readline


while True:
    n = input().strip()
    if n == '0':
        break
    else:
        if len(n) % 2 == 0:
            size = int(len(n) / 2)
        else:
            size = int(len(n) / 2) + 1

        result = 'yes'

        for i in range(size):
            if n[i] != n[(len(n) - 1) - i]:
                result = 'no'

        print(result)
