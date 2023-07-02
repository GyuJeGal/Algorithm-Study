import collections
import sys
input = sys.stdin.readline

str = input().strip()

result = ''

stack = collections.deque()

for i in range(len(str)):
    if str[i].isalpha():
        result += str[i]
        if len(stack):
            if stack[-1] in ['*', '/']:
                result += stack.pop()

    else:
        if str[i] == '(':
            stack.append(str[i])
        elif str[i] == ')':
            while True:
                lastChr = stack.pop()
                if lastChr == '(':
                    break
                else:
                    result += lastChr
        elif str[i] in ['+', '-']:
            if len(stack):
                if stack[-1] in ['+', '-']:
                    result += stack.pop()
            stack.append(str[i])
        else:
            if len(stack):
                if stack[-1] in ['*', '/']:
                    result += stack.pop()
            stack.append(str[i])

if len(stack) > 0:
    while len(stack):
        result += stack.pop()

print(result)


