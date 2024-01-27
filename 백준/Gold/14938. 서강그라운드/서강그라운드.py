import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
dist = [[INF] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a-1][b-1] = l
    dist[b-1][a-1] = l

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

answer = 0
for i in range(n):
    result = 0
    for j in range(n):
        if dist[i][j] <= m:
            result += items[j]
    answer = max(answer, result)

print(answer)