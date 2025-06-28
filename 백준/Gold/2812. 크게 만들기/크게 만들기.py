N, K = map(int, input().split())
num = list(map(int, input()))

stack = []
for n in num:
    while stack and K > 0 and stack[-1] < n:
        stack.pop()
        K -= 1
    stack.append(n)

for _ in range(K):
    stack.pop()

print(''.join(map(str, stack)))