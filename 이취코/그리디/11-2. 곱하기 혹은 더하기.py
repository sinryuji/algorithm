S = list(map(int, input()))

answer = S[0]
for n in S[1:]:
    if n <= 1 or answer <= 1:
        answer += n
    else:
        answer *= n

print(answer)