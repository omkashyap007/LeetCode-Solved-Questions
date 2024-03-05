class DSU:
    def __init__(self , n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def findParent(self, u):
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

        if parent_u == parent_v: 
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for x,y in edges :
            n = max(n , x)
            n = max(n , y)
        dsu = DSU(n)
        answer = []
        for x , y in edges :
            if dsu.findParent(x) == dsu.findParent(y) :
                answer = [x,y]
            else :
                dsu.union(x,y)
        return answer        