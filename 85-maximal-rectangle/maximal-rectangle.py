class Solution:

    def largestRectangleInHistogram(self , l):
        stack = []
        max_area = 0
        for i in range(len(l)):
            min_index = i
            while stack and stack[-1][0] >= l[i] :
                ph , pi = stack.pop()
                area = ph*(i-pi)
                max_area = max(area , max_area)
                min_index = pi
            stack.append((l[i] , min_index))
        for h , i in stack :
            max_area = max(max_area , (h*(len(l)-i)))
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0 :
                    continue
                matrix[i][j] += matrix[i-1][j]
        max_area = 0
        for l in matrix :
            max_area = max(self.largestRectangleInHistogram(l) , max_area)
        return max_area