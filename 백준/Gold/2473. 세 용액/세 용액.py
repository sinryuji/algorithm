import sys

input = sys.stdin.readline

n = int(input())
sol = sorted(list(map(int, input().split())))

ans = []
ans_s = int(3e9)

for i in range(n - 2):
    l = i + 1
    r = n - 1
    while l < r:
        s = sol[i] + sol[l] + sol[r]
        if abs(s) <= ans_s:
            ans = [sol[i], sol[l], sol[r]]
            ans_s = abs(s)
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            print(*ans)
            exit()

print(*ans)