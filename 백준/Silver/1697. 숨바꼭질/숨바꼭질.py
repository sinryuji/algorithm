def bfs(n, k, max_):
    queue = [n]
    while queue:
        v = queue.pop(0)
        if v == k:
            return dist[v]
        for i in (v - 1, v + 1, v * 2):
            if i < 0 or i > max_:
                continue
            if dist[i] == 0:
                queue.append(i)
                dist[i] = dist[v] + 1

n, k = map(int, input().split())
max_ = 100000
dist = [0] * 100001
print(bfs(n, k, max_))