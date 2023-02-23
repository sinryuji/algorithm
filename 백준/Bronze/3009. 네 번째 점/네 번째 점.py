xl, yl = [], []
for _ in range(3):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)
for i in range(3):
    if xl.count(xl[i]) == 1:
        retX = xl[i]
    if yl.count(yl[i]) == 1:
        retY = yl[i]
print(retX, retY)