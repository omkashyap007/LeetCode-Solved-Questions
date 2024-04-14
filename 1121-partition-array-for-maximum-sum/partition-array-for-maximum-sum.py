class Solution:

    def dfs(self , index , arr , dp , k):

        if index < 0 :
            return 0
        if index == 0 : 
            return arr[index]

        if index in dp :
            return dp[index]
        
        max_value = -1
        max_sum = 0
        for j in range(index , max(-1, index-k) , -1) :
            max_value = max(max_value , arr[j])
            max_sum = max(self.dfs(j-1 , arr , dp , k) + max_value * (index-j+1) , max_sum)
        dp[index] = max_sum
        return max_sum

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {0:arr[0]}
        self.dfs(len(arr)-1 , arr , dp , k)
        print(dp)
        return dp[len(arr)-1]