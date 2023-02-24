k = int(input())
direction = []
length = []
for _ in range(6):
    d, l = map(int, input().split())
    direction.append(d)
    length.append(l)
w, h, wi, hi = 0, 0, 0, 0
for i in range(len(direction)):
    if (direction[i] == 1 or direction[i] == 2) and length[i] > w:
        w = length[i]
        wi = i
    if (direction[i] == 3 or direction[i] == 4) and length[i] > h:
        h = length[i]
        hi = i
rwi = wi + 1
if rwi == len(direction):
    rwi = 0
rhi = hi + 1
if rhi == len(direction):
    rhi = 0
small = abs(length[wi - 1] - length[rwi]) * abs(length[hi - 1] - length[rhi])
print((w * h - small) * k)