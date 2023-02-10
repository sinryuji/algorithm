n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
for i in sorted(l):
    print(*i)