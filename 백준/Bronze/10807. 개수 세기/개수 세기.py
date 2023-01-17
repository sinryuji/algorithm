n = int(input())
l = list(map(int, input().split()))
v = int(input())
c = 0
for i in l:
    if i == v:
        c += 1
print(c)