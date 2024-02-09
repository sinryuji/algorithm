import sys
input = sys.stdin.readline

N = int(input())
polygon = [tuple(map(float, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    x1, y1 = polygon[i]
    if i == N - 1:
        x2, y2 = polygon[0]
    else:
        x2, y2 = polygon[i+1]
    answer += x1 * y2 - x2 * y1

print(abs(answer / 2))