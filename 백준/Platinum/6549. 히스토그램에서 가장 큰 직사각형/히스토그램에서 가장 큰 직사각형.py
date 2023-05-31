import sys
input = sys.stdin.readline

while True:
    h = list(map(int, input().split()))
    n = h.pop(0)
    if n == 0:
        break
        
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