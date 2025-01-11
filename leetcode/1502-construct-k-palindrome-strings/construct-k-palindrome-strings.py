class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(i & 1 for i in Counter(s).values()) <= k <= len(s)