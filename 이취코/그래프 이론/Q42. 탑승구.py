import sys

input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

G = int(input())
P = int(input())

parent = [i for i in range(G + 1)]

answer = 0
for _ in range(P):
    gi = int(input())
    root = find(gi)
    if root == 0:
        break
    parent[root] = parent[root-1]
    answer += 1

print(answer)
