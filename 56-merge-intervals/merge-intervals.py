class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        answer = []
        i = 0
        while i < len(intervals):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= curr_end :
                curr_end = max(curr_end , intervals[j][1])
                j += 1
            answer.append([curr_start , curr_end])
            i = j
        return answer