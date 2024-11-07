import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
dist = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    dist[a-1][b-1] = 0

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

answer = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if dist[i][j] == 0 or dist[j][i] == 0:
            cnt += 1
    if cnt == N:
        answer += 1

print(answer)
