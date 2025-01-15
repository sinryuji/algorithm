class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_cnt1, bit_cnt2 = bin(num1).count('1'), bin(num2).count('1')
        diff = bit_cnt1 - bit_cnt2
        
        if diff > 0:
            x = 1
            while diff > 0:
                if num1 & x:
                    num1 ^= x
                    diff -= 1
                x <<= 1
        elif diff < 0:
            x = 1
            while diff < 0:
                if not num1 & x:
                    num1 |= x
                    diff += 1
                x <<= 1

        return num1