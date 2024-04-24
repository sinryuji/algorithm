import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, (int(input())))
s = 0
cnt = 0
while len(cards) > 1:
    card1, card2 = heapq.heappop(cards), heapq.heappop(cards)
    s += card1 + card2
    heapq.heappush(cards, card1 + card2)

print(s)