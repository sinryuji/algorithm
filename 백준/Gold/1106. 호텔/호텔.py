import sys

input = sys.stdin.readline

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
dp = [1e7 for _ in range(C+100)]
dp[0] = 0

for cost, customers in cities:
    for i in range(customers, C+100):
        dp[i] = min(dp[i], dp[i-customers]+cost)

print(min(dp[C:]))