import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(int, input().split())) for _ in range(N)]

q, nq, ans = deque([(0, 0)]), deque(), 0

while q or nq:
    if not q:
        q, nq = nq, deque()
        ans += 1
    r, c = q.popleft()
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < M:
            if not board[nr][nc]:
                board[nr][nc] = -1
                q.append((nr, nc))
            if board[nr][nc] > 0:
                board[nr][nc] += 1
                if board[nr][nc] > 2:
                    board[nr][nc] = -1
                    nq.append((nr, nc))

print(ans)