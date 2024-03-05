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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        max_index = 0
        hash_set = set()
        for x ,y in pairs :
            max_index = max(x,max_index)
            max_index = max(y , max_index)
            hash_set.add(x)
            hash_set.add(y)
        dsu = DSU(max_index+1)
        for x , y in pairs :
            dsu.union(x,y)
        hash_map = {}
        for i in hash_set :
            parent = dsu.findParent(i)
            if parent in hash_map :
                hash_map[parent].add(i)
            else : 
                hash_map[parent] = set([i])
        string = list(s)
        for key in hash_map :
            indices = sorted(list(hash_map[key]))
            values = [s[i] for i in indices]
            values.sort()
            for i in range(len(values)):
                string[indices[i]] = values[i]
        return "".join(string)