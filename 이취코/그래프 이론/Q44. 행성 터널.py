# https://www.acmicpc.net/problem/2887

import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
x, y, z = [], [], []
for i in range(N):
    planet = list(map(int, input().split()))
    x.append((planet[0], i))
    y.append((planet[1], i))
    z.append((planet[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort(key=lambda x: x[0])

parent = [i for i in range(N)]
cnt = 0
answer = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += cost
        cnt += 1
    if cnt == N:
        break

print(answer)
