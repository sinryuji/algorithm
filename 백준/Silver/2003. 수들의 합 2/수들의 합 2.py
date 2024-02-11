import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

p_sum = [0]
s = 0
for num in nums:
    s += num
    p_sum.append(s)

ans = 0
for i in range(N+1):
    for j in range(i):
        if p_sum[i] - p_sum[j] == M:
            ans += 1

print(ans)