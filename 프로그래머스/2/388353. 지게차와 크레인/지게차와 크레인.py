from collections import deque

def remove_all(n, m, storage, target):
    for y in range(n):
        for x in range(m):
            if storage[y][x] == target:
                storage[y][x] = 'x'

def remove_edge(n, m, storage, target):
    di = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q = set()
    visited = [[False] * m for _ in range(n)]
    remove_list = []
    for y in [0, n - 1]:
        for x in range(m):
            if storage[y][x] == target:
                remove_list.append((x, y))
            elif storage[y][x] == 'x':
                q.add((x, y))
                visited[y][x] = True
    for x in [0, m - 1]:
        for y in range(n):
            if storage[y][x] == target:
                remove_list.append((x, y))
            elif storage[y][x] == 'x':
                q.add((x, y))
                visited[y][x] = True

    q = deque(q)

    while q:
        x, y = q.popleft()

        for dx, dy in di:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if storage[ny][nx] == target:
                    remove_list.append((nx, ny))
                    visited[ny][nx] = True
                elif storage[ny][nx] == 'x':
                    q.append((nx, ny))
                    visited[ny][nx] = True

    for x, y in remove_list:
        storage[y][x] = 'x'

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])

    for y in range(n):
        storage[y] = list(storage[y])

    for req in requests:
        if len(req) == 1:
            remove_edge(n, m, storage, req[0])
        if len(req) == 2:
            remove_all(n, m, storage, req[0])

    for y in range(n):
        for x in range(m):
            if storage[y][x] != 'x':
                answer += 1

    return answer