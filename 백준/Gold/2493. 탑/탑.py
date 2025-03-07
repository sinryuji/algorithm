import sys

input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []
answer = [0] * N
for i, v in enumerate(heights):
    while stack:
        if stack[-1][1] > v:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, v))
    
print(*answer)