class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret = 0
        for s in words:
            if s.startswith(pref):
                ret += 1
        return ret