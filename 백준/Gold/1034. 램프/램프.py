import sys

input = sys.stdin.readline

N, M = map(int, input().split())
table = [input() for _ in range(N)]
K = int(input())

answer = 0

for row in range(N):
    zero_cnt = table[row].count('0')
    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        row_cnt = 0
        for row2 in range(N):
            if table[row] == table[row2]:
                row_cnt += 1
        answer = max(answer, row_cnt)

print(answer)