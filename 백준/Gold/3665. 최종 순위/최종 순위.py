import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    prev = list(map(int, input().split()))

    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            graph[prev[i]][prev[j]] = True
            indegree[prev[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not certain:
        print('?')
    else:
        print(*result)
