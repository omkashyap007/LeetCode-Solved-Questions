class DSU:
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
        size_v = self.size[parent_v]
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else : 
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]


class Solution:
    def findCircleNum(self, grid : List[List[int]]) -> int:
        dsu = DSU(len(grid))
        for i in range(len(grid)) :
            for j in range(len(grid)):
                if grid[i][j] == 1 :
                    dsu.union(i , j)
        count = 0
        for i in range(len(grid)):
            if dsu.parent[i] == i : count +=1
        return count