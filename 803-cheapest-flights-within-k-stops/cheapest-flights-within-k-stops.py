class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], source: int, destination: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for src , dst , cost in flights :
            adj_list[src].append((dst , cost))
        queue = deque([(0 , source , 0)])
        min_distance = float("inf")
        distances = [float("inf") for _ in range(n)]
        while queue :
            stops , root , cost = queue.popleft()
            if root == destination :
                min_distance = min(min_distance , cost)
            if stops > k : 
                continue
            for node , node_distance in adj_list[root] :
                new_distance = node_distance + cost
                if stops <= k and new_distance < distances[node] :
                    distances[node] = new_distance
                    queue.append((stops+1 , node , new_distance))
        return -1 if min_distance == float("inf") else min_distance