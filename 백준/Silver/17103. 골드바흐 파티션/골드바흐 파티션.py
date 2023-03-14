import sys
input = sys.stdin.readline

max = 1000000
prime = [True] * max
for i in range(2, int(max ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, max, i):
            prime[j] = False

t = int(input())
for _ in range(t):
    ret = 0
    n = int(input())
    for i in range(2, len(prime)):
        if i >= n:
            break
        if prime[i] and prime[n - i] and i <= n - i:
            ret += 1
    print(ret)