class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        i = 0
        ROWS, COLS = len(grid), len(grid[0])
        j = COLS-1
        while i < ROWS:
            while j >= 0:
                if grid[i][j] < 0:
                    j -= 1
                else:
                    break
            count += (COLS -(j + 1))
            i += 1
        return count
