import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    global result
    for i in graph[n]:
        if visited[i] == -1:
            if visited[n] == 1:
                visited[i] = 2
            elif visited[n] == 2:
                visited[i] = 1
            dfs(i)
        else:
            if visited[n] == visited[i]:
                result = False
                return

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [-1] * (v + 1)
    result = True
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if visited[i] == -1:
            visited[i] = 1
            dfs(i)
            if result == False:
                break
    print("YES" if result else "NO")
                