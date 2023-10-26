from collections import deque

def bfs(start, visited):
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] == 1:
            graph[i].append(j)

answer = []

for i in range(N):
    visited = [0] * N
    bfs(i, visited)
    answer.append(' '.join(map(str, visited)))

for i in answer:
    print(i)