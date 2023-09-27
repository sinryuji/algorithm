N = int(input())
graph = [list(input()) for _ in range(N)]
answer = 0

def check(graph):
    max_cnt = 1
    for x in range(N):
        cnt = 1
        for y in range(1, N):
            if graph[x][y] == graph[x][y - 1]:
                cnt += 1
            else: cnt = 1
            max_cnt = max(max_cnt, cnt)
        cnt = 1
        for y in range(1, N):
            if graph[y][x] == graph[y - 1][x]:
                cnt += 1
            else: cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt

for x in range(N):
    for y in range(N):
        if x + 1 < N:
            graph[x][y], graph[x + 1][y] = graph[x + 1][y], graph[x][y]
            answer = max(answer, check(graph))
            graph[x][y], graph[x + 1][y] = graph[x + 1][y], graph[x][y]
        if y + 1 < N:
            graph[x][y], graph[x][y + 1] = graph[x][y + 1], graph[x][y]
            answer = max(answer, check(graph))
            graph[x][y], graph[x][y + 1] = graph[x][y + 1], graph[x][y]
            
print(answer)