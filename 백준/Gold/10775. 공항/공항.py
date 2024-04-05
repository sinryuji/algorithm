import sys

input = sys.stdin.readline

def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

G, P = int(input()), int(input())
parent = [i for i in range(G + 1)]

answer = 0
for _ in range(P):
    gi = int(input())
    tmp = find(gi)
    if tmp == 0:
        break
    parent[tmp] = parent[tmp - 1]
    answer += 1

print(answer)