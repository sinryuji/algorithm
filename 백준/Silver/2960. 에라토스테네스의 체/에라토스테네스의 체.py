N, K = map(int, input().split())
graph = [0] * (N + 1)
graph[0] = 1
graph[1] = 1

def f(n):
    cnt = 0
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if graph[j] == 0:
                cnt += 1
                graph[j] = 1
                if cnt == K:
                    return j
    
print(f(N))