import sys
input = sys.stdin.readline

n = int(input())
line = [int(input()) for _ in range(n)]
stack = []
result = 0

for i in line:
    while stack and stack[-1][0] < i:
        result += stack.pop()[1]
        
    if not stack:
        stack.append((i, 1))
        continue
    
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        result += cnt
        if stack: result += 1
        stack.append((i, cnt + 1))
    else:
        stack.append((i, 1))
        result += 1
        
print(result)