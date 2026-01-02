class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l = len(nums)//2
        for i in nums:
            if nums.count(i) == l:
                return i