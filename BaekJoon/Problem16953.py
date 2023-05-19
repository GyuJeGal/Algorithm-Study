A, B = map(int, input().split(' '))

result = -2

que = [(A, 0)]
while len(que) > 0:
    (num, count) = que.pop(0)
    if num == B:
        result = count
        break
    elif num < B:
        que.append((num * 2, count + 1))
        que.append((num * 10 + 1, count + 1))
print(result + 1)