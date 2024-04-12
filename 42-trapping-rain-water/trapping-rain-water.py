class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0 
        left = [-1 for _ in range(len(height))]
        right = [-1 for _ in range(len(height))]
        max_left = float("-inf")
        max_right = float("-inf")
        for i in range(1 , len(height)):
            max_left = max(max_left , height[i-1])
            left[i] = max_left
        for j in range(len(height)-2 , -1 , -1):
            max_right = max(max_right , height[j+1])
            right[j] = max_right
        for i in range(1 , len(height)-1) :
            w = min(left[i] , right[i]) - height[i]
            water_trapped += w if w > 0 else 0 
        return water_trapped