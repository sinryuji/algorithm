import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, M):
    q = deque([(0, 0)])
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0:
                q.append((nx, ny))
                board[ny][nx] = 2
                cnt += 1
    return cnt != N * M

def find_exposed(N, M):
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if board[ny][nx] == 2:
                        cnt += 1
                if cnt >= 2:
                    board[y][x] = 3

def remove_exposed(N, M):
    for y in range(N):
        for x in range(M):
            if 2 <= board[y][x] <= 3:
                board[y][x] = 0

N, M = map(int, input().split())
board = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0
while bfs(N, M):
    find_exposed(N, M)
    remove_exposed(N, M)
    answer += 1

print(answer)