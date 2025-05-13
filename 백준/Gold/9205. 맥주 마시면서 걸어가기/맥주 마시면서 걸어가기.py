import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque([(home_x, home_y)])
    visited = [False] * (n + 1)
    while q:
        x, y = q.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return 'happy'
        for i in range(n):
            if not visited[i]:
                store_x, store_y = stores[i]
                if abs(x - store_x) + abs(y - store_y) <= 1000:
                    visited[i] = True
                    q.append((store_x, store_y))
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    stores = []
    for _ in range(n):
        stores.append(tuple(map(int, input().split())))
    festival_x, festival_y = map(int, input().split())
    print(bfs())