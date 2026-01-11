class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start_index = i
            while stack and stack[-1][1] >= heights[i]:
                prev_index, prev_height = stack.pop()
                area = (i-prev_index)*prev_height
                max_area = max(area, max_area)
                start_index = prev_index
            stack.append((start_index, heights[i]))
        while stack:
            prev_index, prev_height = stack.pop()
            max_area = max(max_area, (len(heights) - prev_index) * prev_height)        
        return max_area
