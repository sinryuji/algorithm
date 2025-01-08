class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                result += self.isPrefixAndSuffix(words[i], words[j])
        return result