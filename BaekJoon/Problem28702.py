import sys

input = sys.stdin.readline

# 입력 문자열 저장
inputStr = []

# 결과값
result = 0

for _ in range(3):
    # 입력 받을 때 뒤에 엔터 제거
    s = input().strip()
    inputStr.append(s)

# 입력 문자열 중에 숫자로 된게 있으면 바로 답 알 수 있음
for i in range(3):
    if inputStr[i].isdigit():
        result = int(inputStr[i]) + (3 - i)
        break

# 입력 문자열로 15, 3, 5의 배수인 지 숫자로 저장할 배열
check = []

# result가 이미 저장되어 있으면 패스
if result == 0:
    for i in range(3):
        if inputStr[i] == "FizzBuzz":
            check.append(15)
        if inputStr[i] == "Fizz":
            check.append(3)
        else:
            check.append(5)

    # 처음 숫자는 check[0]의 값
    result = check[0]

    # check를 돌면서 만족하는 result 값 찾기
    flag = True
    while flag:
        for i in range(3):
            # 배수 조건 만족안하면 result += result로 갱신
            if (result + i) % check[i] != 0:
                result += result
                break

            else:
                # 배수 조건을 만족하고 check 배열을 끝까지 돌았으면 result 갱신 후 break
                if i == 2:
                    result += 3
                    flag = False

if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)