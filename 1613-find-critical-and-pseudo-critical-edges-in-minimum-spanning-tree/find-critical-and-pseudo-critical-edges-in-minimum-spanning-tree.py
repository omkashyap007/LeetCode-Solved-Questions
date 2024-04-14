class DSU : 
    def __init__(self , n) :
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.components = n
    
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
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else :
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]
        self.components -= 1
        return True

class Solution:

    def findMST(self , edges , skip , add , n) :
        dsu = DSU(n)
        mst_weight = 0
        if add != -1 :
            u ,  v , weight , _ = edges[add]
            dsu.union(u , v)
            mst_weight += weight
        for i in range(len(edges)):
            if i == skip :
                continue
            u , v , weight , _ = edges[i]
            mst_weight += weight if dsu.union(u,v) else 0
        print(dsu.components)
        if dsu.components == 1 :
            return mst_weight
        return -1


    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key = lambda x : x[2])
        mst = self.findMST(edges , -1 , -1 , n)
        print(f"MST of tree : {mst}")
        critical = []
        pseudo_critical = []
        for i in range(len(edges)):
            skip = self.findMST(edges , i , -1 , n)
            add = self.findMST(edges , -1 , i , n)
            print(f"The skip , add : {skip} , {add}")
            if skip > mst or skip == -1: 
                critical.append(edges[i][3])
            elif add == mst :
                pseudo_critical.append(edges[i][3])
        return [critical , pseudo_critical]