import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nova = list(map(int, input().split()))
origin = list(map(int, input().split()))

novaIgnore = 0
novaResult = 0

nCoolTime = 0
oCoolTime = 0

originIgnore = 0
originResult = 0

nova.sort()
origin.sort()

for i in nova:
    if nCoolTime <= i:
        if novaIgnore <= i:
            nCoolTime = i + 100
            novaIgnore = i + 90
            novaResult += 1
        else:
            nCoolTime = i + 100

for i in origin:
    if oCoolTime <= i:
        if originIgnore <= i:
            oCoolTime = i + 360
            originIgnore = i + 90
            originResult += 1
        else:
            oCoolTime = i + 100

print(novaResult, originResult)

## 25분 -> 간단한 syntax 에러