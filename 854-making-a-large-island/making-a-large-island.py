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
        if parent_u == parent_v :
            return
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]


class Solution:

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
        max_area = 0
        print(dsu.size)
        dirs = [(-1,0) , (0,1) , (1,0) , (0,-1)]
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
                        curr_area += dsu.size[dsu.findParent(x_y_num)]
                        parents.append(the_parent)
                max_area = max(max_area , curr_area + 1)    
        return n*n if max_area == 0 else max_area