N = int(input())
i = 1
while True:
    if (i * (i + 1) / 2 <= N) and ((i + 1) * (i + 2) / 2 > N):
        print(i)
        break
    i += 1