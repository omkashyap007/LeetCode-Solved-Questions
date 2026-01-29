from heapq import heappush, heappop

class Solution:

    def dijkstra(self, start_node, adj_list):
        distances = {start_node: 0}
        heap = [(0, start_node)]
        while heap:
            root_distance, root = heappop(heap)
            for node, node_distance in adj_list.get(root, []):
                new_distance = root_distance + node_distance
                if new_distance < distances.get(node, float("inf")):
                    distances[node] = new_distance
                    heappush(heap, (new_distance, node))
        return distances

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_list = {}
        distances = {}
        for index, char in enumerate(original):
            next_node = (changed[index], cost[index])
            if char in adj_list:
                adj_list[char].append(next_node)
            else:
                adj_list[char] = [next_node]

        for char in adj_list:
            distances[char] = self.dijkstra(char, adj_list)

        count = 0
        for index, source_char in enumerate(source):
            target_char = target[index]
            if source_char == target_char:
                continue
            else:
                if source_char not in distances:
                    return -1
                else:
                    dist = distances[source_char].get(target_char, float("inf"))
                    if dist == float("inf"):
                        return -1
                    else:
                        count += dist
        return count
