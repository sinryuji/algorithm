import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        clothes.append(input().split()[1])
    clothes = Counter(clothes)
    ret = 1
    for i in clothes.values():
        ret *= i + 1
    print(ret - 1)