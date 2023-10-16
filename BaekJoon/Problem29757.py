import heapq
import sys

input = sys.stdin.readline

# 점의 개수
N = int(input())

# 우선순위 큐
que = []

for i in range(1, N + 1):
    x, y = map(int, input().split())
    # 우선순위 큐에 저장할 때, y 좌표에 대해서는 최대 힙, x 좌표에 대해서는 최소 힙으로 해서 푸시
    heapq.heappush(que, [-y, x, i])

# 결과값 저장
answer = []

# 우선순위 큐에 이전에 나온 점이랑 현재 점이랑 연결하면 트리 완성 가능
# y 좌표가 같은 점에 대해서는 오른쪽으로 연결되고, y 좌표가 밑에 있으면 왼쪽 밑으로 연결
before = heapq.heappop(que)
for i in range(N - 1):
    cur = heapq.heappop(que)
    answer.append([before[2], cur[2]])
    before = cur

for a, b in answer:
    print(a, b)

# 11분 소요