class Solution:

    def binarySearch(self, i, target, events):
        index = len(events)
        j = len(events) - 1
        while i <= j:
            mid = (i+j) // 2
            if events[mid][0] > target:
                index = min(mid, index)
                j = mid -1
            else:
                i = mid +1
        return index

    def findMaxSum(self, index, count, events, cache):
        if index >= len(events) or count == 2:
            return 0
        
        if cache[index][count] != -1:
            return cache[index][count]

        next_valid_index = self.binarySearch(index+1, events[index][1], events)
        pick = events[index][2] + self.findMaxSum(next_valid_index, count+1, events, cache)
        not_pick = self.findMaxSum(index+1, count, events, cache)

        answer = max(pick, not_pick)
        cache[index][count] = answer
        return answer


    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        cache = [[-1, -1] for _ in range(len(events))]
        answer = self.findMaxSum(0, 0, events, cache)
        return answer
