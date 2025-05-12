import sys

input = sys.stdin.readline

arr = input().rstrip()
tmp, ret = 1, 0
stack = []
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
        tmp *= 2
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3
    elif arr[i] == ')':
        if not stack or stack[-1] != '(':
            ret = 0
            break
        if arr[i - 1] == '(':
            ret += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] != '[':
            ret = 0
            break
        if arr[i - 1] == '[':
            ret += tmp
        stack.pop()
        tmp //= 3

if stack:
    ret = 0
print(ret)
