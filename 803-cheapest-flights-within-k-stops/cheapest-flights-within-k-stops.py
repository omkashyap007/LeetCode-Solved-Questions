class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], source : int, destination : int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for start , end , price in flights :
            adj_list[start].append((end,price))
        costs = [float("inf") for _ in range(n)]
        costs[source] = 0
        heap = [(0 , 0 , source)]
        min_cost = float("inf")
        while heap :
            stops , cost , root = heapq.heappop(heap)
            if root == destination :
                min_cost = min(min_cost , cost)
                continue
            if stops > k : 
                continue
            for node , node_cost in adj_list[root] :
                new_cost = cost + node_cost
                if stops <= k and new_cost < costs[node] :
                    costs[node] = new_cost
                    heapq.heappush(heap , (stops+1 , new_cost , node))
        return -1 if min_cost == float("inf") else min_cost