N, K = map(int, input().split())
table = list(input())

answer = 0
for i in range(N):
    if table[i] != 'P':
        continue
    for j in range(i - K, i + K + 1):
        if 0 <= j < N:
            if table[j] == 'H':
                table[j] = 'X'
                answer += 1
                break

print(answer)