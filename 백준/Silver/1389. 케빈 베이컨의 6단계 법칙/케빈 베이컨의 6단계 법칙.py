from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

def bfs(start):
    visited = [0] * (N + 1)
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n] + 1
                queue.append(i)
    return sum(visited)

answer = []
for i in range(1, N + 1):
    answer.append(bfs(i))

print(answer.index(min(answer)) + 1)