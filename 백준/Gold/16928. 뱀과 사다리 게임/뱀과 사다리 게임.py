import sys
from collections import deque
input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [0] * 101
ladder = dict()
snake = dict()
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y
q = deque([1])

while q:
    cur = q.popleft()
    if cur == 100:
        print(graph[cur])
        break
    for i in range(1, 7):
        next_ = cur + i
        if next_ <= 100 and graph[next_] == 0:
            if next_ in ladder.keys():
                next_ = ladder[next_]
            if next_ in snake.keys():
                next_ = snake[next_]
            if graph[next_] == 0:
                graph[next_] = graph[cur] + 1
                q.append(next_)