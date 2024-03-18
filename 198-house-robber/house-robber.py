class Solution:

    def dfs(self , index , nums , dp) :
        if dp[index] != -1 : 
            return dp[index]
        curr_step = nums[index] + self.dfs(index-2 , nums , dp)
        prev_step = self.dfs(index-1 , nums , dp)
        answer = max(curr_step , prev_step)
        dp[index] = answer
        return answer

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0]  , nums[1])
        for i in range(2 , len(nums)):
            dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
        return dp[len(nums)-1]