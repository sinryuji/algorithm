import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

l, r = 0, 1
ans = 0
s = nums[0]
while True:
    if s < M:
        if r < N:
            s += nums[r]
            r += 1
        else:
            break
    else:
        if s == M:
            ans += 1
        s -= nums[l]
        l += 1

print(ans)