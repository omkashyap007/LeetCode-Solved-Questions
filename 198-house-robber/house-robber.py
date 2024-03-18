class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            c = max(nums[i] + a , b)
            a = b
            b = c
        return b