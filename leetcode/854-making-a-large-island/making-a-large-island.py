class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        island = []

        def bfs(r, c, num):
            q = deque([(r, c)])
            visited[r][c] = True
            grid[r][c] = num
            size = 1
            while q:
                r, c = q.popleft()
                for dr, dc in di:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                        size += 1
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        grid[nr][nc] = num
            return size

        visited = [[False] * m for _ in range(n)]
        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_num = 1
        island_size = [0]
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and not visited[row][col]:
                    island_size.append(bfs(row, col, island_num))
                    island_num += 1

        largest_size = max(island_size)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    neighbor = set()
                    for dr, dc in di:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 0:
                            neighbor.add(grid[nr][nc])
                    s = 1 + sum(island_size[i] for i in neighbor)
                    largest_size = max(largest_size, s)

        return largest_size