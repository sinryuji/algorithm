import sys
input = sys.stdin.readline

n = int(input())
i = 1
stack = []
ret = []
for _ in range(n):
    num = int(input())
    while len(stack) == 0 or stack[-1] != num and i <= num:
        stack.append(i)
        ret.append('+')
        i += 1
    while len(stack) > 0 and stack[-1] == num:
        stack.pop()
        ret.append('-')
if len(stack) == 0:
    print(*ret, sep = '\n')
else:
    print("NO")