class Solution:

    def dfs(self, i, j,  l, m, cache):
        if i >= len(l) or j >= len(m):
            return 0
        
        if (i,j) in cache:
            return cache[(i, j)]

        if l[i] == m[j]:
            return 1 + self.dfs(i+1, j+1, l, m, cache)
        a = self.dfs(i+1, j, l, m, cache)
        b = self.dfs(i, j+1, l, m, cache)
        answer =max(a, b)
        cache[(i, j)] = answer
        return answer


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        return self.dfs(0, 0, text1, text2, cache)