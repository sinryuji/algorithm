class Solution:
    def bfs(self, graph, start, end):
        q = deque([start])
        visited = [False] * len(graph)
        visited[start] = True
        while q:
            cur = q.popleft()
            if cur == end:
                return True
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        return False
    
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        result = []
        for a, b in queries:
            result.append(self.bfs(graph, a, b))

        return result