import sys, itertools, math

input = sys.stdin.readline

# N: 캐릭터 개수, M: 하루에 사용할 캐릭터 개수, K: 보스의 가짓수
N, M, K = map(int, input().split())

# D: 각 캐릭터의 1초당 데미지 저장
D = []
for _ in range(N):
    d = int(input())
    D.append(d)

# 데미지를 오름차순으로 정렬
D.sort(reverse=True)

# 0 index -> hp, 1 index -> money
boss = []

# 줄 수 있는 최대 데미지
maxDamage = D[0] * 900

for _ in range(K):
    a, b = map(int, input().split())

    # 보스의 체력 및 얻을 수 있는 메소를 입력 받을때, 보스 체력이 줄 수 있는 최대 데미지 보다 높으면 무시
    if maxDamage < a:
        continue
    # 가능한 보스 체력이면 boss 리스트에 추가
    boss.append([a, b])

# 잡을 수 있는 보스 경우의 수 저장
# Ex) [[[900, 30]], [[1800, 40]], [[2700, 50]], [[900, 30], [1800, 40]], [[900, 30], [2700, 50]]]
candidate = []

# 하루에 얻을 수 있는 최대 메소 결과값
result = 0

# 잡을 수 있는 보스가 없는 경우 0 반환
if len(boss) == 0:
    print(0)

else:
    # 잡을 수 있는 모든 경우의 수 넣기
    for i in range(1, K + 1):
        # 파이썬에서 제공하는 조합 라이브러리 이용
        for cur in itertools.combinations(boss, i):
            hpSum = 0
            for j in cur:
                hpSum += j[0]
            # 잡을 수 있는 경우만 저장
            if hpSum <= maxDamage:
                candidate.append(cur)

    # 데미지가 큰 캐릭부터 진행
    for i in range(M):
        # 초당 줄 수 있는 데미지
        damage = D[i]
        # 한 캐릭터가 얻을 수 있는 최대 메소
        maxMoney = 0

        # 모든 경우의 수를 확인하면서 한 캐릭터가 얻을 수 있는 최대 메소 갱신
        for cur in candidate:
            time = 0
            moneySum = 0
            for hp, money in cur:
                time += math.ceil(hp / damage)
                moneySum += money
            if time <= 900 and maxMoney < moneySum:
                maxMoney = moneySum
        # 결과값에 추가
        result += maxMoney

    print(result)