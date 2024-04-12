import sys

input = sys.stdin.readline


def find(target):
    parent[target] = -2
    for i in range(N):
        if target == parent[i]:
            find(i)


N = int(input())
parent = list(map(int, input().split()))
remove = int(input())

find(remove)

leef = 0
for i in range(N):
    if parent[i] != -2 and i not in parent:
        leef += 1

print(leef)