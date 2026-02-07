class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_delete, b = 0, 0

        for c in s:
            if c == 'a':
                min_delete = min(min_delete + 1, b)
            else:
                b += 1
        
        return min_delete
            