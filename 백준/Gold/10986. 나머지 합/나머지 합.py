n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
arr = [0] * m
for i in range(n):
    sum += a[i]
    arr[sum % m] += 1

ret = arr[0]
for i in arr:
    ret += i * (i - 1) // 2

print(ret)