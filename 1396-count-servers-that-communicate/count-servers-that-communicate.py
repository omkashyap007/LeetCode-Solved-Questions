class DSU :
    def __init__(self , n):
        self.parent = [i for i in  range(n)]
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
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dsu = DSU(ROWS*COLS)
        server_count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 :
                    for x in range(i-1 , -1 , -1):
                        if grid[x][j] == 1 :
                            x_num = x*COLS+j
                            i_num = i*COLS+j
                            dsu.union(x_num , i_num)
                    for y in range(j , -1 , -1):
                        if grid[i][y] == 1 :
                            y_num = i*COLS+y
                            j_num = i*COLS+j
                            dsu.union(y_num , j_num)
                    server_count += 1
        disconnected = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 :
                    num = i*COLS+j
                    if dsu.parent[num] == num and dsu.size[num] == 1 :
                        disconnected += 1
        return server_count-disconnected