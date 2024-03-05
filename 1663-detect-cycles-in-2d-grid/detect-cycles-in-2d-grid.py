class DSU:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def findParent(self , u ):
        if self.parent[u] == u :
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent

    def union(self , u , v):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        size_u = self.size[parent_u]
        size_v = self.size[parent_v]

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
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])
        dsu = DSU(ROWS*COLS)
        dirs = [(-1,0) , (0,-1)]
        for i in range(ROWS):
            for j in range(COLS):
                for dx,dy in dirs :
                    x , y = i+dx , j+dy
                    if x>=0 and x < ROWS and y >=0 and y < COLS and grid[x][y] == grid[i][j] :
                        i_j_num = i*COLS + j
                        x_y_num = x*COLS + y
                        if dsu.findParent(i_j_num) == dsu.findParent(x_y_num) :
                            return True
                        else :
                            dsu.union(i_j_num , x_y_num)
        return False