class Solution:

    def markVisited(self ,  i , j , grid , visited ):
        if not ( 0 <= i <len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and not visited[i][j] ) :
            return
        visited[i][j] = True
        self.markVisited(i+1 , j , grid , visited)
        self.markVisited(i-1 , j , grid , visited)
        self.markVisited(i , j-1 , grid , visited)
        self.markVisited(i , j+1 , grid , visited)

    def dfs(self , i , j , grid ,visited , group) :
        if not ( 0 <= i <len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and not visited[i][j] ) :
            return
        visited[i][j] = True
        group[2] = max(group[2] , i)
        group[3] = max(group[3] , j)
        self.dfs(i+1 , j , grid , visited ,group)
        self.dfs(i , j+1 , grid , visited ,group)

    # def bfs(self ,  i, j , grid ,  visited) :
    #     group = [i , j , i , j]
    #     visited[i][j] = True
    #     queue = deque([(i,j)])
    #     while queue : 
    #         i , j = queue.popleft()
    #         for

    def findFarmland(self, grid : List[List[int]]) -> List[List[int]]:
        answer = []
        visited = [[False for _ in  range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j] :
                    group = [i , j , i , j]
                    self.dfs(i , j, grid , visited , group)
                    # answer.append(self.bfs(i , j, grid , visited))
                    answer.append(group)
        return answer