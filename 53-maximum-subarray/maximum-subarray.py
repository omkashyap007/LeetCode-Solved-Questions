class Solution:

    def dfs(self , index , nums , dp , max_val):
        if dp[index] != - 1 : 
            return dp[index]
        if index < 0 :
            return float("-inf")
        max_sum = max(self.dfs(index-1 , nums , dp , max_val )+ nums[index] , nums[index])
        dp[index] = max_sum
        max_val[0] = max(max_val[0] , max_sum)
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        max_val = [float("-inf")]
        self.dfs(len(nums)-1 , nums , dp , max_val )
        return max_val[0]