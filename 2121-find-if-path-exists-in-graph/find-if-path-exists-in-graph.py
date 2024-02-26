class DSU : 
    def __init__(self , n , edges = []):
        self.n = n
        self.rank = [0 for _ in range(self.n)]
        self.parent = [i for i in range(self.n)]
        for u , v in edges :
            self.unionByRank(u,v)
        
    def findParent(self , u ):
        if self.parent[u] == u :
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent
    
    def unionByRank(self , u , v ):
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        rank_u = self.rank[parent_u]
        rank_v = self.rank[parent_v]
        if rank_u == rank_v : 
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_v)
            self.rank[parent_u] += 1
        elif rank_u > rank_v : 
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_v)
            self.rank[parent_u] += 1
        else : 
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_u)
            self.rank[parent_v] += 1

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu = DSU(n , edges)
        print(dsu.rank)
        print(dsu.parent)
        return dsu.findParent(source) == dsu.findParent(destination)