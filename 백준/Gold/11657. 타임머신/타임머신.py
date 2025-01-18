import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[cur] + cost < distance[nxt]:
                distance[nxt] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False


N, M = map(int, input().split())
distance = [INF] * (N + 1)
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

negative_cycle = bellman_ford(1)
if negative_cycle:
    print('-1')
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print('-1')
        else:
            print(distance[i])
