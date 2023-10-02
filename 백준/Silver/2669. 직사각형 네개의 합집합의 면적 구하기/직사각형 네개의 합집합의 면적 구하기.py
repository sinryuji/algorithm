graph = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for x in range(a, c):
        for y in range(b, d):
            if graph[y][x] == 0:
                graph[y][x] = 1
                answer += 1

print(answer)