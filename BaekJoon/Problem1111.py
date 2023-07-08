import sys

# 수열의 개수
n = int(sys.stdin.readline())

# 수열 리스트 저장
nums = list(map(int, sys.stdin.readline().strip().split()))

# 수열 크기가 1이면 A 출력
if len(nums) == 1:
    print("A")
# 수열 크기가 2일 때, 두 수가 서로 다르면 다음 수 추측 불가, 같으면 동일값 출력
elif len(nums) == 2:
    if nums[0] != nums[1]:
        print("A")
    else:
        print(nums[0])
# 수열의 크기가 3 이상일 때
else:
    a = 0
    b = 0
    # 첫번째 수와 두번째 수가 같은 경우
    if nums[0] == nums[1]:
        a = 1
        # 두번째 수와 세번째 수가 다른 경우 B 출력
        if nums[1] != nums[2]:
            a = -1
            print("B")
    # 다음 수를 특정할 수 있는 경우
    if a != -1:
        # a가 1이면 수열의 요소가 모두 같은 경우임
        # a가 1이 아니면 방정식을 통해 a, b를 구해야 함
        if a != 1:
            a = (nums[1] - nums[2]) / (nums[0] - nums[1])
            # a가 정수가 아닌 실수일 때
            if int(a) != a:
                print("B")
            # a가 정수일 때
            else:
                a = int(a)
                b = nums[1] - (nums[0] * a)
        # a가 정수일 때만 통과
        if int(a) == a:
            result = (nums[-1] * a) + b
            # 수열이 중간에 틀리면 B 출력
            for i in range(3, n):
                if (nums[i - 1] * a) + b != nums[i]:
                    result = "B"
                    print(result)
                    break
            # 중간에 틀리는 게 없으면 결과 출력
            if result != "B":
                print(result)

