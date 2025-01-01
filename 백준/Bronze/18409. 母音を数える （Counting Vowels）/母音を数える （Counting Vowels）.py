N, S = input(), input()
answer = 0
for c in S:
    if c in ['a', 'i', 'u', 'e', 'o']:
        answer += 1
print(answer)