import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ps = []
s = 0
for x in arr:
    s += x
    ps.append(s)

ans = 0

for i in range(1, N - 1):
    ans = max(ans, ps[-2] + ps[i - 1] - arr[i])

for i in range(1, N - 1):
    ans = max(ans, ps[-1] - arr[0] - arr[i] + ps[-1] - ps[i])

for i in range(1, N - 1):
    ans = max(ans, ps[-2] - arr[0] + arr[i])

print(ans)