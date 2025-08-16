class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        answer = int(''.join(s))

        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                answer = max(answer, int(''.join(s)))
                s[i] = '6'

        return answer