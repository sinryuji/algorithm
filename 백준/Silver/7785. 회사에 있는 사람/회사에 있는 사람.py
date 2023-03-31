import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    key, val = input().split()
    d[key] = val
d = dict(sorted(d.items(), key = lambda item: item[0], reverse = True))
for i in d.keys():
    if d[i] == 'enter':
        print(i)