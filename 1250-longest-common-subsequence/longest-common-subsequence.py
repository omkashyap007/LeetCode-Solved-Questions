class Solution:

    def dfs(self , i , j , s , p , cache):
        if i < 0 or j < 0 :
            return 0
        if (i,j) in cache :
            return cache[(i,j)]
        if s[i] == p[j] :
            value =  1 + self.dfs(i-1 , j-1 , s , p , cache)
        else : 
            value = max(self.dfs(i-1 , j , s , p , cache) , self.dfs(i, j-1 , s , p , cache))
            cache[(i,j)] = value
        return value
            

    def longestCommonSubsequence(self, s: str, p: str) -> int:
        dp = [[0 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)) :
            for j in range(len(p)) :
                if s[i] == p[j] :
                    dp[i+1][j+1] = 1 + dp[i][j]
                else : 
                    dp[i+1][j+1] = max(
                        dp[i+1][j] , 
                        dp[i][j+1]
                    )
        return dp[-1][-1]
