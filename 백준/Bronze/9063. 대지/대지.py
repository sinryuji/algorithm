import sys
input = sys.stdin.readline

n = int(input())
point_x = []
point_y = []
for _ in range(n):
    x, y = map(int, input().split())
    point_x.append(x)
    point_y.append(y)
if n == 1:
    print(0)
else:
    print((max(point_x) - min(point_x)) * (max(point_y) - min(point_y)))