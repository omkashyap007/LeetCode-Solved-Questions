class Solution:

    def dfs(self , index ,  arr , k ,  dp) : 
        if index in dp : 
            return dp[index]
        max_value = 0
        result = 0
        for i in range(index , min(len(arr) , (index+k))) :
            max_value = max(max_value , arr[i])
            next_partition_max = self.dfs(i+1 , arr , k , dp)
            result = max( result , max_value*(i-index+1) + next_partition_max)
        dp[index] = result
        return result

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {len(arr):0}
        return self.dfs(0 , arr , k ,  dp )