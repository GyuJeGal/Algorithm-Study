import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = [0] * 10

num = a * b * c

while num != 0:
    check = num % 10
    result[check] += 1
    num = int(num / 10)

for i in result:
    print(i)