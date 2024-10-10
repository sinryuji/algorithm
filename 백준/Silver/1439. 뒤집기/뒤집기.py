S = input()

zero, one, idx = 0, 0, 0
while idx < len(S):
    if S[idx] == '0':
        zero += 1
        while idx < len(S) and S[idx] == '0':
            idx += 1
    elif S[idx] == '1':
        one += 1
        while idx < len(S) and S[idx] == '1':
            idx += 1

print(min(zero, one))