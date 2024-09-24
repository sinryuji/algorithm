from collections import deque

def solution(x, y, n):
    visited = [False] * (y + 1)
    visited[x] = True

    q = deque([(x, 0)])
    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt
        if cur + n <= y and not visited[cur + n]:
            visited[cur + n] = True
            q.append((cur + n, cnt + 1))
        if cur * 2 <= y and not visited[cur * 2]:
            visited[cur * 2] = True
            q.append((cur * 2, cnt + 1))
        if cur * 3 <= y and not visited[cur * 3]:
            visited[cur * 3] = True
            q.append((cur * 3, cnt + 1))

    return -1
