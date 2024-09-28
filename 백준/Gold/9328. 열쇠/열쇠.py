import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

di = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    global answer, visited

    q = deque([(0, 0)])
    visited[0][0] = False
    while q:
        x, y = q.popleft()

        for dx, dy in di:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < w + 2 and 0 <= ny < h + 2 and board[ny][
                nx] != '*' and not visited[ny][nx]:
                if board[ny][nx].isupper() and board[ny][nx].lower() not in key:
                    continue
                elif board[ny][nx].islower() and board[ny][nx] not in key:
                    key[board[ny][nx]] = True
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
                elif board[ny][nx] == '$':
                    answer += 1
                    board[ny][nx] = '.'
                visited[ny][nx] = True
                q.append((nx, ny))


for _ in range(T):
    h, w = map(int, input().split())
    board = [list('.' + input().rstrip() + '.') for _ in range(h)]
    board = [list('.' * (w + 2))] + board + [list('.' * (w + 2))]
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    key = {}
    visited_doc = []

    for c in input().rstrip():
        if c.isalpha():
            key[c] = True

    answer = 0
    bfs()
    print(answer)