import sys

input = sys.stdin.readline

def solve():
    for i in range(n):
        for j in range(i + 1, n):
            if (val := arr[i] + arr[j]) <= w:
                visited[val] = (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            val = arr[i] + arr[j]
            if val <= w and visited[w - val] and i not in visited[w - val] and j not in visited[w - val]:
                return True
    return False

w, n = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * (w + 1)

print('YES' if solve() else 'NO')
