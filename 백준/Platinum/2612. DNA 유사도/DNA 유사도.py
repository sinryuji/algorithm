la = int(input())
a = input()
lb = int(input())
b = input()

dp = [[0] * (lb + 1) for _ in range(la + 1)]

m, mi, mj = 0, 0, 0
for i in range(1, la + 1):                             # LCS(Longest Common Subsequence)
    for j in range(1, lb + 1):
        if a[i - 1] == b[j - 1]:                       # 같은 문자면 +3점.
            dp[i][j] = dp[i - 1][j - 1] + 3
        else:                                          # 다른 문자면 -2점.
            dp[i][j] = max(
                max([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) - 2, 0)
        if dp[i][j] > m:                               # 최대값이면 값 갱신하고 인덱스 저장.
            m, mi, mj = dp[i][j], i, j

si, sj = mi, mj
while dp[si][sj] != 0:                                 # 두 DNA의 시작 인덱스의 dp 값이 0일때 까지 반복.
    if dp[si-1][sj] == dp[si][sj] + 2:                 # -2점을 해서 온 곳이면 그 곳으로 역추적.
        si -= 1
    elif dp[si][sj-1] == dp[si][sj] + 2:
        sj -= 1
    else:                                              # 아니면 +3점을 해서 온곳이므로 왼쪽 위 대각선으로 역추적.
        si -= 1
        sj -= 1
    
print(m)
print(a[si:mi])
print(b[sj:mj])