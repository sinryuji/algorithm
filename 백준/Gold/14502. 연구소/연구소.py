import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def bfs(p, graph, virus):
    tmp = copy.deepcopy(graph)
    for x, y in p:
        tmp[y][x] = 1

    q = deque()
    for x, y in virus:
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                q.append((nx, ny))

    result = 0
    for y in range(N):
        for x in range(M):
            if tmp[y][x] == 0:
                result += 1

    return result


N, M = map(int, input().split())
graph = []
empty = []
virus = []

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(M):
        if line[x] == 0:
            empty.append((x, y))
        elif line[x] == 2:
            virus.append((x, y))
    graph.append(line)

per = combinations(empty, 3)

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = 0
for p in per:
    answer = max(answer, bfs(p, graph, virus))

print(answer)
