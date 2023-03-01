def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n + 1):
        if i not in s and (len(s) == 0 or s[-1] < i):
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())
s = []
dfs()