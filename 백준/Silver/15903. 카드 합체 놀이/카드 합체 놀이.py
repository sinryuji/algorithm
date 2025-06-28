import heapq

def solve():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    heapq.heapify(cards)

    for _ in range(m):
        a, b = heapq.heappop(cards), heapq.heappop(cards)
        heapq.heappush(cards, a + b)
        heapq.heappush(cards, a + b)

    print(sum(cards))

solve()