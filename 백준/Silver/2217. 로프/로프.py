import sys

input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)

answer = 0
for i in range(N):
    weight = ropes[i] * (i + 1)
    answer = max(answer, weight)

print(answer)