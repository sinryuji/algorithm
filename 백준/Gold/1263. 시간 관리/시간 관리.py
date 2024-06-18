import sys

input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    T, S = map(int, input().split())
    times.append((T, S))

times.sort(key=lambda x: x[1], reverse=True)

answer = times[0][1] - times[0][0]

for i in times[1:]:
    if answer > i[1]:
        answer = i[1] - i[0]
    else:
        answer -= i[0]

print(-1 if answer <= 0 else answer)