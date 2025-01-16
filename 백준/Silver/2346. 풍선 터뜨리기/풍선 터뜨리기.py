import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
balloons = list(range(1, N + 1))
idx = 0
answer = []

while cards:
    answer.append(balloons.pop(idx))
    move = cards.pop(idx)

    if not cards:
        break

    if move > 0:
        idx = (idx + move - 1) % len(cards)
    else:
        idx = (idx + move) % len(cards)

print(*answer)
