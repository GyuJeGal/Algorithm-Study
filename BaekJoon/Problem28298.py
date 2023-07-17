import collections
import sys
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

tile = collections.deque()
for _ in range(n):
    tile.append(list(input().strip()))

result = 0
result_tile = [[] for _ in range(k)]

for i in range(k):
    for j in range(k):
        most = 0
        most_count = 0
        alpha = collections.deque()
        alpha_count = collections.deque()

        row_count = 0
        while i + (k * row_count) < n:
            col_count = 0
            while j + (k * col_count) < m:
                if len(alpha) == 0:
                    alpha.append(tile[i + (k * row_count)][j + (k * col_count)])
                    alpha_count.append(1)
                    most = tile[i + (k * row_count)][j + (k * col_count)]
                    most_count = 1
                elif tile[i + (k * row_count)][j + (k * col_count)] in alpha:
                    index = alpha.index(tile[i + (k * row_count)][j + (k * col_count)])
                    alpha_count[index] += 1
                    if alpha_count[index] > most_count:
                        most = tile[i + (k * row_count)][j + (k * col_count)]
                        most_count = alpha_count[index]
                else:
                    alpha.append(tile[i + (k * row_count)][j + (k * col_count)])
                    alpha_count.append(1)
                col_count += 1
            row_count += 1

        result += sum(alpha_count) - most_count
        result_tile[i].append(most)

print(result)
for _ in range(int(n/k)):
    for i in range(k):
        for j in range(int(m/k)):
            for p in range(k):
                print(result_tile[i][p], end='')
        print()