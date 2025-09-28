import sys

input = sys.stdin.readline

N, L = map(int, input().split())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], )

edge = arr[0][0]
ans = 0
for start, end in arr:
    if edge > end:
        continue
    elif edge < start:
        edge = start
    dist = end - edge
    cnt = (dist - 1) // L + 1
    edge += cnt * L
    ans += cnt

print(ans)