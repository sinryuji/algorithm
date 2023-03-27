def fibo(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo_dynamic(n):
    global cnt2
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        cnt2 += 1
    return dp[n]

n = int(input())
cnt1 = cnt2 = 0
fibo(n)
fibo_dynamic(n)
print(cnt1, cnt2)