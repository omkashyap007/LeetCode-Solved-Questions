class Solution:

    def dfs(self , i , j , matrix , cache ):
        if j < 0 or j >= len(matrix[0]) :
            return float("inf")
        if i == 0 :
            return matrix[i][j]
        if (i,j) in cache : 
            return cache[(i,j)]
        min_value = float("inf")
        for k in range(j-1 , j+2) :
            min_value = min(
                self.dfs(i-1, k ,  matrix , cache), min_value
            )
        cache[(i,j)] = matrix[i][j] + min_value
        return matrix[i][j] + min_value

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        max_value = float("inf")
        cache = {}
        for i in range(len(matrix[0])):
            max_value = min( self.dfs(len(matrix)-1 , i , matrix , cache ) , max_value)
        return max_value