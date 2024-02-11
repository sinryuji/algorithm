import sys
input = sys.stdin.readline

N = int(input())
sol = list(map(int, input().split()))

l, r = 0, N - 1
ans = abs(sol[l] + sol[r])
ans_l, ans_r = l, r
while l != r:
    s = sol[l] + sol[r] 
    if abs(s) < ans: 
        ans = abs(s)
        ans_l, ans_r = l, r
        if ans == 0:
            break
    if s < 0:
        l += 1
    else:
        r -= 1

print(sol[ans_l], sol[ans_r])