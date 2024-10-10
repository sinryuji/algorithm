import sys

input = sys.stdin.readline

N = int(input())
fears = sorted(list(map(int, input().split())))

answer = 0
count = 0
for fear in fears:
    count += 1
    if count >= fear:
        answer += 1
        count = 0

print(answer)