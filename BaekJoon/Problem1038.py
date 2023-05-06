from itertools import combinations
n = int(input())

# 모든 감소하는 수
result = list()
# 1~10개의 조합 만들기, 10자리수가 마지막 수임
for i in range(1, 11):
    for comb in combinations(range(10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        result.append(int("".join(list(map(str, comb)))))

# 오름차순 정렬
result.sort()

if n >= len(result):
    print(-1)

# 인덱스가 넘어 가는 경우 -1 출력. 마지막 수 9876543210
else:
    print(result[n])