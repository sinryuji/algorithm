class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        s = set()
        for row in range(n):
            tmp = []
            for col in range(m):
                if grid[row][col] == 1:
                    tmp.append((row, col))
            if len(tmp) > 1:
                s.update(tmp)

        for col in range(m):
            tmp = []
            for row in range(n):
                if grid[row][col] == 1:
                    tmp.append((row, col))
            if len(tmp) > 1:
                s.update(tmp)

        return len(s)