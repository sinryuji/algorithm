import sys

input = sys.stdin.readline

def check():
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt

def dfs(n):
    global answer
    if n == N:
        answer = max(answer, check())
        return

    if eggs[n][0] <= 0:
        dfs(n + 1)
    else:
        broken = True
        for i in range(N):
            if n != i and eggs[i][0] > 0:
                broken = False
                eggs[n][0] -= eggs[i][1]
                eggs[i][0] -= eggs[n][1]
                dfs(n + 1)
                eggs[n][0] += eggs[i][1]
                eggs[i][0] += eggs[n][1]
        if broken:
            dfs(N)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(0)
print(answer)