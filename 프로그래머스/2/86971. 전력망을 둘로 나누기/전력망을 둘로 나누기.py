from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    cnt = 0
    
    while q:
        cur = q.popleft()
        cnt += 1
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                
    return cnt

def solution(n, wires):
    answer = n
    
    for i in range(n - 1):
        tmp = wires.copy()
        graph = [[] for i in range(n + 1)]
        visited = [False] * (n + 1)
        tmp.pop(i)
        
        for a, b in tmp:
            graph[a].append(b)
            graph[b].append(a)
            
        for i, v in enumerate(graph):
            if v != []:
                start = i
                break
        
        cnt = bfs(start, graph, visited)
        other = n - cnt
        answer = min(answer, abs(cnt - other))
    
    return answer