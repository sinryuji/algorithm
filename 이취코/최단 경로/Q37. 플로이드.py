# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
dist = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for line in dist:
    print(*[0 if i == INF else i for i in line])
