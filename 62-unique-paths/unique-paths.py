class Solution:

    def dfs(self, i, j, m, n, cache):
        if i > m or j > n:
            return 0
        if i == m and j == n:
            return 1
        if (i,j) in cache:
            return cache[(i,j)]
        left = self.dfs(i+1, j, m, n, cache)
        right = self.dfs(i, j+1, m, n, cache)
        cache[(i,j)] = left + right
        return left + right

    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.dfs(0, 0, m-1,n-1, cache)