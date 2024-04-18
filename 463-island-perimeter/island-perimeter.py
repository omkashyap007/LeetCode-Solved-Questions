class Solution:

    def bfs(self , i , j , grid) :
        count = 0
        queue = deque([(i,j)])
        dirs = [ (0,1) , (1,0) , (-1,0) ,  (0,-1) ]
        while queue : 
            i , j = queue.popleft()
            grid[i][j] = -1
            for dx , dy in dirs : 
                x = i+dx
                y = j+dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) :
                    if grid[x][y] == 1 :
                        grid[x][y] = -1
                        queue.append((x,y))
                    if grid[x][y] == 0 :
                        count += 1
                else :
                    count += 1
        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    return self.bfs(i , j , grid )
        return 0