class Solution:

    @cache
    def dfs(self , i , j):
        if i == 0 and i == 0:
            return 1
        up = self.dfs(i-1 , j) if i-1 >=0 else 0
        left = self.dfs(i,j-1) if j-1>=0 else 0
        return up+ left

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m-1,n-1)