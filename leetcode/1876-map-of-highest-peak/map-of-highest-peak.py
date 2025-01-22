class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        result = [[-1] * m for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    q.append((i, j, 0))

        di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            row, col, height = q.popleft()
            for dr, dc in di:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m and result[nr][nc] == -1:
                    result[nr][nc] = height + 1
                    q.append((nr, nc, height + 1))

        return result