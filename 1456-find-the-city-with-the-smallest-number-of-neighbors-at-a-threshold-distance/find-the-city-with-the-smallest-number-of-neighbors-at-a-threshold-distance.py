class Solution:

    def dijkstra(self , root , n , adj_list):
        heap = [(0 , root)]
        distances = [float("inf") for _ in range(n)]
        distances[root] = 0 
        while heap  :
            root_distance , root = heapq.heappop(heap)
            for node , node_distance in adj_list[root] : 
                if root_distance + node_distance < distances[node] :
                    distances[node] = root_distance + node_distance
                    heapq.heappush(heap , (root_distance + node_distance , node))
        return distances


    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = [[] for _ in range(n)]
        for start , end , weight in edges :
            adj_list[start].append((end , weight))
            adj_list[end].append((start , weight))
        distances = []
        for i in range(n):
            distances.append(self.dijkstra(i , n ,adj_list))
        min_count = float("inf")
        city = None
        for i in range(n):
            d = distances[i]
            count = 0 
            for j in range(len(d)):
                if i == j : 
                    continue
                count += 1 if d[j] <= distanceThreshold else 0
            if count < min_count : 
                min_count = count
                city = i
            elif count == min_count : 
                city = max(city , i)
        return city