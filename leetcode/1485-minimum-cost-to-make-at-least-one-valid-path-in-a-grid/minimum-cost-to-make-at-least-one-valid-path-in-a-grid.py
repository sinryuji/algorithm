class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0)])
        INF = int(1e9)
        row, col = len(grid), len(grid[0])
        min_cost = [[INF] * col for _ in range(row)]
        min_cost[0][0] = 0
        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for idx, (dx, dy) in enumerate(di):
                nx, ny = x + dx, y + dy
                cost = 0 if grid[y][x] == idx + 1 else 1
                if 0 <= nx < col and 0 <= ny < row and min_cost[y][x] + cost < min_cost[ny][nx]:
                    min_cost[ny][nx] = min_cost[y][x] + cost
                    if cost == 1:
                        q.append((nx, ny))
                    else:
                        q.appendleft((nx, ny))
        return min_cost[row-1][col-1]