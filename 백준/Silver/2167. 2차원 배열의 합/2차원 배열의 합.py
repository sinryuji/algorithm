import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (M + 1)]
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

for y in range(1, N + 1):
    for x in range(1, M + 1):
        graph[y][x] = graph[y][x] + graph[y - 1][x] + graph[y][x - 1] - graph[y - 1][x - 1]

for _ in range(int(input())):
    j, i, y, x = map(int, input().split())
    print(graph[y][x] - graph[j - 1][x] - graph[y][i - 1] + graph[j - 1][i - 1])