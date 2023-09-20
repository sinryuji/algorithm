from collections import deque

N, K = map(int, input().split())
stack = deque([i for i in range(1, N + 1)])
answer = []
    
while stack:
    for _ in range(K - 1):
        stack.append(stack.popleft())
    answer.append(stack.popleft())
    
print('<', end='')
print(*answer, sep=', ', end='')
print('>', end='')