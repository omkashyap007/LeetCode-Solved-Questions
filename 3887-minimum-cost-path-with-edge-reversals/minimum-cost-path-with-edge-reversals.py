class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # init
        distances = {}
        distances[0] = 0
        for i in range(1,n):
            distances[i] = float('inf')
        
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,2*w))
        
        # dijkstras
        minHeap = [(0,0)] #(weight, node)
        while minHeap:
            w, u = heapq.heappop(minHeap)
            if w > distances[u]:
                continue

            for v, dw in adj[u]:
                nw = w + dw
                if nw < distances[v]:
                    distances[v] = nw
                    heapq.heappush(minHeap,(nw, v))

        return -1 if distances[n-1] == float('inf') else distances[n-1]