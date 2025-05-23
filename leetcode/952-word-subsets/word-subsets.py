class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for word in words2:
            count |= Counter(word)
        return [word for word in words1 if not count - Counter(word)]