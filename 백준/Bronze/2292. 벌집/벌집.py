n = int(input())
cnt = 1
while n > 1:
    n -= cnt * 6
    cnt += 1
print(cnt)