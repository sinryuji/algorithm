import sys

input = sys.stdin.readline


def bisection_right(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right


def bisection_left(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left



T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

psa, psb = [], []
for i in range(n):
    s = A[i]
    psa.append(s)
    for j in range(i + 1, n):
        s += A[j]
        psa.append(s)
for i in range(m):
    s = B[i]
    psb.append(s)
    for j in range(i + 1, m):
        s += B[j]
        psb.append(s)

psa.sort()
psb.sort()
ans = 0
for i in range(len(psa)):
    l = bisection_left(psb, T - psa[i])
    r = bisection_right(psb, T - psa[i])
    ans += r - l + 1

print(ans)