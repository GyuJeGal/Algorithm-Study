n, m = map(int, input().split())

knownPeople = list(map(int, input().split()))
knownPeople.pop(0)
knownPeople = set(knownPeople)

result = 0

visitPeople = []

for _ in range(m):
    visit = list(map(int, input().split()))
    visit.pop(0)
    visitPeople.append(visit)

check = 1
while check:
    for i in range(m):
        if len(visitPeople[i]) != 1:
            visitTest = set(visitPeople[i])
            inter = visitTest.intersection(knownPeople)
            if len(inter):
                addPeople = visitTest - knownPeople
                if len(addPeople):
                    knownPeople.update(addPeople)
                    break
        if i == m - 1:
            check = 0

for i in range(m):
    visitTest = set(visitPeople[i])
    inter = visitTest.intersection(knownPeople)
    if len(inter) == 0:
        result += 1

print(result)