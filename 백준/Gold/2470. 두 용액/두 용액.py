import sys

input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))

sol.sort()

l, r = 0, n - 1
ans = abs(sol[l] + sol[r])
ans_l, ans_r = l, r

while l != r:
    s = sol[l] + sol[r]

    if s == 0:
        ans_l, ans_r = l, r
        break
    elif abs(s) < ans:
        ans_l, ans_r = l, r
        ans = abs(s)
    if s < 0:
        l += 1
    else:
        r -= 1

print(sol[ans_l], sol[ans_r])