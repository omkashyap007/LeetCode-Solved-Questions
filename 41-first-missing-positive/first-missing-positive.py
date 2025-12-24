class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
        val = 1
        while i < len(nums) and nums[i] == val:
            i += 1
            val += 1
        if i == len(nums) and nums[-1] <= 0:
            return 1
        return val