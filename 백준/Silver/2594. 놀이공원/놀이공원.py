import sys

input = sys.stdin.readline

N = int(input())
times = [(600, 600), (1320, 1320)]
for _ in range(N):
    start, end = map(int, input().split())
    times.append(
        ((start // 100 * 60) + (start % 100) - 10, (end // 100 * 60) + (end % 100) + 10))

times.sort()

answer = 0
last = 600

for start, end in times:
    answer = max(answer, start - last)
    last = max(last, end)

print(answer)