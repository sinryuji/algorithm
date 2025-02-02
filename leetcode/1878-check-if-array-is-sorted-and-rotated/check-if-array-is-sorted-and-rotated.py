class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for _ in range(n):
            if all(nums[i] <= nums[i+1] for i in range(n-1)):
                return True
            nums.append(nums.pop(0))
        return False