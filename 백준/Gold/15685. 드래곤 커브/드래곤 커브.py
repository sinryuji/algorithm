import sys

input = sys.stdin.readline

graph = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1

    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move) - 1, -1, -1):
            tmp.append((move[i] + 1) % 4)
        move += tmp

    for m in move:
        nx = dx[m] + x
        ny = dy[m] + y
        graph[ny][nx] = 1
        x, y = nx, ny

answer = 0
for y in range(100):
    for x in range(100):
        if graph[y][x] and graph[y][x + 1] and graph[y + 1][x] and graph[y + 1][
            x + 1]:
            answer += 1

print(answer)