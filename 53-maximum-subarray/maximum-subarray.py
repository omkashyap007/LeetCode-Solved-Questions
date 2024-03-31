class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        the_sum = 0
        max_sum = float("-inf")
        for i in nums :
            the_sum += i
            max_sum = max(the_sum , max_sum)
            the_sum = max(the_sum , 0)
        return max_sum
        prev = nums[0]
        max_sum = nums[0]
        for i in range(1 , len(nums)):
            curr = max(prev + nums[i] , nums[i])
            prev = curr
            max_sum = max(curr , max_sum)
        return max_sum