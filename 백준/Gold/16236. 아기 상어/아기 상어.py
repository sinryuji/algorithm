import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    global N
    global size
    ret = []
    min_ = int(1e9)
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if dist > min_:
                continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] > size:
                continue
            if 0 < board[nx][ny] < size and dist <= min_:
                visited[nx][ny] = True
                ret.append((nx, ny, dist + 1))
                min_ = dist
                continue
            queue.append((nx, ny, dist + 1))
            visited[nx][ny] = True
    return ret

def get_target(eatable):
    return sorted(eatable, key = lambda x : ([x[0], x[1]]))[0]

N = int(input())
board = []
shark = []
size = 2
answer = 0
count = 0
for i in range(N):
    line = list(map(int, input().split()))
    if 9 in line:
        shark = [i, line.index(9)]
    board.append(line)

eatable = bfs(shark)

while eatable:
    x, y, dist = get_target(eatable)
    board[shark[0]][shark[1]] = 0
    shark = [x, y]
    answer += dist
    count += 1
    if size == count:
        size += 1
        count = 0
    board[x][y] = 9
    eatable = bfs(shark)

print(answer)