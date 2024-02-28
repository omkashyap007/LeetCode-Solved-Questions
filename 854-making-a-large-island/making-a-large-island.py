class DSU :
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def findParent(self , u):
        if self.parent[u] == u :
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent
    
    def union(self , u , v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        size_u = self.size[parent_u]
        size_v  = self.size[parent_v]

        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]


class Solution:

    def bfs(self , i , j , grid , visited , area , dsu , dirs):
        n = len(grid)
        visited[i][j] = True
        area = 0
        queue = deque([(i,j)])
        while queue : 
            i ,  j = queue.popleft()
            area += 1
            for dx , dy in dirs :
                x = i+dx
                y = j+dy
                if  x>=0 and x<n and y>=0 and y<n and grid[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    queue.append((x,y))
        return area

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n*n)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 :
                    for dx , dy in [(-1,0),(0,-1)] :
                        x = i+dx
                        y = j+dy
                        if x>=0 and x<n and y>= 0 and y<n and grid[x][y] == 1 :
                            curr = i*n+j
                            adj  = x*n+y
                            dsu.union(adj , curr)
        visited = [[False for _ in range(n)] for _ in range(n)]
        area = [0 for _ in range(n*n)]
        max_area = 0
        dirs = [(-1,0) , (0,1) , (1,0) , (0,-1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    the_area = self.bfs(i , j , grid , visited , area , dsu , dirs )
                    parent = dsu.findParent(i*n+j)
                    area[parent] = the_area
                    max_area = max(max_area , the_area)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 :
                    continue
                parents = []
                curr_area = 0
                for dx , dy in dirs :
                    x = i+dx
                    y = j+dy
                    if not ( x>=0 and x<n and y>=0 and y<n and grid[x][y] == 1 ) :
                        continue
                    x_y_num = x*n+y
                    the_parent =  dsu.findParent(x_y_num) 
                    if the_parent not in parents :
                        curr_area += area[dsu.findParent(x_y_num)]
                        parents.append(the_parent)
                max_area = max(max_area , curr_area + 1)    
        return max_area