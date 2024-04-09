import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
number_board = [[0] * M for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * M for _ in range(N)]
group = {}


def bfs(x, y, n):
    global N, M

    count = 1

    visited[y][x] = True
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        number_board[y][x] = number
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if board[ny][nx] == 0 and not visited[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = True
                count += 1

    return count

number = 1
for row in range(N):
    for col in range(M):
        if board[row][col] == 0 and not visited[row][col]:
            count = bfs(col, row, number)
            group[number] = count
            number += 1

for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            s = 1
            added_numbers = []
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= M or ny < 0 or ny >= N or number_board[ny][nx] == 0:
                    continue
                if number_board[ny][nx] not in added_numbers:
                    added_numbers.append(number_board[ny][nx])
                    s += group[number_board[ny][nx]]
            board[y][x] = s % 10

for row in board:
    print(''.join(map(str, row)))
