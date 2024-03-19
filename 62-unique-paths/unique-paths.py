class Solution:
    
    def dfs(self , i , j , rows , cols , cache):
        if (i,j) in cache : return cache[(i,j)]
        if i == 0 or j == 0 :
            return 1
        if i<0 or j<0 :
            return 0
        up = self.dfs(i-1 ,  j , rows , cols , cache )
        right = self.dfs(i , j-1 , rows , cols , cache)
        cache[(i,j)] = up+right
        return up+right

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m-1 , n-1 , m , n , cache = {})