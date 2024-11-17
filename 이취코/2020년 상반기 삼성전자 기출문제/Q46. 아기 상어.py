# https://www.acmicpc.net/problem/16236

import sys
from collections import deque

input = sys.stdin.readline


def find_eatable(pos, size):
    global N
    visited = [[False] * N for _ in range(N)]
    q = deque([(pos[0], pos[1], 0)])
    visited[pos[1]][pos[0]] = True

    result = []
    while q:
        x, y, dist = q.popleft()

        if board[y][x] != 0 and board[y][x] < size:
            result.append((x, y, dist))

        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] <= size:
                visited[ny][nx] = True
                q.append((nx, ny, dist + 1))

    return sorted(result, key=lambda x: (x[2], x[1], x[0]))


N = int(input())
board = []
pos = (0, 0)
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 9:
            pos = (j, i)
            line[j] = 0
    board.append(line)

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
size = 2
cnt = 0
answer = 0
while True:
    eatable = find_eatable(pos, size)
    if len(eatable) == 0:
        break
    x, y, dist = eatable[0]
    pos = (x, y)
    board[y][x] = 0
    cnt += 1
    if size == cnt:
        cnt = 0
        size += 1
    answer += dist

print(answer)
