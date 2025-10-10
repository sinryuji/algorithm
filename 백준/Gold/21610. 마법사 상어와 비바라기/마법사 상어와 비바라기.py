import sys

input = sys.stdin.readline

def solve():

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    di = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
          (1, -1)]
    dia = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    for _ in range(M):
        d, s = map(int, input().split())
        dr, dc = di[d]
        tmp = []
        for r, c in cloud:
            nr, nc = (r + dr * s) % N, (c + dc * s) % N
            board[nr][nc] += 1
            tmp.append((nr, nc))
        cloud.clear()

        for r, c in tmp:
            for dr, dc in dia:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] >= 1:
                    board[r][c] += 1

        tmp = set(tmp)
        for r in range(N):
            for c in range(N):
                if board[r][c] >= 2 and (r, c) not in tmp:
                    cloud.append((r, c))
                    board[r][c] -= 2

    answer = 0
    for r in range(N):
        answer += sum(board[r])

    print(answer)

solve()