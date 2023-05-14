N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

i = 0
j = 0
result = 100001
sum = nums[0]

while True:
    if sum >= K:
        sum -= nums[i]
        result = min(result, j - i + 1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        sum += nums[j]
if result == 100001:
    print(0)
else:
    print(result)