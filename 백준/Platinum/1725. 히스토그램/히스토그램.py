import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in range(n):
    while len(stack) != 0 and h[stack[-1]] > h[i]:
        tmp = stack.pop()
            
        if len(stack) == 0:
            width = i 
        else:
            width = i - stack[-1] - 1
        answer = max(answer, width * h[tmp])
    stack.append(i)
    
while len(stack) != 0:
    tmp = stack.pop()
        
    if len(stack) == 0:
        width = n
    else:
        width = n - stack[-1] - 1
    answer = max(answer, width * h[tmp])
        
print(answer)