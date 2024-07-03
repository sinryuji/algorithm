string_A = input()
string_B = input()

dp = [[0] * (len(string_B) + 1) for _ in range(len(string_A) + 1)]

ans = 0
for i in range(1, len(string_A) + 1):
    for j in range(1, len(string_B) + 1):
        if string_A[i-1] == string_B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
            
print(ans)