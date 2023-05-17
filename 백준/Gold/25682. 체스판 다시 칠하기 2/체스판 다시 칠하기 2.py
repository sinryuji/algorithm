import sys
input = sys.stdin.readline

def getMinFillCount(color):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                val = chess[i][j] == color
            else:
                val = chess[i][j] != color
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] + val - prefix[i][j]
    min_cnt = sys.maxsize
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            min_cnt = min(min_cnt, prefix[i + k - 1][j + k - 1] - prefix[i + k - 1][j - 1] - prefix[i - 1][j + k - 1] + prefix[i - 1][j - 1])
    return min_cnt
    
n, m, k = map(int, input().split())
chess = [input().rstrip() for _ in range(n)]

print(min(getMinFillCount('W'), getMinFillCount('B')))