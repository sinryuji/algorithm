exp = list(input())
stack = []
answer = ''

for c in exp:
    if c.isalpha():
        answer += c
    elif c == '(':
        stack.append(c)
    elif c == '*' or c == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(c)
    elif c == '+' or c == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
while stack:
    answer += stack.pop()
print(answer)