import sys
import heapq

input = sys.stdin.readline

# 대학교 개수, 도로의 개수 입력
N, M = map(int, input().split())

# 대학교 성별 입력, 0번째 index는 더미 값임
gender = ['M'] + list(map(str, input().split()))

# 대학교 그래프
graph = [[] for _ in range(N + 1)]

# 연결관계 입력
for _ in range(M):
    v1, v2, weight = map(int, input().split())

    # 사심 경로는 서로 성별이 다른 대학교를 연결하는 도로로만 이루어짐
    if gender[v1] != gender[v2]:
        graph[v1].append([v2, weight])
        graph[v2].append([v1, weight])

visited = [0] * (N + 1)
visited[1] = 1
treeSize = 1

# 최소힙 우선 순위 큐
que = []
# 1과 연결된 도로부터 푸시
for v, w in graph[1]:
    heapq.heappush(que, (w, v))

# 경로 길이
answer = 0

# 종료 조건
while que:
    weight, curVertex = heapq.heappop(que)

    # 중요!!
    # 큐에 (3, 4), (5, 4), (6, 5)가 있다면 우선 순위에 의해 (3, 4) pop
    # 다음으로 (5, 4)가 pop 되는데, 이때 이미 4번 정점은 처리가 되었기 때문에 진행하면 안됨
    # 따라서 pop 된 정점 visited 확인
    if visited[curVertex] == 0:
        answer += weight
        visited[curVertex] = 1
        treeSize += 1

        for v, w in graph[curVertex]:
            if visited[v] == 0:
                heapq.heappush(que, (w, v))

if treeSize == N:
    print(answer)
else:
    print(-1)
