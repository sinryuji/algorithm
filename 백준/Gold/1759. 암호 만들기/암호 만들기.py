import sys
from itertools import combinations

input = sys.stdin.readline


L, C = map(int, input().split())
alphas = sorted(list(input().split()))
words = combinations(alphas, L)

for word in words:
    if len(word) != L:
        continue
    cnt = 0
    for i in word:
        if i in 'aeiou':
            cnt += 1

    if cnt >= 1 and len(word) - cnt >= 2:
        print(''.join(word))