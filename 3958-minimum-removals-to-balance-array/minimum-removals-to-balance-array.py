class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 0
        max_len = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] <= nums[i]*k:
                j += 1
            max_len = max((j-i), max_len)
        return len(nums) - max_len