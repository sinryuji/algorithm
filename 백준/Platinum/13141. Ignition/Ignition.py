import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = float('inf')
max_edge = [[0] * (N + 1) for _ in range(N + 1)]
min_edge = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, l = map(int, input().split())
    min_edge[e][s] = min_edge[s][e] = min(min_edge[s][e], l)
    max_edge[e][s] = max_edge[s][e] = max(max_edge[s][e], l)

for k in range(1, N + 1):
    min_edge[k][k] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == k or j == k:
                continue
            if min_edge[i][j] > min_edge[i][k] + min_edge[k][j]:
                min_edge[i][j] = min_edge[j][i] = min_edge[i][k] + min_edge[k][j]

answer = INF
for k in range(1, N+1) :
    min_edge[k][k] = 0
    result = 0.
    for i in range(1, N+1) :
        for j in range(i, N+1) :
            if not max_edge[i][j] :
                continue
            result = max(result, min_edge[k][i], min_edge[k][j])
            if abs(min_edge[k][i] - min_edge[k][j]) != max_edge[i][j] :
                result = max(result, max(min_edge[k][i], min_edge[k][j]) + (max_edge[i][j] - abs(min_edge[k][i] - min_edge[k][j])) / 2)
    answer = min(answer, result)

print(f'{answer:0.1f}')
