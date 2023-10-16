from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
doyeon = [0, 0]
answer = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 'I':
            doyeon = [x, y]
            break

queue = deque([doyeon])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[ny][nx] == 'P':
            graph[ny][nx] = 'O'
            answer += 1
        if graph[ny][nx] == 'O':
            graph[ny][nx] = 'X'
            queue.append([nx, ny])

if answer == 0:
    print('TT')
else:
    print(answer)