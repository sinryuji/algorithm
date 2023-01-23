n = int(input())
for _ in range(n):
    l = input().split()
    r = int(l[0]) 
    s = l[1]
    for c in s:
        print(c * r, end = '')
    print()