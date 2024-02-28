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
            self.size[parent_v] += self.size[parent_u]
            self.parent[u] = self.findParent(parent_v)
        else :
            self.parent[parent_v] = self.findParent(parent_u)
            self.size[parent_u] += self.size[parent_v]
            self.parent[v] = self.findParent(parent_u)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        hash_map = {}
        for i in range(len(accounts)):
            for j in range(1 ,  len(accounts[i])):
                mail = accounts[i][j]
                if mail in hash_map :
                    dsu.union(i , hash_map[mail])
                else : 
                    hash_map[mail] = i
        a = [set() for _ in range(n)]
        for i in range(len(accounts)):
            for j in range(1 , len(accounts[i])) :
                mail = a[dsu.findParent(i)].add(accounts[i][j])
        answer = []
        for i in range(len(a)):
            if a[i] :
                l = [accounts[i][0]] + sorted(list((a[i])))
                answer.append(l)
        return answer