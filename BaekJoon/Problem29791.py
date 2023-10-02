import sys

input = sys.stdin.readline

# 각 스킬 사용 횟수
N, M = map(int, input().split())

# 스킬 노바를 누른 시점
nova = list(map(int, input().split()))
# 스킬 오리진을 누른 시점
origin = list(map(int, input().split()))

# 각 스킬에 대한 면역 시간
novaIgnore = 0
originIgnore = 0

# 각 스킬의 쿨타임
nCoolTime = 0
oCoolTime = 0

# 각 스킬이 들어간 결과값
novaResult = 0
originResult = 0

# 스킬을 누른 시간이 뒤죽박죽 입력되므로 정렬 필요
nova.sort()
origin.sort()

# 스킬 노바에 대해 결과 계산
for i in nova:
    if nCoolTime <= i:
        if novaIgnore <= i:
            nCoolTime = i + 100
            novaIgnore = i + 90
            novaResult += 1
        else:
            nCoolTime = i + 100

# 스킬 오리진에 대해 결과 계산
for i in origin:
    if oCoolTime <= i:
        if originIgnore <= i:
            oCoolTime = i + 360
            originIgnore = i + 90
            originResult += 1
        else:
            oCoolTime = i + 100

print(novaResult, originResult)