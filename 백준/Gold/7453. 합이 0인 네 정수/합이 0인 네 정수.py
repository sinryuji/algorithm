import sys

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
for a in A:
    for b in B:
        AB.append(a + b)
AB.sort()

CD = []
for c in C:
    for d in D:
        CD.append(c + d)
CD.sort()

answer = 0
l, r = 0, len(CD) - 1
while r >= 0 and l < len(AB):
    s = AB[l] + CD[r]
    if s < 0:
        l += 1
    elif s > 0:
        r -= 1
    else:
        l_tmp = l
        while l < len(AB) and AB[l_tmp] == AB[l]:
            l += 1
        r_tmp = r
        while r >= 0 and CD[r_tmp] == CD[r]:
            r -= 1
        answer += (l - l_tmp) * (r_tmp - r)

print(answer)