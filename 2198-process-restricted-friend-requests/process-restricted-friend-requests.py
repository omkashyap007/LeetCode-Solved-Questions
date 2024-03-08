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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu  = DSU(n)
        answer = []
        for x , y in requests :
            l , m  = dsu.findParent(x) , dsu.findParent(y)
            if l == m :
                answer.append(True)
                continue
            for a , b in restrictions :
                aa = dsu.findParent(a)
                bb = dsu.findParent(b)
                if (aa==l and bb==m) or (aa==m and bb==l) :
                    answer.append(False)
                    break
            else :
                answer.append(True)
                dsu.union(l,m)
        return answer