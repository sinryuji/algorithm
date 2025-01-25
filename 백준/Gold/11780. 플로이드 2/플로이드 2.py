import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[[INF, []] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b][0]:
        dist[a][b][0] = c
        dist[a][b][1] = [b, a]

for i in range(n + 1):
    dist[i][i][0] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost = dist[i][k][0] + dist[k][j][0]
            if cost < dist[i][j][0]:
                dist[i][j][0] = cost
                dist[i][j][1] = dist[k][j][1] + dist[i][k][1][1:]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j][0] == INF else dist[i][j][0], end=' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(len(dist[i][j][1]), *dist[i][j][1][::-1])
