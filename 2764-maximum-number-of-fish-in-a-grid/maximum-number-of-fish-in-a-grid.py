class Solution:

    def bfs(self , i , j , visited , grid):
        queue = deque([(i,j)])
        dirs = [(0,1) , (1,0) , (-1,0) , (0,-1)]
        area = 0 
        while queue :
            i,j = queue.popleft()
            area += grid[i][j]
            visited[i][j] = True
            for dx,dy in dirs :
                x,y = i+dx,j+dy
                if x>=0 and x < len(grid) and y>=0 and y < len(grid[0]) and not visited[x][y] and grid[x][y] > 0 : 
                    queue.append((x,y))
                    visited[x][y] = True
                    
        return area
            

    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and not visited[i][j] : 
                    max_area = max(max_area , self.bfs(i , j , visited , grid))
        return max_area