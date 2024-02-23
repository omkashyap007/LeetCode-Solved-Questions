class Solution:
    MOD = 10**9 + 7

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for start , end , time in roads :
            adj_list[start].append((end,time))
            adj_list[end].append((start,time))
        distances = [float("inf") for _ in range(n)]
        ways = [0 for _ in range(n)]
        distances[0] = 0
        ways[0] = 1
        heap = [(0 , 0)]
        while heap :
            distance , root = heapq.heappop(heap)
            if root == n-1 :
                continue
            for node , node_dist in adj_list[root] :
                new_distance = node_dist + distance
                if new_distance < distances[node] :
                    distances[node] = new_distance
                    ways[node] = ways[root]
                    heapq.heappush(heap , (new_distance , node))
                elif new_distance == distances[node] :
                    ways[node] += ways[root]
                    ways[node]%=self.MOD
        return ways[n-1]%self.MOD