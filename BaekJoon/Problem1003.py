import sys
import collections

T = int(sys.stdin.readline())
que = collections.deque()

zeroCount = [1, 0]
oneCount = [0, 1]

for i in range(2, 41):
    zeroCount.append(zeroCount[i - 1] + zeroCount[i - 2])
    oneCount.append(oneCount[i - 1] + oneCount[i - 2])

for _ in range(T):
    n = int(sys.stdin.readline())
    print(zeroCount[n], oneCount[n])