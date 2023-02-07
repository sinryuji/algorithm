n, m = map(int, input().split())

ret = 0
for _ in range(n):
    line = list(map(int, input().split()))
    minVal = min(line)
    ret = max(ret, minVal)
print(ret)
