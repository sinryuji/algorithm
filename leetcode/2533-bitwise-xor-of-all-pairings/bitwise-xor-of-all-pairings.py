class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n1, n2 = len(nums1), len(nums2)

        if n1 & 1:
            for n in nums2:
                res ^= n
        if n2 & 1:
            for n in nums1:
                res ^= n

        return res