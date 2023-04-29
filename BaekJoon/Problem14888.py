import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
# +, -, *, / 순

maximum = -1e9
minimum = 1e9

def solution(depth, result, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    # + 인 경우
    if plus > 0:
        solution(depth + 1, result + nums[depth], plus - 1, minus, multiply, divide)
    # - 인 경우
    if minus > 0:
        solution(depth + 1, result - nums[depth], plus, minus - 1, multiply, divide)
    # * 인 경우
    if multiply > 0:
        solution(depth + 1, result * nums[depth], plus, minus, multiply - 1, divide)
    # / 인 경우
    if divide > 0:
        # if result < 0:
        #     solution(depth + 1, ((result * -1) / nums[depth]) * -1, plus, minus, multiply, divide - 1)
        # else:
        #     solution(depth + 1, result / nums[depth], plus, minus, multiply, divide - 1)
        solution(depth + 1, int(result / nums[depth]), plus, minus, multiply, divide - 1)

solution(1, nums[0], opers[0], opers[1], opers[2], opers[3])
print(maximum)
print(minimum)