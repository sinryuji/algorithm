import sys

input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

make_x_len = W - f
if make_x_len < W // 2:
    make_x_len = W - make_x_len
split_x = W - make_x_len
split_y = c + 1
total = W * H
n = x2 - x1
if x1 < split_x:
    if x2 > split_x:
        n += split_x - x1
    else:
        n *= 2

print(total - (n * (y2 - y1) * split_y))
