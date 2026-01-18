class Solution:

    def isMagic(self, grid):
        k = len(grid)
        if not k:
            return False
        s = sum(grid[0])
        
        for x in grid:
            if sum(x) != s:
                return False
        for y in range(len(grid[0])):
            _s = 0
            for x in range(len(grid)):
                _s += grid[x][y]
            if _s != s:
                return False
        _s1 = 0
        _s2 = 0
        for x in range(k):
            _s1 += grid[x][x]
            _s2 += grid[x][k-x-1]
        if _s1 != s:
            return False
        if _s2 != s:
            return False
        return True


    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        answer = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l = min(
                    len(grid) - i+1,
                    len(grid[0]) - j+1
                )
                for k in range(l):
                    _grid = [row[j:j+k] for row in grid[i:i+k]]
                    if self.isMagic(_grid):
                        answer = max(answer, k)

        return answer
