import sys

input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i + 1, n):
        ix, iy = stars[i]
        jx, jy = stars[j]
        edges.append([i, j, get_distance(ix, iy, jx, jy)])

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

ans = 0
cnt = 0
for a, b, dist in edges:
    if find(a) != find(b):
        union(a, b)
        ans += dist
        cnt += 1

    if cnt == n:
        break

print(ans)