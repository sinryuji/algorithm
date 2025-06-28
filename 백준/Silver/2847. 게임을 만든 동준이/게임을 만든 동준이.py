import sys

input = sys.stdin.readline

N = int(input())
score = list(int(input()) for _ in range(N))

answer = 0
for i in range(N - 1, 0, -1):
    if score[i] <= score[i - 1]:
        diff = score[i - 1] - score[i] + 1
        score[i - 1] -= diff
        answer += diff
        
print(answer)