import sys

sys.stdin.readline()
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
print(len(a - b) + len(b - a))