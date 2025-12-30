class Solution:

    def check(self, mat):
        if len(mat) != 3 or len(mat[0]) != 3:
            return False
        
        hash_set = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] in hash_set or mat[i][j] > 9 or mat[i][j] < 1:
                    return False
                hash_set.add(mat[i][j])
        row_sum = [sum(mat[i]) for i in range(len(mat))]
        col_sum = [0 , 0, 0]
        diag_sum = [0, 0]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                col_sum[j] += mat[i][j]
                if i == j:
                    diag_sum[0] += mat[i][j]
                if i+j == 2:
                    diag_sum[1] += mat[i][j]
        row_sum.extend(col_sum)
        row_sum.extend(diag_sum)
        is_magic = all(x == row_sum[0] for x in row_sum)
        return is_magic


    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                mat = [
                    [grid[i][j] for j in range(j, j+3)]
                    for i in range(i, i+3)
                ]
                count += self.check(mat)
        return count
               
