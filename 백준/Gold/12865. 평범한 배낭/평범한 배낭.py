n, k = map(int, input().split())
l = [[0, 0]]
for _ in range(n):
    l.append(list(map(int, input().split())))
dp = [0] * (k + 1)

for i in range(1, n + 1):
    for j in range(k, 0, -1):
        if l[i][0] <= j:
            dp[j] = max(dp[j], dp[j - l[i][0]] + l[i][1])
          
print(dp[k])