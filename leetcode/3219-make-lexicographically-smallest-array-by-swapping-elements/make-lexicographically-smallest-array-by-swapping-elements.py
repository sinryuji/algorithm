class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)

        cur_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = cur_group

        group_to_list = {}
        group_to_list[cur_group] = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                cur_group += 1

            num_to_group[nums_sorted[i]] = cur_group

            if cur_group not in group_to_list:
                group_to_list[cur_group] = deque()
            group_to_list[cur_group].append(nums_sorted[i])

        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()

        return nums