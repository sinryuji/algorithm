from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append(N)
arr = [-1] * 100001
arr[N] = 0
result = 0

while queue:
    x = queue.popleft()
    if x == K:
        result += 1
        continue
    for nx in (x*2, x+1, x-1):
        if 0 <= nx <= 100000 and (arr[nx] == arr[x] + 1 or arr[nx] == -1):
            arr[nx] = arr[x] + 1
            queue.append(nx)

print(arr[K])
print(result)