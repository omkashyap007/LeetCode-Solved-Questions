class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_sum = nums[0]
        for i in range(1 , len(nums)):
            curr = max(prev + nums[i] , nums[i])
            prev = curr
            max_sum = max(curr , max_sum)
        return max_sum