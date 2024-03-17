class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        answer = []
        i = 0
        while i < len(intervals):
            start , end = intervals[i][0] , intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end :
                end = max(end , intervals[j][1])
                j += 1
            answer.append([start , end])
            i = j
        return answer