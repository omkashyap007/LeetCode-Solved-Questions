class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        grid = [[-1 for _ in range(len(matrix))] for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         grid[j][len(matrix)-i-1] = matrix[i][j]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)) :
        #         matrix[i][j] = grid[i][j]
        
        for i in range(len(matrix)):
            for j in range(i , len(matrix)) :
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[0])-1
            while l < r :
                matrix[i][l] , matrix[i][r] = matrix[i][r] , matrix[i][l]
                l += 1
                r -= 1