class Solution:

    def dfs(self , i , j , grid , squares , required_squares , count) :
        if not (0<= i < len(grid) and 0 <= j < len(grid[0]) ) or grid[i][j] == "*" :
            return
        if grid[i][j] == -1 :
            return 
        if grid[i][j] == 2 :
            if squares + 1 == required_squares :
                count[0] += 1
            return
        cell_value = grid[i][j]
        grid[i][j] = "*"
        top = self.dfs(i-1 , j , grid , squares  + 1, required_squares , count)
        left = self.dfs(i , j-1 , grid , squares  + 1, required_squares , count)
        down = self.dfs(i+1 , j , grid , squares  + 1, required_squares , count)
        right = self.dfs(i , j+1 , grid , squares  + 1, required_squares , count)
        grid[i][j] = cell_value

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x = y = None
        required_squares = len(grid)*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] == -1 :
                    required_squares -= 1
                if grid[i][j] == 1 :
                    x = i
                    y = j
        count = [0]
        self.dfs(
            x , y , grid , 0 , required_squares , count
        )
        return count[0]


"""

pseudo code : 

if out of bounds ) or ( visited )  : return

if (i,j) == end : if s + 1 == required_squares : count += 1

visit cel : 
    move 4 dirs :

unvisite the cell./


"""