l = list(map(int, input().split()))
s = set(l)
if len(s) == 1:
    print(10000 + l[0] * 1000)
elif len(s) == 3:
    print(max(l) * 100)
else:
    for i in s:
        l.remove(i)
    print(1000 + l[0] * 100)