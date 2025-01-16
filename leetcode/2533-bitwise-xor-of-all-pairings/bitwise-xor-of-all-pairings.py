class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        d = defaultdict(int)
        l1, l2 = len(nums1), len(nums2)

        for n1 in nums1:
            d[n1] += l2
        for n2 in nums2:
            d[n2] += l1

        res = 0
        for k, v in d.items():
            if v & 1:
                res ^= k

        return res