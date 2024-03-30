board = input()
answer = ''

cnt = 0
for c in board:
    if c == '.':
        if cnt == 2:
            answer += 'BB'
        elif cnt != 0:
            answer = '-1'
            break
        cnt = 0
        answer += c
        continue
    cnt += 1
    if cnt == 4:
        cnt = 0
        answer += 'AAAA'

if cnt == 2:
    answer += 'BB'
elif cnt != 0:
    answer = '-1'

print(answer)