class Solution:

    # def dfs(self , i , j , grid , dp) :
    #     if dp[i][j] != -1 :
    #         return dp[i][j]
    #     top = 0
    #     left = 0
    #     if grid[i][j] == 1 :
    #         dp[i][j] = 0
    #         return 0
    #     if i-1 >= 0 :
    #         top = self.dfs(i-1 , j , grid , dp)
    #     if j-1 >= 0 :
    #         left = self.dfs(i , j-1,  grid , dp)
    #     dp[i][j] = top+left
    #     return top+left
            

    def uniquePathsWithObstacles(self, grid : List[List[int]]) -> int:
        if grid[0][0] == 1 : 
            return 0
        dp = [
            [0 for _ in range(len(grid[0]))] for _ in range(len(grid))
        ]
        dp[0][0] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if i == 0 and j == 0 :
                    continue
                if grid[i][j] == 1 :
                    dp[i][j] = 0
                else :
                    top = 0
                    left = 0
                    if i-1>=0 :
                        top = dp[i-1][j]
                    if j-1>=0 :
                        left = dp[i][j-1]
                    dp[i][j] = top+left
        print(dp)
        return dp[-1][-1]