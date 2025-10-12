import sys
from itertools import permutations
import copy

input = sys.stdin.readline

def roll(arr, r, c, s):
    tmp = [row[:] for row in arr]
    for a in range(1, s):
        for x in range(c - a + 1, c + a + 1):
            arr[r - a][x] = tmp[r - a][x - 1]
        for y in range(r - a + 1, r + a + 1):
            arr[y][c + a] = tmp[y - 1][c + a]
        for x in range(c + a - 1, c - a - 1, -1):
            arr[r + a][x] = tmp[r + a][x + 1]
        for y in range(r + a - 1, r - a - 1, -1):
            arr[y][c - a] = tmp[y + 1][c - a]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cal = [tuple(map(int, input().split())) for _ in range(K)]

ans = sys.maxsize
for per in permutations(cal, K):
    tmp = [row[:] for row in arr]
    for r, c, s in per:
        roll(tmp, r - 1, c - 1, s + 1)
    ans = min(ans, min(map(sum, tmp)))

print(ans)