import sys

input = sys.stdin.readline

N = int(input())
weights = sorted(list(map(int, input().split())))

target = 1
for w in weights:
    if target < w:
        break
    target += w

print(target)