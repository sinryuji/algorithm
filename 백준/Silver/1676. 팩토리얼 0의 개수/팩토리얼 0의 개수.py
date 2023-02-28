def factorial(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret

n = factorial(int(input()))
cnt = 0
for i in str(n)[::-1]:
    if i != '0':
        break
    cnt += 1
print(cnt)