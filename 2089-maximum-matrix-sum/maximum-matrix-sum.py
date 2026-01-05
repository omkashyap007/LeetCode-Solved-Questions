class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_num = float("inf")
        negative_count = 0
        _sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ae = abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negative_count += 1
                if ae < min_num:
                    min_num  = ae
                _sum += ae
        if negative_count % 2 == 1:
            _sum -= min_num*2
        return _sum
            
