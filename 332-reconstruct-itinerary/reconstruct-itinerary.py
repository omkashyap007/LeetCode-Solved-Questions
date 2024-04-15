class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {root  : [] for root , _ in tickets}
        for start , end in tickets :
            heapq.heappush(adj_list[start] , end )
        path = []
        def dfs(root) :
            if root not in adj_list :
                path.insert(0 , root)
                return
            while adj_list[root] :
                node = heapq.heappop(adj_list[root])
                dfs(node)
            path.insert(0, root)
        dfs("JFK")
        return path