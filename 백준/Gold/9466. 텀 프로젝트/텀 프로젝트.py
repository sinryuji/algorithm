import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    next_ = nums[x]

    if visited[next_]:
        if next_ in cycle:
            result += cycle[cycle.index(next_):]
    else:
        dfs(next_)


T = int(input())
for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))