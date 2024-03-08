import sys
from collections import deque

input = sys.stdin.readline


def topology_sort(N, indegree, dp, seq, times):
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        n = q.popleft()
        for i in seq[n]:
            indegree[i] -= 1
            dp[i] = max(dp[n] + times[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    return dp

def solve():
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    seq = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        seq[a].append(b)
        indegree[b] += 1
    W = int(input())

    dp = topology_sort(N, indegree, dp, seq, times)

    print(dp[W])


for _ in range(int(input())):
    solve()