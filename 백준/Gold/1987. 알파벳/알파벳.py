R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
alphas = set()

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in alphas:
            alphas.add(board[nx][ny])
            dfs(nx, ny, count + 1)
            alphas.remove(board[nx][ny])

alphas.add(board[0][0])
dfs(0, 0, 1)
print(answer)