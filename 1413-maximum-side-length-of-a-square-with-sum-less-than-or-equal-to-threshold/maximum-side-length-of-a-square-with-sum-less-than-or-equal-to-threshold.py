class Solution:

    def getSum(self, i, j, x, y, prefix):
        _sum = (
            (prefix[i][j])
            - (prefix[x-1][j] if x-1 >= 0 else 0)
            - (prefix[i][y-1] if y-1 >= 0 else 0)
            + (prefix[x-1][y-1] if x-1 >= 0 and y-1 >= 0 else 0)
        )
        return _sum

    def maxSideLength(self, mat: List[List[int]], t: int) -> int:
        answer = 0
        ROWS, COLS = len(mat), len(mat[0])
        prefix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                a = prefix[i-1][j] if i-1 >=0 else 0
                b = prefix[i][j-1] if j-1 >=0 else 0 
                c = prefix[i-1][j-1] if i-1 >=0 and j-1 >=0 else 0
                d = mat[i][j]
                prefix[i][j] = a + b - c + d

        for i in range(ROWS):
            for j in range(COLS):
                k = min(ROWS-i, COLS-j)
                for offset in range(answer, k):
                    x, y = i+offset, j+offset
                    grid_sum = self.getSum(x, y, i, j, prefix)
                    if grid_sum <= t:
                        answer = max(answer, offset+1)
                    else:
                        break
        return answer
