N, r, c = map(int, input().split())
answer = 0

while N != 0:
    N -= 1
    l = 2 ** N
    if r < l and c < l:
        answer += l * l * 0
    elif r < l and c >= l:
        answer += l * l * 1
        c -= l
    elif r >= l and c < l:
        answer += l * l * 2
        r -= l
    else:
        answer += l * l * 3
        r -= l
        c -= l

print(answer)