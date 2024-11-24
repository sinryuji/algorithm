import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start):
    visited[start] = True
    dp[start][0] = 0
    dp[start][1] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]

dfs(1)
print(min(dp[1][0], dp[1][1]))
