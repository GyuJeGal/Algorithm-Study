import sys, itertools, math

input = sys.stdin.readline

N, M, K = map(int, input().split())

D = []
for _ in range(N):
    d = int(input())
    D.append(d)

D.sort(reverse=True)

# 0 index -> hp, 1 index -> money
boss = []

for _ in range(K):
    a, b = map(int, input().split())
    if D[0] * 900 < a:
        continue
    boss.append([a, b])

candidate = []
result = 0

if len(boss) == 0:
    print(0)
else:
    # 잡을 수 있는 모든 경우의 수 넣기
    for i in range(1, K + 1):
        maxDamage = D[0] * 900
        for cur in itertools.combinations(boss, i):
            hpSum = 0
            for j in cur:
                hpSum += j[0]
            if hpSum <= maxDamage:
                candidate.append(cur)

    # 데미지가 큰 캐릭부터 진행
    for i in range(M):
        # 초당 줄 수 있는 데미지
        damage = D[i]
        # 한 캐릭터가 얻을 수 있는 최대 메소
        maxMoney = 0
        for cur in candidate:
            time = 0
            moneySum = 0
            for hp, money in cur:
                time += math.ceil(hp / damage)
                moneySum += money
            if time <= 900 and maxMoney < moneySum:
                maxMoney = moneySum
        result += maxMoney

    print(result)

# 50분