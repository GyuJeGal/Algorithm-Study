import collections
import sys
input = sys.stdin.readline

# 첫번째 풀이
# N, K = map(int, input().strip().split(' '))
# appliance = list(map(int, input().strip().split(' ')))
#
# multitab = []
# count = 0
#
# for i in range(K):
#     temp = appliance[i]
#     if temp in multitab:
#         continue
#     if len(multitab) < N:
#         multitab.append(temp)
#         continue
#     far = 0
#     check = 0
#     for plug in multitab:
#         if plug not in appliance[i:]:
#             check = plug
#             break
#         elif appliance[i:].index(plug) > far:
#             far = appliance[i:].index(plug)
#             check = plug
#     multitab[multitab.index(check)] = temp
#     count += 1
# print(count)


n, k = map(int, input().strip().split())
use = list(map(int, input().strip().split()))

result = 0

candidate = [collections.deque() for _ in range(101)]
for i in range(k):
    candidate[use[i]].appendleft(i)

multiTab = collections.deque()

for i in use:
    if len(multiTab) == 0:
        multiTab.append(i)
        candidate[i].pop()
    else:
        if i in multiTab:
            candidate[i].pop()
        elif len(multiTab) < n:
            multiTab.append(i)
            candidate[i].pop()
        else:
            far = -1
            index = -1
            for j in range(n):
                if len(candidate[multiTab[j]]) == 0:
                    index = j
                    break
                elif far < candidate[multiTab[j]][-1]:
                    far = candidate[multiTab[j]][-1]
                    index = j
            multiTab[index] = i
            candidate[i].pop()
            result += 1

print(result)



