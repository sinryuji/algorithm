import sys

input = sys.stdin.readline

V, E = map(int, input().split())
INF = int(1e9)
distance = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

answer = INF
for i in range(1, V + 1):
    answer = min(answer, distance[i][i])

print(-1 if answer == INF else answer)
