class DSU:
    def __init__(self , n ):
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
    def removeStones(self, stones: List[List[int]]) -> int:
        ROWS = 0
        COLS = 0
        for x , y in stones : 
            ROWS = max(ROWS , x+1)
            COLS = max(COLS , y+1)
        dsu = DSU(ROWS+COLS+1)
        comps = 0
        hash_set = set()
        for x , y in stones :
            x_row = x
            y_col = y + ROWS + 1
            dsu.union(x_row , y_col)
            hash_set.add(x_row)
            hash_set.add(y_col)
        for i in hash_set :
            if dsu.findParent(i) == i :
                comps += 1
        return len(stones) - comps