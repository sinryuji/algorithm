import sys
input = sys.stdin.readline

def dfs(x, wei):
    for a, b in tree[x]:
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei+b)

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    line = list(map(int, input().split()))
    node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[node].append((adj_node, adj_cost))
        idx += 2

distance = [-1] * (V+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (V+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))