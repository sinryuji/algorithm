import sys
from functools import cmp_to_key

input = sys.stdin.readline

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def compare_dist(p1, p2):
    d1 = p1[0] ** 2 + p1[1] ** 2
    d2 = p2[0] ** 2 + p2[1] ** 2
    return d1 > d2

def comp(p1, p2):
    direction = ccw([0, 0], p1, p2)
    if direction > 0:
        return -1
    if direction == 0:
        if compare_dist(p1, p2):
            return 1
        else:
            return -1
    if direction < 0:
        return 1

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: (x[1], x[0]))
start = points[0]

shifted_points = [[x - start[0], y - start[1]] for x, y in points[1:]]
shifted_points.sort(key=cmp_to_key(comp))
points = [[x + start[0], y + start[1]] for x, y in shifted_points]

stack = [start, points[0]]

for p in points[1:]:
    while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <= 0:
        stack.pop()
    stack.append(p)

print(len(stack))
