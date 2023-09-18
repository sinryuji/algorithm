from collections import deque

def bfs(n, k, max_):
    queue = deque([n])
    dist[n] = 0
    while queue:
        v = queue.popleft()
        if v == k:
            return dist[v]
        if 0 <= v - 1 <= max_ and dist[v - 1] == -1:
            dist[v - 1] = dist[v] + 1
            queue.append(v - 1)
        if 0 <= v * 2 <= max_ and dist[v * 2] == -1:
            dist[v * 2] = dist[v]
            queue.appendleft(v * 2)
        if 0 <= v + 1 <= max_ and dist[v + 1] == -1:
            dist[v + 1] = dist[v] + 1
            queue.append(v + 1)
        
N, K = map(int, input().split())
max_ = 100000
dist = [-1] * (max_ + 1)
print(bfs(N, K, max_))