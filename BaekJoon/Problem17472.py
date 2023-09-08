import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
groupCount = 1

# 입력받은 지도
inputMap = [list(map(int, input().split())) for _ in range(N)]

# 섬의 그룹 번호를 포함한 지도
groupMap = [[[] for _ in range(M)] for _ in range(N)]

# 지도에 1인 위치 다 저장
oneLoc = []

# 주어진 좌표와 연결된 1을 그룹핑하기
def grouping(x, y, groupNumber):
    que = []
    visited = []
    que.append((x, y))
    while que:
        cur = que.pop()
        oneLoc.append(cur)
        groupMap[cur[0]][cur[1]].append(1)
        groupMap[cur[0]][cur[1]].append(groupNumber)
        visited.append(cur)
        for i in range(4):
            if 0 <= cur[0] + dx[i] < N and 0 <= cur[1] + dy[i] < M:
                if (cur[0] + dx[i], cur[1] + dy[i]) not in visited:
                    if inputMap[cur[0] + dx[i]][cur[1] + dy[i]] == 1:
                        inputMap[cur[0] + dx[i]][cur[1] + dy[i]] = -1
                        que.append((cur[0] + dx[i], cur[1] + dy[i]))

for i in range(N):
    for j in range(M):
        if inputMap[i][j] == 0:
            groupMap[i][j].append(0)
            groupMap[i][j].append(0)
        # 1 만나면 그룹핑하기
        elif inputMap[i][j] == 1:
            grouping(i, j, groupCount)
            groupCount += 1

# 그룹 간 연결 정보
graph = [[] for _ in range(groupCount)]

# 그룹 간 연결 정보 계산
for loc in oneLoc:
    x, y = loc[0], loc[1]
    curGroupNumber = groupMap[x][y][1]
    for i in range(4):
        count = 1
        while True:
            # 지도 범위 벗어나는지 체크
            if 0 <= x + dx[i] * count < N and 0 <= y + dy[i] * count < M:
                nx = x + dx[i] * count
                ny = y + dy[i] * count
                if groupMap[nx][ny][0] == 0:
                    count += 1
                # 다리를 잇는 도중 1을 만난 경우
                else:
                    # 그룹 번호가 현재 그룹 번호와 다른지 확인 + 다리의 길이가 2 이상인 지 확인
                    if groupMap[nx][ny][1] != curGroupNumber and count > 2:
                        # 이미 연결관계가 있는지 체크하는 변수
                        modify = 0
                        for ele in graph[curGroupNumber]:
                            # 연결관계가 이미 존재하면 더 짧은 거리의 다리로 연결
                            if ele[0] == groupMap[nx][ny][1]:
                                modify = 1
                                ele[1] = min(ele[1], count - 1)
                                break
                        # 연결관계가 없는 경우, 그냥 추가
                        if modify == 0:
                            graph[curGroupNumber].append([groupMap[nx][ny][1], count - 1])
                        break
                    # 같은 그룹 번호를 만났거나 or 다른 그룹을 만났지만 다리의 길이가 2 미만인 경우
                    else:
                        break
            # 지도 범위를 벗어나는 경우
            else:
                break

# 결과
answer = 0

for i in range(1, groupCount):
    if len(graph[i]) == 0:
        answer = -1
        break

if answer == -1:
    print(answer)
else:
    # 트리에 포함된 번호
    treeGroup = [1]

    # treeGroup의 사이즈
    groupSize = 1

    # 최소 힙 리스트
    que = []

    # 초기 세팅
    for i in graph[1]:
        heapq.heappush(que, (i[1], 1, i[0]))

    while groupSize < groupCount - 1:
        # 우선순위 큐가 비어있는 경우
        if len(que) == 0:
            answer = -1
            break

        weight, vertex1, vertex2 = heapq.heappop(que)
        # cycle이 생기는 경우
        if vertex2 in treeGroup:
            continue
        # 트리에 추가해야 되는 경우
        else:
            # 트리에 추가
            treeGroup.append(vertex2)
            groupSize += 1
            answer += weight
            # 정점 2와 연결된 간선 푸시
            for connect in graph[vertex2]:
                # 방문되지 않은 정점에 대한 간선만 푸시
                if connect[0] not in treeGroup:
                    heapq.heappush(que, (connect[1], vertex2, connect[0]))

    print(answer)