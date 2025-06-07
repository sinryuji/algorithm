import sys

input = sys.stdin.readline

N = int(input())
s = []

answer = 0
s.append(int(input()))
for _ in range(N - 1):
    h = int(input())
    while s and h >= s[-1]:
        s.pop()
    answer += len(s)
    s.append(h)

print(answer)