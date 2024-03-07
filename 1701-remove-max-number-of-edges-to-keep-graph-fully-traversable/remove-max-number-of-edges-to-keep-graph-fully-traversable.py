class DSU:
    def __init__(self , n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        self.comp = n

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
            return 0
        if size_u < size_v :
            self.parent[parent_u] = self.findParent(parent_v)
            self.parent[u] = self.findParent(parent_v)
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.parent[v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
        self.comp -= 1
        return 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)
        answer = 0
        for t , u , v in edges :
            if t == 3 :
                answer += alice.union(u,  v) | bob.union(u,v)
        for t , u , v in edges:
            if t == 1 :
                if alice.findParent(u) != alice.findParent(v):
                    answer += 1
                alice.union(u , v)
            if t == 2 :
                if bob.findParent(u) != bob.findParent(v):
                    answer += 1
                bob.union(u , v)
        if bob.comp <= 1 and alice.comp <= 1 :
            return len(edges)-answer
        return -1