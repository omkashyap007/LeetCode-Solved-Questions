class Solution:
    def recursiveTask(self, grid, currentId, X, Y):
        grid[X][Y] = currentId

        if X > 0 and grid[X - 1][Y] == 1:
            self.recursiveTask(grid, currentId, X - 1, Y)
        if X < len(grid) - 1 and grid[X + 1][Y] == 1:
            self.recursiveTask(grid, currentId, X + 1, Y)
        if Y > 0 and grid[X][Y - 1] == 1:
            self.recursiveTask(grid, currentId, X, Y - 1)
        if Y < len(grid) - 1 and grid[X][Y + 1] == 1:
            self.recursiveTask(grid, currentId, X, Y + 1)

    def largestIsland(self, grid: List[List[int]]) -> int:
        currentId = -1
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    self.recursiveTask(grid, currentId, i, j)
                    currentId -= 1
        
        # print(grid)

        if currentId == -1:
            return 1
            
        areaDict = {}

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] < 0:
                    if grid[i][j] in areaDict:
                        areaDict[grid[i][j]] += 1
                    else:
                        areaDict[grid[i][j]] = 1
        
        # print(areaDict)

        maximumIsland = max(areaDict.values())

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    answer = 1
                    islands = set()
                    if i > 0 and grid[i - 1][j] < 0:
                        islands.add(grid[i - 1][j])
                    if i < len(grid) - 1 and grid[i + 1][j] < 0:
                        islands.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] < 0:
                        islands.add(grid[i][j - 1])
                    if j < len(grid) - 1 and grid[i][j + 1] < 0:
                        islands.add(grid[i][j + 1])
                    
                    for island in islands:
                        answer += areaDict[island]

                    maximumIsland = max(maximumIsland, answer)


        return maximumIsland



        