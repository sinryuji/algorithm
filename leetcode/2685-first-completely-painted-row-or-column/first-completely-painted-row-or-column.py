class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos = dict()
        n, m = len(mat), len(mat[0])

        for row in range(n):
            for col in range(m):
                pos[mat[row][col]] = (row, col)

        row_cnt, col_cnt = [0] * m, [0] * n
        for i in range(len(arr)):
            row, col = pos[arr[i]]
            row_cnt[col] += 1
            col_cnt[row] += 1
            if row_cnt[col] == n or col_cnt[row] == m:
                return i