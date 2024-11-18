# https://www.acmicpc.net/problem/1929

import math

M, N = map(int, input().split())

array = [True] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        for j in range(i * 2, N + 1, i):
            array[j] = False

if M == 1:
    M += 1
for i in range(M, N + 1):
    if array[i]:
        print(i)
