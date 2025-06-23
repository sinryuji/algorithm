import sys

input = sys.stdin.readline

N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = 0
while arr:
    x = arr.pop()
    while arr and x - L + 1 <= arr[-1]:
        arr.pop()
    answer += 1

print(answer)