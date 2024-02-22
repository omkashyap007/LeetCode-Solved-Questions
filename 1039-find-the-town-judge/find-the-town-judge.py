class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 :
            return 1
        adj_list = [set() for _ in range(n+1)]
        for start , end in trust :
            adj_list[start].add(end)
        judge = None
        for i in range(1,len(adj_list)):
            if len(adj_list[i]) == 0 :
                if judge == None :
                    judge = i
                else :
                    return -1
        elements = set([i for i in range(1,n+1)])
        for i in range(1, len(adj_list)):
            if not adj_list[i] :
                continue
            elements.intersection_update(adj_list[i])
        if not elements :
            return -1
        a = elements.pop()
        if a == judge :
            return a
        return -1