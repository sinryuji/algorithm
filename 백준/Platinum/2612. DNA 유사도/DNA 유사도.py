la = int(input())
a = input()
lb = int(input())
b = input()

dp = [[0] * (lb + 1) for _ in range(la + 1)]

m, mi, mj = 0, 0, 0
for i in range(1, la + 1):
    for j in range(1, lb + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 3
        else:
            dp[i][j] = max(
                max([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) - 2, 0)
        if dp[i][j] > m:
            m, mi, mj = dp[i][j], i, j

si, sj = mi, mj
while dp[si][sj] != 0:
    if dp[si-1][sj] == dp[si][sj] + 2:
        si -= 1
    elif dp[si][sj-1] == dp[si][sj] + 2:
        sj -= 1
    else:
        si -= 1
        sj -= 1
    
print(m)
print(a[si:mi])
print(b[sj:mj])