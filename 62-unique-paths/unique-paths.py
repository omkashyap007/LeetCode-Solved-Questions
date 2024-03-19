class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]
        for i in range(m):
            prev_j = 0
            temp = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0 :
                    temp[j] = 1
                    prev_j = 1
                else:
                    temp[j] = dp[j] + prev_j
                    prev_j = temp[j]
            dp = temp
        return dp[-1]