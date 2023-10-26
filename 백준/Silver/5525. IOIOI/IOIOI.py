N, M, S = int(input()), int(input()), input()

i, count, answer = 0, 0, 0

while i < M - 1:
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)