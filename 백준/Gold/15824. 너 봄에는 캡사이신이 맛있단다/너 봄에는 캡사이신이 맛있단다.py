import sys

input = sys.stdin.readline

N = int(input())
menu = sorted(list(map(int, input().split())))

answer = 0
d = 1000000007

for i in range(N):
    answer += menu[i] * (pow(2, i, d) - pow(2, N - i - 1, d))
print(answer % d)
