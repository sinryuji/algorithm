from itertools import combinations
import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
for s in combinations(heights, 7):
    if sum(s) == 100:
        print(*sorted(list(s)), sep='\n')
        break