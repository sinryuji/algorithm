import sys

input = sys.stdin.readline


def solve():
    dp = [0] * (w + 1)
    half = w // 2

    for i in range(n):
        for j in range(i + 1, n):
            v = arr[i] + arr[j]

            if v < half:
                if not dp[v]:
                    dp[v] = (i, j)
            else:
                v = w - v
                if v > 0 and dp[v]:
                    a, b = dp[v]
                    if i != a and i != b and j != a and j != b:
                        return True
    return False


w, n = map(int, input().split())
arr = sorted(list(map(int, input().split())))

print('YES' if solve() else 'NO')
