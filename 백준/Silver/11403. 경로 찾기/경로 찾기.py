from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited = []
    cnt = 0
    while queue:
        n = queue.popleft()
        if n == end and cnt > 0:
            return True
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                cnt += 1
    return False

N = int(input())
graph = [[] for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        if l[j] == 1:
            graph[i].append(j)

answer = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if bfs(i, j):
            answer[i].append(1)
        else:
            answer[i].append(0)

for i in answer:
    print(*i)