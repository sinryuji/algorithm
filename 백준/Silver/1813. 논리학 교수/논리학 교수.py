N = int(input())
board = list(map(int, input().split()))

answer = -1
for i in range(N + 1):
    cnt = board.count(i)
    if cnt == i:
        answer = max(answer, cnt)

print(answer)