import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000000007

def factorial(n):
    ret = 1
    for i in range(2, n + 1):
        ret = (ret * i) % p 
    return ret

def square(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        tmp = square(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % p
        else:
            return tmp * tmp * a % p
        
top = factorial(n)
bot = factorial(k) * factorial(n - k) % p

print(top * square(bot, p - 2) % p)