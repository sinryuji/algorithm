import sys

input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(N):
    ans = max(ans, arr[i] + i + 2)

print(ans)