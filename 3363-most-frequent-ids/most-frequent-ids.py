class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        frequency_map = {}
        answer = []
        heap = []
        for i in range(len(nums)) :
            item , frequency = nums[i] , freq[i]
            frequency_map[item] = frequency_map.get(item,0)-frequency
            heapq.heappush(heap , (frequency_map[item] ,  item))
            while heap and frequency_map[heap[0][1]] != heap[0][0] :
                heapq.heappop(heap)
            answer.append(0 if not heap else -heap[0][0])
        return answer