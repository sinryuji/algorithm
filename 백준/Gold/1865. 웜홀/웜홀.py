import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    distance = [INF] * (N + 1)
    distance[start] = 0

    for i in range(N):
        for edge in edges:
            curr = edge[0]
            next_ = edge[1]
            dist = edge[2]
            cost = distance[curr] + dist
            if distance[next_] > cost:
                distance[next_] = cost
                if i == N - 1:
                    return True
    return False

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")