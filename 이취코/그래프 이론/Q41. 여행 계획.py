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

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            union(i+1, j+1)

plan = list(map(int, input().split()))
result = True
for i in range(1, M):
    if find(i) != find(i+1):
        result = False
        break

print(parent)
if result:
    print("YES")
else:
    print("NO")
