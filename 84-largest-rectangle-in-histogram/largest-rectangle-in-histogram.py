class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for index, height in enumerate(heights):
            start_index = index
            while stack and stack[-1][1] >= height:
                prev_index, prev_height = stack.pop()
                area = prev_height * (index - prev_index)
                max_area = max(max_area, area)
                start_index = prev_index
            stack.append((start_index, height))
        
        while stack:
            prev_index, prev_height = stack.pop()
            area = prev_height * (len(heights) - prev_index)
            max_area = max(area, max_area)
        return max_area
