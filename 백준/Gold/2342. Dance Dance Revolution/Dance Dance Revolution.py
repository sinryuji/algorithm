import sys

input = sys.stdin.readline


def move(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a - b) == 2:
        return 4
    else:
        return 3


def solve():
    arr = list(map(int, input().split()))
    arr_len = len(arr)
    max_ = 4 * arr_len
    dp = [[[max_] * 5 for _ in range(5)] for _ in range(arr_len)]
    dp[0][0][0] = 0

    for i in range(arr_len - 1):
        n = arr[i]
        for left in range(5):
            for right in range(5):
                dp[i + 1][left][n] = min(dp[i + 1][left][n],
                                         dp[i][left][right] + move(right, n))
                dp[i + 1][n][right] = min(dp[i + 1][n][right],
                                          dp[i][left][right] + move(left, n))

    print(min(min(dp[arr_len - 1])))


if __name__ == "__main__":
    solve()
