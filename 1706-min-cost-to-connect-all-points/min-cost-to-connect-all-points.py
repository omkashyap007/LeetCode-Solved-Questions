class DSU : 
    def __init__(self , n) :
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        
    def findParent(self , u ):
        if self.parent[u] == u :
            return u
        parent = self.findParent(self.parent[u])
        self.parent[u] = parent
        return parent

    def union(self , u , v) :
        parent_u = self.findParent(u)
        parent_v = self.findParent(v)
        if parent_u == parent_v :
            return False
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
        return True
        

class Solution:
    def manhattenDistance(self , first , second) :
        return abs(first[0] - second[0]) + abs(first[1] - second[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int :
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            for j in range(i+1 , n) :
                dist = self.manhattenDistance(points[i] , points[j])
                edges.append((i,j,dist))
        edges.sort(key = lambda x : x[2])
        the_sum = 0
        for u , v , dist in edges :
            the_sum += dist if dsu.union(u,v) else 0
        return the_sum