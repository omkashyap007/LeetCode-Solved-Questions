class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 :
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        dp[0][0] = 1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else :
                    if i==0 and j == 0 :
                        continue
                    up = dp[i-1][j] if i-1>=0 else 0
                    left = dp[i][j-1] if j-1>=0 else 0
                    dp[i][j] = up+left
        return dp[ROWS-1][COLS-1]