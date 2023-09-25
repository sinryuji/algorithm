from collections import deque

S = deque(list(input()))
flag = False
stack = []
answer = ''
while S:
    c = S.popleft()
    if c == '<':
        answer += ''.join(stack[::-1])
        stack.clear()
        answer += c
        c = S.popleft()
        while c != '>':
            answer += c
            c = S.popleft()
        answer += c
        continue
    if c == ' ':
        answer += ''.join(stack[::-1]) + ' '
        stack.clear()
        continue
    stack.append(c)
answer += ''.join(stack[::-1])
print(answer)     