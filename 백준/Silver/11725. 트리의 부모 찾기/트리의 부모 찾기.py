from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [0] * (N + 1)

queue = deque([1])
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if answer[i] == 0:
            answer[i] = str(x)
            queue.append(i)

sys.stdout.write('\n'.join(answer[2:]))