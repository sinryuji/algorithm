import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    seq = list(map(int, input().split()))[1:]
    seq_len = len(seq)
    for i in range(seq_len):
        for j in range(i + 1, seq_len):
            graph[seq[i]].append(seq[j])
            indegree[seq[j]] += 1

ans = []
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    ans.append(cur)
    for next_ in graph[cur]:
        indegree[next_] -= 1
        if indegree[next_] == 0:
            q.append(next_)
            
if len(ans) == n:
    print(*ans, sep='\n')
else:
    print(0)