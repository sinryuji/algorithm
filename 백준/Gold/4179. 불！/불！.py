import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
q_j = deque()
q_f = deque()
graph = []
visited_j = [[0] * C for _ in range(R)]
visited_f = [[0] * C for _ in range(R)]
for y in range(R):
    line = list(input().rstrip())
    for x in range(C):
        if line[x] == 'J':
            q_j.append((x, y))
            visited_j[y][x] = 1
        if line[x] == 'F':
            q_f.append((x, y))
            visited_f[y][x] = 1
    graph.append(line)

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    while q_f:
        x, y = q_f.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and 0 <= ny < R and not visited_f[ny][nx] and graph[ny][nx] != '#' and graph[ny][nx] != 'F':
                visited_f[ny][nx] = visited_f[y][x] + 1
                q_f.append((nx, ny))

    while q_j:
        x, y = q_j.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and 0 <= ny < R:
                if not visited_j[ny][nx] and graph[ny][nx] != '#':
                    if not visited_f[ny][nx] or visited_f[ny][nx] > visited_j[y][x] + 1:
                        visited_j[ny][nx] = visited_j[y][x] + 1
                        q_j.append((nx, ny))
            else:
                return visited_j[y][x]

    return 'IMPOSSIBLE'

print(bfs())
