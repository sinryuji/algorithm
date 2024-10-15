import sys
from collections import deque

input = sys.stdin.readline

N, K = int(input()), int(input())
apples = []
for _ in range(K):
    y, x = map(int, input().split())
    apples.append((x, y))
L = int(input())
directions = deque()
for _ in range(L):
    x, c = input().rstrip().split()
    x = int(x)
    directions.append((x, c))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

snake = deque([(1, 1)])
cur = 0

second = 0
while True:
    second += 1
    nx, ny = snake[0][0] + d[cur][0], snake[0][1] + d[cur][1]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        break
    if (nx, ny) in snake:
        break

    snake.appendleft((nx, ny))
    
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        snake.pop()
        
    if directions and directions[0][0] == second:
        if directions[0][1] == 'L':
            cur = (cur - 1) % 4
        else:
            cur = (cur + 1) % 4
        directions.popleft()

print(second)
