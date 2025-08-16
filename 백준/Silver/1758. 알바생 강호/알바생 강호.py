import sys

input = sys.stdin.readline

N = int(input())
arr = sorted([int(input().rstrip()) for _ in range(N)], reverse=True)

ans = 0
for i in range(N):
    tip = arr[i] - i
    if tip > 0:
        ans += tip

print(ans)