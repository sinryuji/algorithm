n, k = map(int, input().split())

ret = 0
while n > 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    ret += 1
print(ret)
