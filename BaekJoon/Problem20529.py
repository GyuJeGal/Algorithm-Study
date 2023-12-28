import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    if n > 32:
        print(0)
    else:
        ans = 100000
        p = []

        def dfs(start):
            global ans
            if len(p) == 3:
                temp = 0
                for i in range(4):
                    if p[0][i] != p[1][i]:
                        temp += 1
                    if p[1][i] != p[2][i]:
                        temp += 1
                    if p[2][i] != p[0][i]:
                        temp += 1
                ans = min(ans, temp)
                return
            for i in range(start, n):
                p.append(arr[i])
                dfs(i + 1)
                p.pop()
        dfs(0)
        print(ans)