import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = []
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if ((cx - x1) ** 2 + (cy - y1) ** 2 - r ** 2) * ((cx - x2) ** 2 + (cy - y2) ** 2 - r ** 2) < 0:
            cnt += 1
    print(cnt)