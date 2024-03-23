class Solution:

    def dfs(self , i , j , matrix , dp) :
        if i < 0 :
            return 0
        if dp[i][j] != -1 : 
            return dp[i][j]
        value =  matrix[i][j] + min(
            [
                self.dfs(i-1 , j-1 , matrix , dp) if j-1>=0 else float("inf") ,
                self.dfs(i-1 , j , matrix , dp) ,
                self.dfs(i-1 , j+1 , matrix , dp) if j+1< len(matrix) else float("inf")
            ]
        )
        dp[i][j] = value
        return value
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        answer = float("inf")
        n = len(matrix)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1,n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(
                    [
                        dp[i-1][j-1] if j-1>=0 else float("inf") ,
                        dp[i-1][j] ,
                        dp[i-1][j+1] if j+1< len(matrix) else float("inf")
                    ]
                )
        return min(dp[n-1])