N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
answer = 0

def check(x, y, graph):
    target = graph[y][x]
    ans = 0
    for i in range(x, M):
        if target == graph[y][i]:
            if y + (i - x) < N and target == graph[y + (i - x)][x]:
                if target == graph[y + (i - x)][i]:
                    ans = max(ans, (i - x + 1) ** 2)
    return ans

for y in range(N):
    for x in range(M):
        answer = max(answer, check(x, y, graph))
        
print(answer)           