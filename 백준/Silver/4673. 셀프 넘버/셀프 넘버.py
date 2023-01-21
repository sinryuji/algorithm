nums = [0 for _ in range(10001)]

def d(n):
    sum = n
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

for i in range(1, 10001):
    n = d(i)
    if n < 10001:
        nums[n] = 1

for i in range(1, 10001):
    if nums[i] == 0:
        print(i)