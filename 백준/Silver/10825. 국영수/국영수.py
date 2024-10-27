import sys

input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
    name, a, b, c = input().rstrip().split()
    score.append([name, int(a), int(b), int(c)])

score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, a, b, c in score:
    print(name)
