class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[-1 for _ in range(COLS)] for _  in range(ROWS)]
        dp[0][0] = grid[0][0]
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j == 0 :
                    continue
                value = grid[i][j]
                top = dp[i-1][j] if i-1>=0 else float("inf")
                left = dp[i][j-1] if j-1>=0 else float("inf")
                dp[i][j] = value + min(top , left)
        return dp[ROWS-1][COLS-1]