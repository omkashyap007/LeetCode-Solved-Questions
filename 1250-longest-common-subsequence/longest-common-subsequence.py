class Solution:

    def dfs(self , i , j , s , p , cache):
        if i < 0 or j < 0 :
            return 0
        if (i,j) in cache :
            return cache[(i,j)]
        if s[i] == p[j] :
            value =  1 + self.dfs(i-1 , j-1 , s , p , cache)
        else : 
            value = max(self.dfs(i-1 , j , s , p , cache) , self.dfs(i, j-1 , s , p , cache))
            cache[(i,j)] = value
        return value
            

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        return self.dfs(len(text1) - 1 , len(text2)-1 , text1 , text2 , cache)