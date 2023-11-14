n = int(input()) # 사람 수
arr = list(map(int, input().split())) # 인출 시간
arr.sort() # 정렬

result = 0

for i in range(1, n):
    arr[i] += arr[i - 1] # 인출 시간 갱신

print(sum(arr))