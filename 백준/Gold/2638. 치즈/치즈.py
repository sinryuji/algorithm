import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    margin = [[-1] * (M + 2)]
    board = [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
    board = margin + board + margin
    
    q, nq, ans = deque([(1, 1)]), deque(), 0
    
    while q or nq:
        if not q:
            q, nq = nq, deque()
            ans += 1
        r, c = q.popleft()
        for dr, dc in d:
            if board[(nr:=r+dr)][(nc:=c+dc)] > 0:
                board[nr][nc] += 1
                if board[nr][nc] > 2:
                    board[nr][nc] = -1
                    nq.append((nr, nc))
            if not board[nr][nc]:
                board[nr][nc] = -1
                q.append((nr, nc))

    print(ans)

if __name__ == "__main__":
    main()