import sys

input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)

ans = -1
for i in range(N - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        ans = arr[i] + arr[i + 1] + arr[i + 2]
        break

print(ans)