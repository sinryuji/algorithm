n = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
            if n % i == 0:
                return False
    return True

nums = map(int, input().split())
cnt = 0
for i in nums:
    if isPrime(i):
        cnt += 1
print(cnt)