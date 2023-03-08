import sys

def dfs(depth, idx):
    global min_val
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += s[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += s[i][j]
        min_val = min(min_val, abs(power1 - power2))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

n = int(sys.stdin.readline())
s = [list(map(int, i.split())) for i in sys.stdin.readlines()]
visited = [False] * n
min_val = 200
dfs(0, 0)
print(min_val)