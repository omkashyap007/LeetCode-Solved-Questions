class Solution:

    def dfs(self , r1  , c1 , r2 , c2 , grid , cache) :
        N = len(grid)
        if not (0<=r1<N and 0<=c1<N and 0<=r2<N and 0<=c2<N): return -inf
        if not (grid[r1][c1]!=-1 and grid[r2][c2]!=-1): return -inf
        if r1 == r2 == c1 == c2 == len(grid)-1 : return grid[N-1][N-1]
        if (r1 , c1 , r2 , c2) in cache : 
            return cache[(r1 , c1 , r2 , c2)]
        cp = grid[r1][c1] + (grid[r2][c2] if r1!=r2 or c1!=c2 else 0)
        f1 = self.dfs(r1+1, c1, r2+1, c2 , grid ,  cache)
        f2 = self.dfs(r1+1, c1, r2, c2+1 , grid ,  cache)
        f3 = self.dfs(r1, c1+1, r2+1, c2 , grid ,  cache)
        f4 = self.dfs(r1, c1+1, r2, c2+1 , grid ,  cache)
        value =  cp +  max([f1, f2 , f3 , f4])
        cache[(r1 , c1,r2 , c2)] = value
        return value

    def cherryPickup(self, grid: List[List[int]]) -> int:
        cache = {}
        answer = self.dfs(0 , 0 , 0 , 0 , grid  , cache)
        return answer if answer >= 1 else 0