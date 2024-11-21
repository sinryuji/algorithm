import sys
from collections import Counter

input = sys.stdin.readline


def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def check(p1, p2, p3, p4):
    l1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    l2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if l1 <= 0 and l2 <= 0:
        if l1 == 0 and l2 == 0:
            d1 = max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0])
            d2 = max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1])
            if d1 and d2:
                return 1
            return 0
        else:
            return 1
    return 0


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
lines = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append(((x1, y1), (x2, y2)))

parent = [i for i in range(N)]

for i in range(N):
    A, B = lines[i]
    for j in range(i):
        C, D = lines[j]
        if check(A, B, C, D):
            if find(i) != find(j):
                union(i, j)

for i in range(N):
    find(i)

print(len(set(parent)))
print(Counter(parent).most_common(1)[0][1])
