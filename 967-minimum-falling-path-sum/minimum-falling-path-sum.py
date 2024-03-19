class Solution:

    def dfs(self , index , i ,  matrix , dp):
        if i < 0 or i >= len(matrix) :
            return float("inf")
        if index < 0 :
            return float("inf")
        if dp[index][i] != - 1 :
            return dp[index][i]
        value = matrix[index][i]
        min_value = float("inf")
        for j in [-1 , 0 , 1]:
            a = self.dfs(index-1 , i+j , matrix , dp)
            min_value = min(min_value , a)
        if min_value == float("inf") :
            dp[index][i] = value
            return value
        else :
            dp[index][i] = value + min_value
            return value + min_value
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1 , n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] + min([
                    matrix[i-1][j] , 
                    matrix[i-1][j-1] if j-1 >= 0 else float("inf") , 
                    matrix[i-1][j+1] if j+1 < n else float("inf")
                    ]
                )
        return min(matrix[-1])