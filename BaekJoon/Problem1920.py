import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()


def binary(i):
    first = 0
    end = n - 1

    while first <= end:
        mid = (first + end) // 2
        if n_arr[mid] == i:
            return True
        if i < n_arr[mid]:
            end = mid - 1
        elif i > n_arr[mid]:
            first = mid + 1


for i in range(m):
    if binary(m_arr[i]):
        print(1)
    else:
        print(0)