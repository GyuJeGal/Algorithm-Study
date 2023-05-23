from collections import deque

N, K = map(int, input().split(' '))

min_time = 0
case_size = 0

if N > K:
    print(N - K)
    print(1)
else:
    que = deque()
    que.append(N)
    visited = [0] * 100001

    while len(que) > 0:
        pos = que.popleft()
        time = visited[pos]
        if pos == K:
            if min_time == 0:
                min_time = time
                case_size = 1
            elif min_time > time:
                min_time = time
                case_size = 1
            elif min_time == time:
                case_size += 1
        else:
            if min_time != 0:
                if time >= min_time:
                    continue
            for candidate in [pos + 1, pos * 2, pos - 1]:
                if 0 <= candidate < 100001:
                    if visited[candidate] == 0 or visited[candidate] == visited[pos] + 1:
                        que.append(candidate)
                        visited[candidate] = time + 1

    print(min_time)
    print(case_size)