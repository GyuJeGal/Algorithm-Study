import sys, heapq

input = sys.stdin.readline

# 배열의 길이
N = int(input())
# A 배열
A = list(map(int, input().split()))

# 최소 힙 우선순위 큐
que = []
for i in range(N):
    heapq.heappush(que, A[i])

MAX = max(A)
initialMax = MAX

# 결과값 저장
answer = int(1e9)

while True:
    cur = heapq.heappop(que)

    # 이전의 최대-최소 차이와 현재 최대-최소 차이 중 작은 값으로 갱신
    answer = min(answer, MAX - cur)

    MAX = max(MAX, cur * 2)

    heapq.heappush(que, cur * 2)

    # 현재 가장 작은 값이 초기 최댓값일 때 멈춤
    if cur == initialMax:
        break

print(answer)

