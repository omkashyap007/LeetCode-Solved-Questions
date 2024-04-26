class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = [i for i in grid[0]]
        for i in range(1,len(grid)):
            curr = [j for j in grid[i]]
            for j in range(len(grid[0])) :
                min_value = float("inf")
                for k in range(len(grid[0])) :
                    if k == j : 
                        continue
                    min_value = min(dp[k] , min_value)
                    curr[j] = min_value + grid[i][j]
            dp = curr
        return min(dp)