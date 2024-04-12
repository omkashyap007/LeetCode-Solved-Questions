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
        if parent_u == parent_v : 
            return False
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU(n)
        cyclic_edges = 0
        for u , v in connections :
            if dsu.findParent(u) != dsu.findParent(v) :
                dsu.union(u,v)
            else :
                cyclic_edges += 1
        components = 0
        for i in range(n):
            if dsu.parent[i] == i :
                components += 1
        edges_required = components - 1
        if cyclic_edges >= edges_required :
            return edges_required
        return -1