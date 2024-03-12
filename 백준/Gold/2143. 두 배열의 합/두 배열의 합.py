import sys

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

psa = {}
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        if s in psa:
            psa[s] += 1
        else:
            psa[s] = 1

psb = {}
ans = 0
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        if T - s in psa:
            ans += psa[T - s]
            
print(ans)