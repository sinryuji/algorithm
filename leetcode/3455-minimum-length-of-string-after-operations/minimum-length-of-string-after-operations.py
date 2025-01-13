class Solution:
    def minimumLength(self, s: str) -> int:
        alphabet = [0] * 26
        a = ord('a')
        for c in s:
            alphabet[ord(c) - a] += 1
        n = len(s)
        for alpha in alphabet:
            if alpha > 2:
                n -= (alpha - 1) // 2 * 2
        return n