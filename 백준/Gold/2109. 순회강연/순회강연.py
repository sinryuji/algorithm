import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: -x[0])

ans = 0
reservation = [False] * (10001)
for a, b in arr:
    for i in range(b, 0, -1):
        if not reservation[i]:
            ans += a
            reservation[i] = True
            break
            
print(ans)