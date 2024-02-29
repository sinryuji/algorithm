import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 0
ans = 0
s = 0

for l in range(N):
    while s < M and r < N:
        s += nums[r]
        r += 1
    if s == M:
        ans += 1
    s -= nums[l]

print(ans)