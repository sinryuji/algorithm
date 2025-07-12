import sys

input = sys.stdin.readline

N = int(input())
seats = input().rstrip().replace('LL', 'X')

print(len(seats) + (1 if 'X' in seats else 0))