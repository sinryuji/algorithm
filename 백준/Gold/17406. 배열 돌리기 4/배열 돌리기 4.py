import sys
from itertools import permutations

input = sys.stdin.readline

def roll(arr, r, c, s):
    for layer in range(1, s):
        r1, r2 = r - layer, r + layer
        c1, c2 = c - layer, c + layer

        tmp = arr[r1][c1]

        for i in range(r1, r2):
            arr[i][c1] = arr[i + 1][c1]
        for i in range(c1, c2):
            arr[r2][i] = arr[r2][i + 1]
        for i in range(r2, r1, -1):
            arr[i][c2] = arr[i - 1][c2]
        for i in range(c2, c1, -1):
            arr[r1][i] = arr[r1][i - 1]

        arr[r1][c1 + 1] = tmp

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