from collections import deque

N, K = map(int, input().split())


def get_path(start, pos):
    res = [pos]
    while pos != start:
        pos = path[pos]
        res.append(pos)
    return res[::-1]


m = 100000
q = deque([(N, 0)])
visited = [False] * (m + 1)
visited[N] = True
path = [0] * (m + 1)
while q:
    pos, sec = q.popleft()
    if pos == K:
        print(sec)
        print(*get_path(N, pos))
        break
    for i in (pos - 1, pos + 1, pos * 2):
        if 0 <= i <= m and not visited[i]:
            visited[i] = True
            path[i] = pos
            q.append((i, sec + 1))
