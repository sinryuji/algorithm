while 1:
    l = sorted(list(map(int, input().split())))
    if sum(l) == 0:
        break
    if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        print("right")
    else:
        print("wrong")