import sys, itertools as it

input = sys.stdin.readline

n, k = map(int, input().split())
if k < 5:
    print(0)
    sys.exit()

word = []
for _ in range(n):
    s = 0
    for i in list(input().rstrip()):
        s |= (2 ** (ord(i) - 97))
    word.append(s)

r = 0
comb = [2 ** i for i in range(26)]
for i in [0, 2, 8, 13, 19]:
    comb.remove(2 ** i)

for c in it.combinations(comb, k - 5):
    cnt, bit = 0, 532741
    for i in c:
        bit += i
    for i in word:
        if bit & i == i:
            cnt += 1
    r = max(r, cnt)
print(r)