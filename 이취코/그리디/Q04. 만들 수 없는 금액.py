import sys

input = sys.stdin.readline

N = input()
coins = sorted(map(int, input().split()))

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)