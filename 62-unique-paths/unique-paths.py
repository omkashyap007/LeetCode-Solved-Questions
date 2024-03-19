class Solution:

    def dfs(self ,  i , j ,dp):
        if dp[i][j] != -1 :
            return dp[i][j]
        dp[i][j] = self.dfs(i-1 , j ,dp) + self.dfs(i , j-1,dp)
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        dp[0][0] = 1
        for i in range(1 , m):
            for j in range(1 , n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]