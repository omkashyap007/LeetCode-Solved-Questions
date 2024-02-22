class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        efforts = [[float("inf") for _ in range(M)] for _ in range(N)]
        efforts[0][0] = 0
        min_effort = float("inf")
        dirs = [(-1,0) , (0,1) , (1,0) , (0,-1)]
        heap = [(0 , 0 , 0)]
        while heap :
            effort , x , y = heapq.heappop(heap)
            if x == N-1 and y == M-1 :
                min_effort = min(min_effort, effort)
                continue
            for dx,dy in dirs :
                i , j = x+dx , y+dy
                if i>=0 and i<N and j>=0 and j<M :
                    abs_diff = abs(grid[i][j] - grid[x][y])
                    new_effort = max(abs_diff , effort)
                    if new_effort < efforts[i][j] :
                        efforts[i][j] = new_effort
                        heapq.heappush(heap , (new_effort , i , j))
        return min_effort