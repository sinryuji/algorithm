import sys, copy
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
cost = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for j in data[1:len(data)-1]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(cost)

while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i], result[now] + cost[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*result[1:], sep='\n')