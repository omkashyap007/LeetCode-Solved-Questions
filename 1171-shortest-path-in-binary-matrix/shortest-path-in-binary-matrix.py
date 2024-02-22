class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 : 
            return -1
        min_distance = float("inf")
        N = len(grid)-1
        dirs = [
            (-1, 0) , 
            (-1, 1) , 
            ( 0, 1) , 
            ( 1, 1) , 
            ( 1, 0) , 
            ( 1,-1) , 
            ( 0,-1) , 
            (-1,-1) 
        ]
        distances = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
        distances[0][0] = 1
        queue = deque([(1 , 0 , 0)])
        while queue :
            distance , x , y = queue.popleft()
            if x == N and y == N :
                min_distance = min(min_distance , distance)
                continue
            for dx , dy in dirs :
                i , j = x+dx , y+dy
                if i>=0 and i <= N and j>=0 and j <=N and grid[i][j] == 0 and distance+1 < distances[i][j] :
                    distances[i][j] = distance+1
                    queue.append((distance+1 , i , j))
        return -1 if min_distance == float("inf") else min_distance