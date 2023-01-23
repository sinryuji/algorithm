def d(n):
    l = list(map(int, str(n)))
    return l[0] - l[1] == l[1] - l[2]

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i <= 99:
        cnt += 1
        continue
    if d(i) == True:
        cnt += 1
print(cnt)