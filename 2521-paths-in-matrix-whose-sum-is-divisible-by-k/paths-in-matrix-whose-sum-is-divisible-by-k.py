class Solution:

    def getPaths(self, i, j, curr_sum, k, grid, cache):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        
        if i == len(grid)-1 and j == len(grid[0])-1:
            return (curr_sum + grid[i][j])%k == 0

        if (i, j, curr_sum) in cache:
            return cache[(i, j, curr_sum)]
        new_sum = (curr_sum + grid[i][j])%k

        right = self.getPaths(i, j+1, new_sum, k, grid, cache)
        down = self.getPaths(i+1, j, new_sum, k, grid, cache)
        answer = right+ down
        cache[(i, j, curr_sum)] = answer

        return answer


    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        cache = {}
        return self.getPaths(0, 0, 0, k, grid, cache)% (10**9+ 7)