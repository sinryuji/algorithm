N = int(input())

def is_prime(x):
    if x in primes:
        return True
    elif x in not_primes:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            not_primes.add(x)
            return False
    primes.add(x)
    return True

def dfs(x, l):
    if l == N:
        print(x)
        return
    x *= 10
    for i in range(1, 10):
        if is_prime(x + i):
            dfs(x + i, l + 1)

primes = set()
not_primes = {1}

for i in range(2, 10):
    if is_prime(i):
        dfs(i, 1)
