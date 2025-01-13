import sys

input = sys.stdin.readline

N = int(input())
stack = []
result = []
for _ in range(N):
    cmd = input()
    if cmd[0] == '1':
        stack.append(int(cmd[2:]))
    elif cmd[0] == '2':
        result.append(stack.pop() if stack else -1)
    elif cmd[0] == '3':
        result.append(len(stack))
    elif cmd[0] == '4':
        result.append(int(not stack))
    else:
        result.append(stack[-1] if stack else -1)

print(*result, sep='\n')