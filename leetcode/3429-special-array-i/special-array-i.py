class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        odd = False
        if nums[0] & 1:
            odd = True
        for n in nums:
            if odd and not n & 1:
                return False
            if not odd and n & 1:
                return False
            odd = not odd
        return True