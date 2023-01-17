n, x = map(int, input().split())
l = list(map(int, input().split()))
c = [str(i) for i in l if i < x]
print(' '.join(c))