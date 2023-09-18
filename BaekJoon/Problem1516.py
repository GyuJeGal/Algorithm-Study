import collections
import sys

input = sys.stdin.readline

N = int(input())

# 짓는데 걸리는 시간
buildTime = [0] * (N + 1)
# 인접차수
inDegree = [0] * (N + 1)
# 연결관계
graph = [[] for _ in range(N + 1)]
# 결과
answer = [0] * (N + 1)

# 연결 관계 입력
for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    for j in range(len(inputList)):
        if j == 0:
            buildTime[i] = inputList[j]
        elif j < len(inputList) - 1:
            graph[inputList[j]].append(i)
            inDegree[i] += 1

# 위상 정렬을 위한 초기 세팅
que = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        que.append([i, 0])

# 위상정렬 시작
while que:
    v, t = que.popleft()
    # 해당 건물 결과값 저장
    answer[v] = t + buildTime[v]

    # 연결된 건물들 순회
    for i in graph[v]:
        # 인접 차수 빼기
        inDegree[i] -= 1
        # 어떤 건물을 짓기전 선행 건물이 완료된 최대 시간 저장
        answer[i] = max(answer[i], t + buildTime[v])

        # 만약 인접 차수가 0인 경우 큐에 넣기
        if inDegree[i] == 0:
            # 선행 건물이 완료된 최대 시간을 큐에 넣기
            que.append([i, max(t + buildTime[v], answer[i])])

for i in range(1, N + 1):
    print(answer[i], end=' ')