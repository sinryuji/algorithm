import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = input()
    if cmd[0] == '1':
        stack.append(int(cmd[2:]))
    elif cmd[0] == '2':
        print(stack.pop() if stack else -1)
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        print(int(not stack))
    else:
        print(stack[-1] if stack else -1)
