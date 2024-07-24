import sys

input = sys.stdin.readline
INF = 1e+9
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    
dp = [[None for _ in range(1 << N)] for _ in range(N)]
visited = 1

def dfs(start, visited):
    if visited == (1 << N) - 1:
        if graph[start][0] != 0:
            return graph[start][0]
        else:
            return INF

    if dp[start][visited] != None:
        return dp[start][visited]

    min_val = INF
    for i in range(1, N):
        if (graph[start][i] != 0) and ((visited & (1 << i)) == 0):
            min_val = min(min_val, dfs(i, visited | (1 << i)) + graph[start][i])
    dp[start][visited] = min_val

    return min_val


answer = dfs(0, visited)
print(dfs(0, 1))