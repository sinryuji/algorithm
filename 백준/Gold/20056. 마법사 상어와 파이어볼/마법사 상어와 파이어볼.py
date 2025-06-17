import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))

board = [[[] for _ in range(N)] for _ in range(N)]
di = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(K):
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop()
        dr, dc = di[cd]
        nr = (cr + cs * dr) % N
        nc = (cc + cs * dc) % N
        board[nr][nc].append((cm, cs, cd))

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(
                    board[r][c])
                while board[r][c]:
                    m, s, d = board[r][c].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:
                    for d in nd:
                        fireballs.append((r, c, sum_m // 5, sum_s // cnt, d))

            if len(board[r][c]) == 1:
                m, s, d = board[r][c].pop()
                fireballs.append((r, c, m, s, d))

print(sum(f[2] for f in fireballs))