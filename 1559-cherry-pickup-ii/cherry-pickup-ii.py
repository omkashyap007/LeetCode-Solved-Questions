class Solution:

    def dfs(self , r , c1  , c2 , ROWS , COLS , grid , cache) :
        if r == ROWS-1 :
            if c1 == c2 :
                return grid[r][c1]
            else :
                return grid[r][c2] + grid[r][c1]
        if (r,c1,c2)  in cache : 
            return cache[(r,c1,c2)]
        if c1 == c2 :
            cc = grid[r][c2]
        else :
            cc = grid[r][c1] + grid[r][c2]
        max_value = float("-inf")
        for i in range(c1-1 , c1+2) :
            for j in range(c2-1 , c2+2):
                if i < 0 or i >= COLS or j < 0 or j >= COLS :
                    continue
                max_value = max(self.dfs(r+1 , i , j , ROWS, COLS,  grid , cache) , max_value)
        cache[(r,c1,c2)] = max_value + cc
        return max_value + cc

    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        c1 = 0
        c2 = COLS-1
        cache = {}
        return self.dfs(0 , c1 , c2 , ROWS , COLS ,  grid , cache)