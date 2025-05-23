import sys

input = sys.stdin.readline

def dfs(x, y):
    visited[x] = True
    v = arr[x]
    if not visited[v]:
        dfs(v, y)
    elif visited[v] and v == y:
        ret.append(v)

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

ret = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

ret.sort()
print(len(ret))
print(*ret, sep='\n')