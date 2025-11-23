class Solution:

    def getMaxLength(self, i, j, text1, text2):
        if i >= len(text1) or j >= len(text2):
            return 0
        elif text1[i] == text2[j]:
            return 1 + self.getMaxLength(i+1, j+1, text1, text2)
        else:
            return max(
                self.getMaxLength(i, j+1, text1, text2),
                self.getMaxLength(i+1, j, text1,  text2)
            )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    top = grid[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                    grid[i][j] = 1 + top
                else:
                    top = grid[i-1][j] if i-1 >= 0 else 0
                    left = grid[i][j-1] if j-1 >= 0 else 0
                    grid[i][j] = max(top, left)
        return grid[len(text1)-1][len(text2)-1]