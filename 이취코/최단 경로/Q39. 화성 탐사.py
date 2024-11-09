import sys, heapq

imput = sys.stdin.readline

T = int(input())
INF = int(1e9)
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    distance = [[INF] * N for _ in range(N)]
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                q.append((cost, nx, ny))

    print(distance[N-1][N-1])
