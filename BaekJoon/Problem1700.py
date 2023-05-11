N, K = map(int, input().split(' '))
appliance = list(map(int, input().split(' ')))

multitab = []
count = 0

for i in range(K):
    temp = appliance[i]
    if temp in multitab:
        continue
    if len(multitab) < N:
        multitab.append(temp)
        continue
    far = 0
    check = 0
    for plug in multitab:
        if plug not in appliance[i:]:
            check = plug
            break
        elif appliance[i:].index(plug) > far:
            far = appliance[i:].index(plug)
            check = plug
    multitab[multitab.index(check)] = temp
    count += 1
print(count)