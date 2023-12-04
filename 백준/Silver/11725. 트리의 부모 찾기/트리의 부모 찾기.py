from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (N + 1)

queue = deque([1])
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if answer[i] == 0:
            answer[i] = x
            queue.append(i)

for i in range(2, N + 1):
    print(answer[i])