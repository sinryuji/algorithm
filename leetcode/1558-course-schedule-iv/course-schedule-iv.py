class Solution:
    def bfs(self, graph, start):
        q = deque([start])
        visited = [False] * len(graph)
        visited[start] = True
        result = set()
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    result.add(nxt)
        return result
    
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        enable = [set() for _ in range(numCourses)]
        for i in range(numCourses):
            enable[i] = self.bfs(graph, i)

        result = []
        for a, b in queries:
            if b in enable[a]:
                result.append(True)
            else:
                result.append(False)

        return result