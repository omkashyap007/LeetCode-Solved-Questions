import heapq

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        #pre process grid 
        m = len(grid)
        n = len(grid[0])
        
        cells=[]

        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j],i,j))
        cells.sort()

        ptr = [0]*(k+1)

        dist = [[[math.inf for _ in range(n)] for _ in range(m)] for _ in range(k+1)]
        dist[0][0][0] = 0

        heap = [(0,0,0,0)]

        while heap:
            cost, t, i, j = heapq.heappop(heap)

            if cost>dist[t][i][j]:
                continue

            if i==m-1 and j==n-1:
                return cost
            
            if i<m-1:
                new_cost = cost + grid[i+1][j]
                if new_cost<dist[t][i+1][j]:
                    dist[t][i+1][j]=new_cost
                    heapq.heappush(heap,(new_cost, t, i+1, j))
            if j<n-1:
                new_cost = cost + grid[i][j+1]
                if new_cost<dist[t][i][j+1]:
                    dist[t][i][j+1]=new_cost
                    heapq.heappush(heap, (new_cost,t,i,j+1))
            
            if t<k:
                v = grid[i][j]

                while ptr[t]<len(cells) and cells[ptr[t]][0] <= v:
                    _, x, y = cells[ptr[t]]

                    if cost < dist[t+1][x][y]:
                        dist[t+1][x][y]=cost
                        heapq.heappush(heap,(cost,t+1,x,y))
                    ptr[t]+=1
                