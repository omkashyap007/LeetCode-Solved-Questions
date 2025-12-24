class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        val = 1
        while val in nums:
            val += 1
        return val