n, m = map(int, input().split())
a, b, d = map(int, input().split())
visit = [[a, b]]
m = []
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(n):
    m.append(list(map(int, input().split())))
flag = True
while flag:
    flag = False
    for _ in range(len(direction)):
        d -= 1
        if d < 0:
            d = 3
        da = a + direction[d][0]
        db = b + direction[d][1]
        if m[da][db] != 1 and [da, db] not in visit:
            visit.append([da, db])
            a, b = da, db
            flag = True
            break
    if flag == False:
        da = a - direction[d][0]
        db = b - direction[d][1]
        if m[da][db] == 0:
            a, b = da, db
            flag = True
        else:
            break
print(len(visit))
