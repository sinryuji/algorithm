def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n + 1):
        if len(s) == 0 or (len(s) > 0 and i >= s[-1]):
            s.append(i)
            dfs()
            s.pop()
        
n, m = map(int, input().split())
s = []
dfs()