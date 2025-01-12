class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def validate(s: str, locked: str, op: str) -> bool:
            left = unlock = 0
            for i in range(len(s)):
                if locked[i] == '1':
                    left += 1 if s[i] == op else -1
                else:
                    unlock += 1
                if left + unlock < 0:
                    return False
            return left <= unlock
        return len(s) % 2 == 0 and validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')
