import sys
from collections import deque

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[b] > rank[a]:
        parent[a] = b
    else:
        rank[b] += 1
        parent[a] = b
        

n, m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0] * n
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if not ans:
        if find(a) == find(b):
            ans = i + 1
        else:
            union(a, b)
    
print(ans)