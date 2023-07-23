import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 보석의 가치 배열
values = [0] * (N + 1)
# 누적합 배열
prefixSum = [0] * (N + 1)
dp = [0] * (N + 1)

# 각 보석의 가치를 입력 받으면서 누적합 계산
for i in range(1, N + 1):
    values[i] = int(input())
    prefixSum[i] = prefixSum[i - 1] + values[i]

# 0 ~ (i - M)까지의 최소 누적합, i는 M부터 N까지 순회
minSum = 0
# 최소로 가져갈 수 있는 보석이 M개 이므로 i는 M부터 시작
# dp는 현재시점까지 최대 이익, dp[i - 1]의 값과 (i번째 누적합 - 최소 누적합) 중 더 큰 값을 저징
for i in range(M, N + 1):
    minSum = min(prefixSum[i - M], minSum)
    dp[i] = max(dp[i - 1], prefixSum[i] - minSum)

print(dp[-1])

# 처음 풀이
# import collections
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# values = [0] * (N + 1)
# dp = [0] * (N + 1)
#
# for i in range(1, N + 1):
#     values[i] = int(input())
#     if i == 0:
#         dp[i] = values[i]
#     else:
#         dp[i] = dp[i - 1] + values[i]
#
# candidate = list(set(dp.copy()))
# candidate.sort()
# que = collections.deque()
# que.append([0, len(candidate) - 1, 0]) # [시작 인덱스, 끝 인덱스, depth]
#
# result = 0
# depth = 0
# while que:
#     cur = que.popleft()
#     if result != 0:
#         if depth < cur[2]:
#             break
#     else:
#         maxIndex = list(filter(lambda x: dp[x] == candidate[cur[1]], range(len(dp))))
#         minIndex = dp.index(candidate[cur[0]])
#
#         for i in reversed(range(len(maxIndex))):
#             if maxIndex[i] - minIndex >= M:
#                 result = max(result, candidate[cur[1]] - candidate[cur[0]])
#                 depth = cur[2]
#                 break
#         if cur[1] - cur[0] > 1:
#             que.append([cur[0] + 1, cur[1], cur[2] + 1])
#             que.append([cur[0], cur[1] - 1, cur[2] + 1])
#
# if result < 0:
#     print(result)
# else:
#     print(result)