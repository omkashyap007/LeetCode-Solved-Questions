class Solution:

    def dfs(self , i , j , matrix , cache) :
        if i < 0 :
            return 0
        if (i,j) in cache : 
            return cache[(i,j)]
        value =  matrix[i][j] + min(
            [
                self.dfs(i-1 , j-1 , matrix , cache) if j-1>=0 else float("inf") ,
                self.dfs(i-1 , j , matrix , cache) ,
                self.dfs(i-1 , j+1 , matrix , cache) if j+1< len(matrix) else float("inf")
            ]
        )
        cache[(i,j)] = value
        return value
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        answer = float("inf")
        cache = {}
        for i in range(len(matrix)):
            answer = min(self.dfs(len(matrix)-1 , i , matrix , cache ) , answer)
        return answer