import sys
from collections import deque

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(arr):
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])
    remove = set()
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    q.append((nr, nc))
                elif (nr, nc) not in remove:
                    remove.add((nr, nc))
                visited[nr][nc] = True
    return remove

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
remove_cnt = 0
while True:
    remove = bfs(board)
    if not remove:
        break
    for r, c in remove:
        board[r][c] = 0
    ans += 1
    remove_cnt = len(remove)

print(ans)
print(remove_cnt)