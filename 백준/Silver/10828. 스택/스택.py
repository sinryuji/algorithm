import sys
input = sys.stdin.readline

stack = []
n = int(input())

def pop():
    global stack
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def empty():
    global stack
    if len(stack) == 0:
        print(1)
    else:
        print(0)
        
def top():
    global stack
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        
for _ in range(n):
    cmd = input().rstrip()
    if cmd == "pop":
        pop()
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        empty()
    elif cmd == "top":
        top()
    else:
        cmd, val = cmd.split()
        stack.append(val)