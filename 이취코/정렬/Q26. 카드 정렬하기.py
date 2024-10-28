# https://www.acmicpc.net/problem/1715

import sys, heapq

input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)
answer = 0
while len(cards) >= 2:
    x, y = heapq.heappop(cards), heapq.heappop(cards)
    answer += x + y
    heapq.heappush(cards, x + y)

print(answer)
