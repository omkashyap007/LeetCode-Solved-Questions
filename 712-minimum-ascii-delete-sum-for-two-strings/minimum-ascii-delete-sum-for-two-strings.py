class Solution:

    def dfs(self, i, j, s1, s2, cache):
        if i >= len(s1) and j >= len(s2):
            return 0
        
        if (i, j) in cache:
            return cache[(i,j)]

        if i >= len(s1):
            return ord(s2[j]) + self.dfs(i, j+1, s1, s2, cache)
        if j >= len(s2):
            return ord(s1[i]) + self.dfs(i+1, j, s1, s2,  cache)

        if s1[i] == s2[j]:
            return self.dfs(i+1, j+1, s1, s2, cache)
        a = ord(s1[i]) + self.dfs(i+1, j, s1, s2, cache)
        b = ord(s2[j]) + self.dfs(i, j+1, s1, s2, cache)
        answer = min(a, b)
        cache[(i, j)] = answer
        return answer


    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cache = {}
        return self.dfs(0, 0, s1, s2, cache)
