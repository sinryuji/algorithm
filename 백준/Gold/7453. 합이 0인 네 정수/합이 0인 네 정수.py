import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    dict_ = dict()
    answer = 0

    for a in A:
        for b in B:
            ab = a + b
            if ab in dict_:
                dict_[ab] += 1
            else:
                dict_[ab] = 1

    for c in C:
        for d in D:
            cd = -(c + d)
            if cd in dict_:
                answer += dict_[cd]

    print(answer)

solve()