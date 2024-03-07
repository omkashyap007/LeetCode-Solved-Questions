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
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        dsu = DSU(len(strs))
        for i in range(len(strs)):
            for j in range(i+1 , len(strs)):
                if dsu.findParent(i) == dsu.findParent(j) :
                    continue
                index = count = 0
                while index < len(strs[i]):
                    if strs[i][index] != strs[j][index] :
                        count += 1
                    index += 1
                if count == 2 :
                    dsu.union(i , j)
        comps = 0
        for i in range(len(strs)):
            if dsu.findParent(i) == i :
                comps += 1
        return comps