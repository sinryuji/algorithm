from collections import deque

N = int(input())
cards = deque([i for i in range(1, N + 1)])
answer = []

while True:
    answer.append(cards.popleft())
    if not cards:
        break
    cards.append(cards.popleft())

print(*answer)