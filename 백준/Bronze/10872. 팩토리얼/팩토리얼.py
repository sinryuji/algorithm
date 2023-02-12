n = int(input())

ret = 1
while n > 1:
    ret *= n
    n -= 1
print(ret)