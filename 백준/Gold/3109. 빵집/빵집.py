import sys

input = sys.stdin.readline

def dfs(r, c):
    global ans
    board[r][c] = 'x'

    if c == C - 1:
        return True

    if 0 <= r - 1 and board[r - 1][c + 1] == '.':
        if dfs(r - 1, c + 1):
            return True
    if board[r][c + 1] == '.':
        if dfs(r, c + 1):
            return True
    if r + 1 < R and board[r + 1][c + 1] == '.':
        if dfs(r + 1, c + 1):
            return True

    return False


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

ans = 0
for r in range(R):
    if dfs(r, 0):
        ans += 1

print(ans)