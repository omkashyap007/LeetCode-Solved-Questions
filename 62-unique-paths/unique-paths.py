class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            temp = [0 for _ in range(n)]
            prev_j = 0
            for j in range(n):
                if i == 0 and j == 0 : 
                    dp[j] = 1
                    temp[j] = 1
                    prev_j = 1
                    continue
                up = dp[j]
                left = prev_j
                temp[j] = up + left
                prev_j = temp[j]
            dp = temp
        return dp[n-1]