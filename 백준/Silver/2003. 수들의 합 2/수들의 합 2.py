import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

s, e = 0, 1
ans = 0
while e <= N:
    sum_ = sum(nums[s:e])
    if sum_ == M:
        ans += 1
        e += 1
    elif sum_ < M:
        e += 1
    else:
        s += 1

print(ans)