class Solution:
    def bfs(self, grid, visited, n, m, r, c):
        q = deque([(r, c)])
        visited[r][c] = True
        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = grid[r][c]
        while q:
            r, c = q.popleft()
            for dr, dc in di:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    result += grid[nr][nc]
                    q.append((nr, nc))
        return result

    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        result = 0
        visited = [[False] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if grid[r][c] > 0 and not visited[r][c]:
                    result = max(result, self.bfs(grid, visited, n, m, r, c))

        return result
