class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjacent_list = defaultdict(list)
        queue = deque()
        in_degree = [0]*n
        remaining_nodes = n
        result = []

        for edge0, edge1 in edges:
            adjacent_list[edge0].append(edge1)
            adjacent_list[edge1].append(edge0)
            in_degree[edge0] += 1
            in_degree[edge1] += 1

        for i in range(n):
            if in_degree[i] == 1:
                queue.append(i)
       

        while(remaining_nodes > 2):           
            remaining_nodes -= len(queue)   
                      
            for _  in range(len(queue)): 
                node = queue.popleft()            
                neighbors = adjacent_list[node]                
                for nei in neighbors:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        queue.append(nei)
        while(queue):
            n = queue.popleft()
            result.append(n)

        return result 
        