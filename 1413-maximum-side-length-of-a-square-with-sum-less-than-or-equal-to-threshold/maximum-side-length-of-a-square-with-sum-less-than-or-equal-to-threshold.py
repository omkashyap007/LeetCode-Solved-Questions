class Solution:

    def getSum(self, i, j, x, y, prefix):
        _sum = (
            (prefix[i][j])
            - (prefix[x-1][j] if x-1 >= 0 else 0)
            - (prefix[i][y-1] if y-1 >= 0 else 0)
            + (prefix[x-1][y-1] if x-1 >= 0 and y-1 >= 0 else 0)
        )
        return _sum

    def binarySearch(self, i, j, k, prefix, t):
        answer = 0
        low = 0
        high = k
        while low <= high:
            mid = low + (high-low)//2
            _sum = self.getSum(i+mid, j+mid, i, j, prefix)
            if _sum <= t:
                answer = mid + 1
                low = mid + 1
            else:
                high = mid - 1
        return answer

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
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
                k = min(ROWS-i, COLS-j) - 1
                _answer = self.binarySearch(i, j, k, prefix, threshold)
                answer = max(answer, _answer)
        return answer
