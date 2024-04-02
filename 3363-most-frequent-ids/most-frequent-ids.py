class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        hash_map = {}
        answer = []
        heap = []
        for i in range(len(nums)) :
            item = nums[i]
            frequency = freq[i]
            hash_map[item] = hash_map.get(item,0)-frequency
            heapq.heappush(heap , (hash_map[item] ,  item))
            while heap and hash_map[heap[0][1]] != heap[0][0] :
                heapq.heappop(heap)
            answer.append(0 if not heap else -heap[0][0])
        return answer