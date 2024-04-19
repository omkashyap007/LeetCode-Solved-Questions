class Solution:

    def bfs(self , i , j , grid , visited) :
        visited[i][j] = True
        queue = deque([(i,j)])
        dirs = [ (0,1) , (1,0) , (-1,0) , (0,-1)]
        while queue :
            i , j = queue.popleft()
            for dx , dy in dirs :
                x , y = i+dx , j+dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[i][j] ==  "1" and not visited[x][y] :
                    queue.append((x,y))
                    visited[x][y] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == "1" and not visited[i][j] : 
                    count += 1
                    self.bfs(i , j , grid , visited )
        return count