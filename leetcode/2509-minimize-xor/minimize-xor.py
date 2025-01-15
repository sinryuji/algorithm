class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1, n2 = bin(num1)[2:], bin(num2)[2:]
        n = max(len(n1), len(n2))
        if len(n1) < n:
            n1 = '0' * (n - len(n1)) + n1
        elif len(n2) < n:
            n2 = '0' * (n - len(n2)) + n2
        cnt = n2.count('1')
        res = []
        for c in n1:
            if cnt and c == '1':
                res.append('1')
                cnt -= 1
            else:
                res.append('0')

        if cnt:
            for i in range(len(res)-1, -1, -1):
                if not cnt:
                    break
                if res[i] == '0':
                    res[i] = '1'
                    cnt -= 1

        return int(''.join(res), 2)