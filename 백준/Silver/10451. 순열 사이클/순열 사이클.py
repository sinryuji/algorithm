import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(start, x):
    global answer
    visited[x] = True
    if start == nums[x]:
        answer += 1
        return
    else:
        dfs(start, nums[x])


T = int(input())
for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    answer = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, i)

    print(answer)
