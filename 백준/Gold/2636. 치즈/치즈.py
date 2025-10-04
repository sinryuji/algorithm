import sys
from collections import deque

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(arr):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    q.append((nr, nc))
                if arr[nr][nc] == 1:
                    arr[nr][nc] = -1
                visited[nr][nc] = True


def cleanup(arr):
    removed = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == -1:
                arr[r][c] = 0
                removed += 1
    return removed


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
prev = 0
while True:
    bfs(board)
    removed = cleanup(board)
    if not removed:
        break
    ans += 1
    prev = removed

print(ans)
print(prev)