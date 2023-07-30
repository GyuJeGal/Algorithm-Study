import collections
import sys
input = sys.stdin.readline

S = int(input())

if S == 2:
    print(2)
else:
    que = collections.deque()

    # 제일 처음엔 무조건 화면에 있는 이모티콘을 클립보드에 복사하고 붙여넣기를 해야함
    # 왜냐하면 S가 2 이상의 값이기 때문에 시간은 2부터 시작, ex) [화면의 이모티콘 수, 클립보드의 이모티콘 수, 소요시간]
    que.append([2, 1, 2])
    visit = [([0] * 2000) for _ in range(2000)]
    visit[2][1] = 1

    while que:
        cur = que.popleft()
        if cur[0] + cur[1] == S or cur[0] - 1 == S:
            print(cur[2] + 1)
            break

        # Case1.화면에 붙여넣기
        if cur[0] + cur[1] < 2000 and cur[1] < 2000:
            que.append([cur[0] + cur[1], cur[1], cur[2] + 1])
            visit[cur[0] + cur[1]][cur[1]] = 1

        # Case2.화면에 있는 이모티콘, 클립보드에 복사
        # cur[0] == cur[1]인 경우, 이전에 이미 클립보드에 복사했다는 의미 -> 다시 복사할 필요 없음
        if cur[0] != cur[1] and visit[cur[0]][cur[0]] == 0:
                que.append([cur[0], cur[0], cur[2] + 1])
                visit[cur[0]][cur[0]] = 1

        # Case3.화면에 있는 이모티콘 중 하나를 삭제
        if cur[0] != 2 and visit[cur[0] - 1][cur[1]] == 0:
            que.append([cur[0] - 1, cur[1], cur[2] + 1])
            visit[cur[0] - 1][cur[1]] = 1