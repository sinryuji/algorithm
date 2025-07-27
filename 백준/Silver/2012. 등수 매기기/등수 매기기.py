import sys

input = sys.stdin.readline

N = int(input())
expected = sorted([int(input()) for _ in range(N)])

ans = 0
for i in range(1, N + 1):
    ans += abs(i - expected[i-1])
    
print(ans)