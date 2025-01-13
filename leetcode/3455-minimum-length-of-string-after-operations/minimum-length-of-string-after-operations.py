class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        for i in range(ord('a'), ord('z') + 1):
            cnt = s.count(chr(i))
            if cnt & 1: res += 1
            elif cnt != 0: res += 2
        return res