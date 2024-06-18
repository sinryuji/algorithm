import sys

input = sys.stdin.readline

N = int(input())
times = []
for _ in range(N):
    T, S = map(int, input().split())
    times.append((T, S))

times.sort(key=lambda x: x[1])

answer = 0

for i in range(1000000):
    flag = True
    sum_ = i
    for t, s in times:
        sum_ += t
        if sum_ > s:
            flag = False
            break
    if not flag:
        if i == 0:
            answer = -1
        else:
            answer = i - 1
        break

print(answer)