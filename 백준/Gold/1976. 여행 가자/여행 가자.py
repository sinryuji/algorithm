import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            union(i + 1, j + 1)
travel = list(map(int, input().split()))
s = set()
for i in travel:
    s.add(parent[i])

if len(s) == 1:
    print('YES')
else:
    print('NO')
