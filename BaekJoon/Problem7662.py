import sys
import heapq

for T in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    visited = [False] * k
    maxH, minH = [], []
    for i in range(k):
        operation, n = sys.stdin.readline().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(minH, (n, i))
            heapq.heappush(maxH, (-n, i))
            visited[i] = True
        elif n == 1:
            while maxH and not visited[maxH[0][1]]:
                heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                visited[minH[0][1]] = False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    print(-maxH[0][0], minH[0][0]) if maxH and minH else print("EMPTY")