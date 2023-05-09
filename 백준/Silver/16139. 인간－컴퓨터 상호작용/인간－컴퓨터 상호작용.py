import sys
input = sys.stdin.readline

s = input()
q = int(input())
alpha = [0] * 26
for _ in range(q):
    a, start, end = input().split()
    print(s.count(a, int(start), int(end) + 1))