# 좌우로 더 높은 블록으로 둘러 싸여있는 경우 물이 고임
# 중요!! 자신 보다 높은, 왼쪽과 오른쪽 중 더 낮은 블록까지 물이 고임

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0  # 빗물의 고인 양
for i in range(1, W - 1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없다.
    left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
    right_max = max(blocks[i + 1:])  # 오른쪽에서 제일 높은 블록

    limit = min(left_max, right_max)  # 그 중 가장 낮은 블록

    if blocks[i] < limit:  # 현재 블록이 limit 블록 보다는 낮아야 빗물이 고인다.
        result += limit - blocks[i]
print(result)