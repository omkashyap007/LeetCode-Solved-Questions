class Solution:

    def markVisited(self ,  i , j , grid , visited ):
        if not ( 0 <= i <len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and not visited[i][j] ) :
            return
        visited[i][j] = True
        self.markVisited(i+1 , j , grid , visited)
        self.markVisited(i-1 , j , grid , visited)
        self.markVisited(i , j-1 , grid , visited)
        self.markVisited(i , j+1 , grid , visited)

    def findFarmland(self, grid : List[List[int]]) -> List[List[int]]:
        answer = []
        visited = [[False for _ in  range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j] :
                    group = [i , j , i , j]
                    nj = j
                    ni = i
                    while ni < len(grid) and grid[ni][j] == 1 :
                        ni += 1
                    group[2] = ni-1
                    while nj < len(grid[0]) and grid[i][nj] == 1 :
                        nj += 1 
                    group[3] = nj-1
                    self.markVisited(i ,j , grid, visited)
                    answer.append(group)
        return answer