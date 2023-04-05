def solution(cards, limit):
    result = 0
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            for k in range(j + 1, len(cards)):
                sum = cards[i] + cards[j] + cards[k]
                if(sum <= limit):
                    if(sum > result):
                        result = sum
                else:
                    break
    return result


N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
print(solution(cards, M))