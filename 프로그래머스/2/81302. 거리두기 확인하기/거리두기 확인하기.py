from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, place):
    # print(x, y)
    q = deque([(x, y, 0, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[y][x] = True

    while q:
        # print(q)
        x, y, dist, partition = q.popleft()
        if dist > 1 or partition > 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                if place[ny][nx] == 'P':
                    # print('false', nx, ny, dist, partition)
                    return False
                visited[ny][nx] = True
                # if place[ny][nx] == 'X':
                #     partition += 1
                q.append((nx, ny, dist + 1, partition + 1 if place[ny][nx] == 'X' else partition))
    return True


def solution(places):
    answer = []

    for place in places:
        positions = []
        for x in range(5):
            for y in range(5):
                if place[y][x] == 'P':
                    positions.append((x, y))
        res = True
        for x, y in positions:
            if not bfs(x, y, place):
                res = False
                break
        answer.append(1 if res else 0)

    return answer
