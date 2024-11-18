n = 5
m = 5
data = [1, 2, 3, 2, 5]

cnt = 0
s = 0
end = 0

for start in range(n):
    while s < m and end < n:
        s += data[end]
        end += 1
    if s == m:
        cnt += 1
    s -= data[start]

print(cnt)
