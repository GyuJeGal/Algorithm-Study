import sys

input = sys.stdin.readline

# N: 블랙홀 개수, M: 소행성 개수
N, M = map(int, input().split())

# 블랙홀 위치 배열
b = list(map(int, input().split()))
# 블랙홀 위치 정렬
b.sort()

answer = 0

# 소행성 별로 블랙홀에 빨려들어가기 위한 최소 힘 계산
for _ in range(M):
    a, w = map(int, input().split())

    left = 0
    right = N - 1

    # 가장 가까운 블랙홀 위치를 찾는게 필요 -> 이분 탐색
    while left + 1 < right:
        mid = int((left + right) / 2)

        if b[mid] > a:
            right = mid
        else:
            left = mid

    candidate = min(abs(b[left] - a), abs(b[right] - a))

    answer = max(candidate * w, answer)

print(answer)

# 30분 소요