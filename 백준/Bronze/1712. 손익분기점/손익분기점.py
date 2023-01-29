a, b, c = map(int, input().split())
m = c - b
if m <= 0:
    print(-1)
else:
    print(a // m + 1)