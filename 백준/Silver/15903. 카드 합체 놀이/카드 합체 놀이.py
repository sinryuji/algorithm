def solve():
    n, m = map(int, input().split())
    cards = sorted(list(map(int, input().split())))

    for _ in range(m):
        cards[0] = cards[1] = cards[0] + cards[1]
        cards.sort()

    print(sum(cards))

solve()