import sys
from collections import deque

input = sys.stdin.readline

N, K = int(input()), int(input())
apples = []
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    apples.append([y, x])
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

snake = deque()
snake.append([0, 0])
cur_di = 0
sec = 0

L = int(input())
change_directions = []
for _ in range(L):
    X, C = input().split()
    change_directions.append((int(X), C))

while(True):
    sec += 1
    head = snake[0]
    next_head = [head[0] + di[cur_di][0], head[1] + di[cur_di][1]]
    if next_head[0] < 0 or next_head[0] >= N or next_head[1] < 0 or next_head[
        1] >= N:
        break
    if next_head in snake:
        break
    snake.appendleft(next_head)
    if next_head in apples:
        apples.remove(next_head)
    else:
        snake.pop()
    if change_directions and sec == change_directions[0][0]:
        if change_directions[0][1] == 'D':
            cur_di += 1
        else:
            cur_di -= 1
        if cur_di == 4:
            cur_di = 0
        if cur_di == -1:
            cur_di = 3
        change_directions.pop(0)

print(sec)