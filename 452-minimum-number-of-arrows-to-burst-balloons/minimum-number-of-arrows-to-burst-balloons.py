class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key = lambda x : x[0] )
        i = 0 
        while i < len(points):
            start , end = points[i]
            j = i  + 1 
            while j < len(points) and points[j][0] <= end :
                end = min(end , points[j][1])
                j += 1 
            count += 1
            i = j
        return count