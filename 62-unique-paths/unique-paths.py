class Solution:

    def dfs(self , i , j , cache):
        if (i,j) in cache : 
            
            return cache[(i,j)]
        if i == 0 and j == 0:
            return 1
        up = self.dfs(i-1 , j , cache) if i-1 >=0 else 0
        left = self.dfs(i,j-1 , cache) if j-1>=0 else 0
        cache[(i,j)] = up+left
        return up+left

    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.dfs(m-1,n-1 , cache)