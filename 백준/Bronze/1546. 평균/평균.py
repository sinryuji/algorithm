n = int(input())
l = list(map(int, input().split()))
max = max(l)
ret = [(i / max) * 100 for i in l]
print(sum(ret) / n)