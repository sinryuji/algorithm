import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    height = sorted(list(map(int, input().split())))
    ans = 0

    for i in range(2, N):
        ans = max(ans, abs(height[i] - height[i - 2]))

    print(ans)