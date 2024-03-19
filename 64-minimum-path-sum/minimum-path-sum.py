class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [float("inf") for _ in range(COLS)]
        prev_j = float("inf")
        dp[0] = grid[0][0]
        for i in range(ROWS):
            temp = [-1 for _ in range(COLS)]
            prev_j = float("inf")
            for j in range(COLS):
                if i == 0 and j == 0 :
                    prev_j = grid[i][j]
                    temp[j] = prev_j
                else :
                    value = grid[i][j]
                    top = dp[j]
                    left = prev_j
                    temp[j] = value + min(top , left)
                    prev_j = temp[j]
            dp = temp
        return dp[-1]