n, b = map(int, input().split())

base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ret = ""
while n != 0:
    ret += base[n % b]
    n //= b
print(ret[::-1])