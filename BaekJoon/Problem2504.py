brackets = input()
stack = []
# depth = 1이면 result[1]
result = [0] * 16

for i in range(len(brackets)):
    if (brackets[i] == '(') or (brackets[i] == '['):
        stack.append(brackets[i])
    elif brackets[i] == ')':
        if len(stack) == 0:
            result[0] = 0
            break
        if stack[-1] == '(':
            stack.pop()
            depth = len(stack)
            if result[depth + 1] == 0:
                result[depth] += 2
            else:
                result[depth] += result[depth + 1] * 2
                result[depth + 1] = 0
        else:
            result[0] = 0
            break
    # brackets[i]가 ] 일때
    else:
        if len(stack) == 0:
            result[0] = 0
            break
        if stack[-1] == '[':
            stack.pop()
            depth = len(stack)
            if result[depth + 1] == 0:
                result[depth] += 3
            else:
                result[depth] += result[depth + 1] * 3
                result[depth + 1] = 0
        else:
            result[0] = 0
            break
print(result[0])