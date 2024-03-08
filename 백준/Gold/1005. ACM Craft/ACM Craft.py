import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def dfs(n, times, graph, dp):
    if dp[n] != -1:
        return dp[n]
    max_ = 0
    for x in graph[n]:
        r = dfs(x, times, graph, dp)
        if r > max_:
            max_ = r
    dp[n] = max_ + times[n]
    return dp[n]

def solve():
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    dp = [-1] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b].append(a)
    W = int(input())

    print(dfs(W, times, graph, dp))

for _ in range(int(input())):
    solve()