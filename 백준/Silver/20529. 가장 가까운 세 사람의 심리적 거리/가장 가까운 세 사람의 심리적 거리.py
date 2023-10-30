from itertools import combinations

def get_distance(a, b):
    ret = 0
    for i in range(4):
        if a[i] != b[i]:
            ret += 1
    return ret

for _ in range(int(input())):
    N = int(input())
    mbtis = input().split()

    if N > 32:
        print(0)
    else:
        combi = combinations(mbtis, 3)
        ret = 13
        for a, b, c in combi:
            total = 0
            total += get_distance(a, b)
            total += get_distance(b, c)
            total += get_distance(a, c)
            ret = min(ret, total)
        print(ret)