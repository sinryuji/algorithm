import sys

input = sys.stdin.readline

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(D, C, A) * ccw(D, C, B) < 0:
    print(1)
else:
    print(0)
