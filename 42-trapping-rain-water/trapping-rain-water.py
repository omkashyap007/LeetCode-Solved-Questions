class Solution:
    def trap(self, height: List[int]) -> int:
        right_max_array = [0 for _ in range(len(height))]
        left_max = height[0]
        right_max = height[-1]
        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            right_max_array[i] = right_max
        
        water = 0
        for i in range(len(height)):
            left_max = max(left_max, height[i])
            min_height = min(right_max_array[i], left_max)
            _water = min_height - height[i]
            water += _water if _water > 0 else 0
        return water
