import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = 0
for x in arr:
    if x == ans % 3:
        ans += 1

print(ans)