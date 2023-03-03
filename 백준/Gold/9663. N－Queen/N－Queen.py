def dfs(x):
    if x == n:
        global ret
        ret += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        chess[x] = i
        if is_possible(x):
            visited[i] = True
            dfs(x + 1)
            visited[i] = False

def is_possible(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x] - chess[i]) == x - i:
            return False
    return True

n = int(input())
chess = [0] * n
visited = [False] * n
ret = 0
dfs(0)
print(ret)