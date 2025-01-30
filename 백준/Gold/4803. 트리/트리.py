import sys

input = sys.stdin.readline


def dfs(node, parent):
    global cycle
    visited[node] = True

    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, node)
        elif nxt != parent:
            cycle = True


case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = False
            dfs(i, -1)
            if not cycle:
                cnt += 1

    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')

    case += 1
