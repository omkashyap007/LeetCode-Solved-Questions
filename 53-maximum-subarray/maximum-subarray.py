class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_value = nums[0]
        for i in range(1 , len(nums)):
            curr = max(prev + nums[i] , nums[i])
            prev = curr
            max_value = max(curr , max_value)
        return max_value